# HomeMatch: AI-Powered Real Estate Matching

HomeMatch is an innovative application that leverages large language models (LLMs) and vector databases to transform standard real estate listings into personalized narratives tailored to potential buyers' unique preferences and needs.

## Project Overview

HomeMatch revolutionizes how clients interact with real estate listings by creating a personalized experience for each buyer. The application:

1. Generates real estate listings using LLMs
2. Stores these listings in a vector database
3. Collects buyer preferences through interactive questions
4. Matches properties to buyer preferences using semantic search
5. Personalizes property descriptions to highlight aspects most relevant to the buyer
6. Presents enhanced listings to the buyer

## Prerequisites

### Python Environment

- **Python 3.12** is required for this project
- [uv](https://github.com/astral-sh/uv) package manager for dependency management
- Jupyter Notebook for running the `.ipynb` file

### Setting up Python with uv

```bash
# Install uv (if not already installed)
curl -sSf https://install.python-poetry.org | python3 -

# Create a virtual environment with Python 3.12
uv venv -p 3.12

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### Required Environment Variables

The following environment variables need to be set:

- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_API_BASE`: Base URL for OpenAI API (default is "https://openai.vocareum.com/v1")
- `DEFAULT_PROVIDER`: Provider to use (default is "OPEN_AI", can also be "LM_STUDIO")

You can set these environment variables in your shell before running the application:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export OPENAI_API_BASE="https://openai.vocareum.com/v1"
export DEFAULT_PROVIDER="OPEN_AI"
```

## Installation

1. Clone the repository (if not already done)
2. Navigate to the project directory
3. Install dependencies using uv:

```bash
cd 4_Building_Generative_AI_Solutions/final_project
uv sync
```

This will install all required dependencies specified in the `pyproject.toml` file, including:
- langchain
- openai
- pydantic
- sentence-transformers
- transformers
- chromadb
- tiktoken
- jupyter
- langchain-community
- lancedb
- pandas
- jq

## Running the Application

The HomeMatch application is contained in a Jupyter Notebook. To run it:

1. Ensure your virtual environment is activated and environment variables are set
2. Launch Jupyter Notebook:

```bash
jupyter notebook
```

3. Open the `HomeMatch.ipynb` file
4. Run the notebook cells sequentially to:
   - Generate real estate listings
   - Store listings in the vector database
   - Collect buyer preferences
   - Find matching properties
   - Enhance property descriptions
   - Present personalized listings

### Application Workflow

The notebook follows these steps:

1. **Generating Real Estate Listings**: Creates sample real estate listings using an LLM and saves them to a JSON file
2. **Storing Listings in a Vector Database**: Loads the generated listings into ChromaDB for vector search
3. **Building the User Preference Interface**: Collects buyer preferences through a series of questions
4. **Searching Based on Preferences**: Uses the structured buyer preferences to perform semantic search on the vector database
5. **Personalizing Listing Descriptions**: Enhances property descriptions to highlight aspects that match buyer preferences
6. **Presenting Results**: Displays the personalized property listings to the buyer

### Test Mode vs. Interactive Mode

The application can run in two modes:
- **Test Mode**: Uses predefined buyer preferences for quick testing
- **Interactive Mode**: Prompts the user to input their preferences in real-time

## Application Architecture

### Key Components

- **LLM Provider**: Handles interactions with the language model (OpenAI or LM Studio)
- **Vector Store**: Manages the vector database for semantic search (ChromaDB)
- **Real Estate Listings**: JSON data containing property information
- **Buyer Preference Collection**: Interface for gathering buyer requirements
- **Semantic Search**: Matches buyer preferences to property listings
- **Description Enhancement**: Personalizes property descriptions based on preferences

### Directory Structure

```
root/
├── HomeMatch.ipynb       # Main application notebook
├── README.md             # This documentation
├── pyproject.toml        # Project dependencies
├── real_estate_listings.json  # Generated property listings
└── src/
    ├── configs.py        # Configuration and environment variables
    ├── provider.py       # LLM provider implementation
    └── db/
        ├── chroma_db.py  # Vector database implementation
        ├── generate_sample_data.py  # Data generation utilities
        └── models/
            └── real_estate_listing.py  # Data models
```

## Troubleshooting

### Common Issues

1. **Missing Environment Variables**:
   - Ensure all required environment variables are set
   - Check that your API keys are valid

2. **Dependency Issues**:
   - Make sure you're using Python 3.12
   - Try reinstalling dependencies with `uv sync`

3. **Vector Database Errors**:
   - Ensure ChromaDB is properly installed
   - Check that the real estate listings JSON file exists

4. **LLM API Errors**:
   - Verify your OpenAI API key is correct
   - Check your internet connection
   - Ensure you're not exceeding API rate limits

For additional help, refer to the documentation of the individual libraries used in this project.
