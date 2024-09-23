# GraphRAG-Biology

## Overview

GraphRAG-Biology is a specialized implementation of Microsoft's GraphRAG framework, tailored for processing and analyzing biological research papers. This project leverages the structured, hierarchical approach to Retrieval Augmented Generation (RAG) provided by GraphRAG to enhance the analysis of complex biological information.

## Setup and Usage

Follow these steps to set up and use GraphRAG-Biology:

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Create an input directory and add your text files:
   ```bash
   mkdir ./input
   # Add your text files to the ./input directory
   ```
   If you don'T have text files, you can use the example files in the `./input` directory, or use the pdf_extractor.py to extract text from pdfs

3. Initialize and index the GraphRAG project:
   ```bash
   # Initialize the project
   python -m graphrag.index --init --root .   

   # Index the documents
   python -m graphrag.index --root .  
   ```

4. Query the GraphRAG:
   ```bash
   python -m graphrag.query --root . --method local "Your query here"
   ```

   Full usage:
   ```
   python -m graphrag.query [-h] [--config CONFIG] [--data DATA] [--root ROOT] --method {local,global} [--community_level COMMUNITY_LEVEL] [--response_type RESPONSE_TYPE] [--streaming] query
   ```




## Example Query

Here's an example of how to query the GraphRAG:

```bash
python -m graphrag.query --root . --method local "What is the relationship between AA and minoxidil?"
```

## Purpose

The main goals of this project are to:

1. Extract and connect complex biological entities, relationships, and claims from research papers.
2. Generate comprehensive summaries of biological communities and their interactions.
3. Provide advanced reasoning capabilities for complex biological queries.


