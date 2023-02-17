# AI-Chat-Email-Analytics-GUI
Analyze chat/email data for ediscovery, customer sentiment, HR and more with Azure Cognitive Services. This GUI uses Pandas, Tkinter, and requests to extract insights via sentiment analysis, keyphrases, and named entity recognition. Developed by MahumTech, import your data and filter it based on email addresses, then view results in a new window.

## Usage

1. Clone this repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run `python main.py` to start the GUI.

The GUI consists of several input widgets:

- **Endpoint**: The endpoint for the Azure Cognitive Services API.
- **Access Key**: The access key for the Azure Cognitive Services API.
- **CSV File Path**: The path to the CSV file containing the email or chat data.
- **Sender Email**: The email address of the sender.
- **Receiver Email**: The email address of the receiver.

To use the tool, enter the required information in the input widgets and click the **Analyze** button. The tool will import the email or chat data, filter it based on the sender and receiver email addresses, perform sentiment analysis, keyphrase extraction, named entity recognition, and known entity linking using Azure Cognitive Services, save the results to a CSV file, and display the results in a table in a new window.

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

## Use Cases

Here are ten ways this code can be used to analyze chat or email data:

1. **eDiscovery**: Analyze email data to identify relevant documents for eDiscovery purposes.
2. **Customer Sentiment Analysis**: Analyze customer emails to determine sentiment and identify areas for improvement.
3. **HR Complaints**: Analyze employee emails to identify HR complaints and improve the workplace.
4. **Marketing Campaigns**: Analyze customer emails to identify customer preferences and improve marketing campaigns.
5. **Product Feedback**: Analyze customer emails to identify product feedback and improve product development.
6. **Fraud Detection**: Analyze chat data to identify fraudulent behavior and prevent fraud.
7. **Competitor Analysis**: Analyze customer emails to identify competitor mentions competitor mentions and sentiment to gain a competitive edge.
8. **Sales Strategy**: Analyze customer emails to identify common questions or issues and tailor sales strategies accordingly.
9. **Market Research**: Analyze customer emails to identify industry trends and gather market research data.
10. **Brand Reputation**: Analyze customer emails to identify negative sentiment and improve brand reputation.

## Contributing
We welcome contributions to improve the codebase. Feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For more information, contact us at info@mahumtech.com or visit our website at https://mahumtech.com.

## Disclaimer
This code is provided as-is with no warranty or support. Use at your own risk.
