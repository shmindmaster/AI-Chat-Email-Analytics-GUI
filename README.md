# AI-Chat-Email-Analytics-GUI
Analyze chat/email data for ediscovery, customer sentiment, HR and more with Azure Cognitive Services. This GUI uses Pandas, Tkinter, and requests to extract insights via sentiment analysis, keyphrases, and named entity recognition. Developed by MahumTech, import your data and filter it based on email addresses, then view results in a new window.

## Use Cases

Here are ten ways this code can be used to analyze chat or email data:

1. **eDiscovery**: Analyze email data to identify relevant documents for eDiscovery purposes.
2. **Customer Sentiment Analysis**: Analyze customer emails to determine sentiment and identify areas for improvement.
3. **HR Complaints**: Analyze employee emails to identify HR complaints and improve the workplace.
4. **Marketing Campaigns**: Analyze customer emails to identify customer preferences and improve marketing campaigns.
5. **Product Feedback**: Analyze customer emails to identify product feedback and improve product development.
6. **Fraud Detection**: Analyze chat data to identify fraudulent behavior and prevent fraud.
7. **Competitor Analysis**: Analyze customer emails to identify competitor mentions and improve competitive intelligence.
8. **Customer Support**: Analyze customer emails to identify customer support issues and improve customer support.
9. **Customer Churn**: Analyze customer emails to identify customer churn and improve customer retention.
10. **Customer Segmentation**: Analyze customer emails to identify customer segments and improve customer segmentation.

## Usage

1. Clone this repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run `python main.py` to start the GUI.

## Technical Details

The tool is built using Python and several libraries, including:

- `pandas` for importing the email or chat data into a Pandas DataFrame.
- `requests` for making API calls to Azure Cognitive Services.
- `tqdm` for displaying a progress bar.
- `csv` for saving the results to a CSV file.
- `tkinter` for creating the GUI.

The GUI consists of several input widgets, including:

- **Endpoint Entry**: An entry widget for the Azure Cognitive Services API endpoint.
- **Access Key Entry**: An entry widget for the Azure Cognitive Services API access key.
- **CSV File Path Entry**: An entry widget for the path to the CSV file containing the email or chat data.
- **Sender Email Entry**: An entry widget for the email address of the sender.
- **Receiver Email Entry**: An entry widget for the email address of the receiver.
- **Browse Button**: A button for browsing for the CSV file containing the email or chat data.
- **Analyze Button**: A button for analyzing the email or chat data.

When the user clicks the **Analyze** button, the tool imports the email or chat data into a Pandas DataFrame, filters it based on the sender and receiver email addresses, and performs sentiment analysis, keyphrase extraction, named entity recognition, and known entity linking using Azure Cognitive Services. The results are saved to a CSV file and displayed in a table in a new window.

The tool also includes a cache object to optimize API performance by caching results to avoid duplicate calls. This improves the tool's performance and reduces the number of API calls required.
