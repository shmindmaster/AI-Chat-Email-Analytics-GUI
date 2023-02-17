import pandas as pd
import requests
import tqdm
import csv
import tkinter as tk
from tkinter import filedialog


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chat/Email Data Analysis")
        self.window.geometry("500x400")

        # Create input widgets
        tk.Label(self.window, text="Endpoint").grid(row=0, column=0)
        self.endpoint_entry = tk.Entry(self.window)
        self.endpoint_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Access Key").grid(row=1, column=0)
        self.access_key_entry = tk.Entry(self.window)
        self.access_key_entry.grid(row=1, column=1)

        tk.Label(self.window, text="CSV File Path").grid(row=2, column=0)
        self.file_path_entry = tk.Entry(self.window)
        self.file_path_entry.grid(row=2, column=1)
        tk.Button(self.window, text="Browse",
                  command=self.browse_file).grid(row=2, column=2)

        tk.Label(self.window, text="Sender Email").grid(row=3, column=0)
        self.sender_email_entry = tk.Entry(self.window)
        self.sender_email_entry.grid(row=3, column=1)

        tk.Label(self.window, text="Receiver Email").grid(row=4, column=0)
        self.receiver_email_entry = tk.Entry(self.window)
        self.receiver_email_entry.grid(row=4, column=1)

        tk.Button(self.window, text="Analyze",
                  command=self.analyze_data).grid(row=5, column=1)

        # Initialize file_path attribute
        self.file_path = ""

        self.window.mainloop()

    def browse_file(self):
        # Open file dialog to select file
        file_path = filedialog.askopenfilename()
        # Update file path entry widget
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)
        # Update file_path attribute
        self.file_path = file_path

    def analyze_data(self):
        # Import the email or chat data into a Pandas Dataframe
        chat_data = pd.read_csv(self.file_path, encoding='utf-8')

        # Filter email or chat data based on the sender and receiver's email addresses
        filtered_df = chat_data[
            (
                (chat_data["From"].str.lower() ==
                 self.sender_email_entry.get().lower())
                & (chat_data["To"].str.lower() == self.receiver_email_entry.get().lower())
            )
            | (
                (chat_data["From"].str.lower() ==
                 self.receiver_email_entry.get().lower())
                & (chat_data["To"].str.lower() == self.sender_email_entry.get().lower())
            )
        ].reset_index(drop=True)

        # Set up Text Analytics endpoints and access keys
        headers = {"Ocp-Apim-Subscription-Key": self.access_key_entry.get(),
           "Content-Type": "application/json"}

        # Create cache object to Optimize API performance by caching results to avoid duplicate calls
        cache = {}

        # Create a Process_Text function that makes API calls to sentiment analysis, keyphrase extraction, named entity recognition, and known entity linking, and returns the results
        def process_text(text):
            if text in cache:
                return cache[text]
            else:
                # Create a dictionary to store the results
                results = {}

                # Retrieve the endpoint and access key values entered by the user
                endpoint = self.endpoint_entry.get()
                access_key = self.access_key_entry.get()

                # Create a dictionary to store the text analytics endpoints
                endpoints = {
                    "sentiment": endpoint + "/text/analytics/v3.2-preview.2/sentiment",
                    "key_phrases": endpoint + "/text/analytics/v3.2-preview.2/keyPhrases",
                    "entities": endpoint + "/text/analytics/v3.2-preview.2/entities/recognition/general",
                    "linked_entities": endpoint + "/text/analytics/v3.2-preview.2/entities/linking"
                }

                # Create a dictionary to store the text analytics parameters
                params = {
                    "sentiment": {"documents": [{"id": "1", "text": text}]},
                    "key_phrases": {"documents": [{"id": "1", "text": text}]},
                    "entities": {"documents": [{"id": "1", "text": text}]},
                    "linked_entities": {"documents": [{"id": "1", "text": text}]}
                }

                # Loop through the endpoints and parameters dictionaries to make API calls
                for endpoint, param in zip(endpoints, params):
                    response = requests.post(endpoints[endpoint], headers={
                                             "Ocp-Apim-Subscription-Key": access_key, "Content-Type": "application/json"}, json=params[endpoint])
                    response.raise_for_status()
                    results[endpoint] = response.json()

                # Add the results to the cache object
                cache[text] = results

            return results

        # Analyze the chat data and display the results
        results = []
        for i in tqdm.tqdm(range(len(filtered_df))):
            text = filtered_df.loc[i, "Message"]
            analysis = process_text(text)
            results.append(analysis)

        # Save the results to a CSV file
        with open('results.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Text', 'Sentiment', 'Key Phrases',
                             'Entities', 'Linked Entities'])
            for i in range(len(filtered_df)):
                text = filtered_df.loc[i, 'Message']
                analysis = results[i]
                sentiment = analysis['sentiment']['documents'][0]['sentiment']
                key_phrases = ', '.join(
                    analysis['key_phrases']['documents'][0]['keyPhrases'])
                entities = ', '.join(
                    [e['text'] for e in analysis['entities']['documents'][0]['entities']])
                linked_entities = ', '.join(
                    [e['name'] for e in analysis['linked_entities']['documents'][0]['entities']])
                writer.writerow([text, sentiment, key_phrases,
                                entities, linked_entities])

        # Create a new window to display the results
        result_window = tk.Toplevel(self.window)
        result_window.title("Analysis Results")
        result_window.geometry("800x600")

        # Create a table to display the results
        table = tk.Frame(result_window)
        table.pack(side="top")

        # Create the headers for the table
        headers = ["Text", "Sentiment", "Key Phrases",
                   "Entities", "Linked Entities"]
        for j in range(len(headers)):
            tk.Label(table, text=headers[j]).grid(row=0, column=j)

        # Add the results to the table
        for i in range(len(filtered_df)):
            tk.Label(table, text=filtered_df.loc[i, "Message"]).grid(
                row=i+1, column=0)
            tk.Label(table, text=results[i]["sentiment"]["documents"][0]["sentiment"]).grid(
                row=i+1, column=1)
            tk.Label(table, text=", ".join(
                results[i]["key_phrases"]["documents"][0]["keyPhrases"])).grid(row=i+1, column=2)
            entities = ", ".join(
                [entity["text"] for entity in results[i]["entities"]["documents"][0]["entities"]])
            tk.Label(table, text=entities).grid(row=i+1, column=3)
            linked_entities = ", ".join(
                [entity["name"] for entity in results[i]["linked_entities"]["documents"][0]["entities"]])
            tk.Label(table, text=linked_entities).grid(row=i+1, column=4)


# Create a GUI object
if __name__ == '__main__':
    gui = GUI()
