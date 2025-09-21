# LinkedIn Post Generator with LangChain & Streamlit

This project is a **LangChain-powered application** with a **Streamlit web UI** that generates LinkedIn posts tailored to specific styles, tones, and creators. It leverages a curated dataset of posts (with engagement metadata), preprocesses them to extract contextual information, and then uses an LLM to generate new posts that closely match the writing style of selected creators.

## 🚀 Features

- **Interactive Streamlit UI**

  - Four **dropdown menus** in a columnar layout:

    - **Tag (Title)** – Select thematic category (e.g., Tech, AI, Leadership).
    - **Language** – _English_ or _Hinglish_.
    - **Creator** – Choose the creator whose style you want to mimic.
    - **Length** – _Short_, _Medium_, or _Long_.

- **Metadata Extraction**

  - Line count → Post length classification.
  - Language detection → English or Hinglish.
  - Tag assignment.
  - Engagement mapping for insights.

- **Style Imitation**

  - Mimics the tone, vocabulary, and structure of selected creators.

## 📂 Data

- **Input JSON**:

  ```json
  {
    "post_text": "Your sample post here...",
    "engagement": {
      "likes": 120,
      "comments": 15,
      "shares": 5
    },
    "creator": "John Doe"
  }
  ```

- **Source**: Manually curated (can be extended with **Bright Data** or **LinkedIn scraping**).
- **Preprocessing**: Extract metadata (tags, length, language) via LLM pipeline.

## 🛠️ Tech Stack

- **LangChain** – LLM workflow orchestration.
- **Streamlit** – Web-based interactive UI.
- **LLMs** – Metadata extraction & post generation.
- **Python** – Core logic.
- **Bright Data / LinkedIn scraping** – (optional) dataset enrichment.

## ⚙️ Workflow

1. **Data Collection** – Gather raw JSON posts.
2. **Preprocessing** – Extract metadata (tags, language, length).
3. **Streamlit UI** – User selects dropdown values:

   - Tag (Title)
   - Language
   - Creator
   - Length

4. **Post Generation** – LangChain + LLM generate post with given context.

## 🖥️ Streamlit UI

- The UI consists of **four dropdowns aligned in columns**.
- Example layout:

```python
import streamlit as st

col1, col2, col3, col4 = st.columns(4)

with col1:
    tag = st.selectbox("Tag (Title)", tag_options)

with col2:
    language = st.selectbox("Language", ["English", "Hinglish"])

with col3:
    creator = st.selectbox("Creator", creator_options)

with col4:
    length = st.selectbox("Length", ["Short", "Medium", "Long"])
```

- After selection, clicking **"Generate Post"** triggers the LangChain pipeline to produce the post.

## 📊 Example

### Input Selections:

- Tag: _AI_
- Language: _Hinglish_
- Creator: _John Doe_
- Length: _Short_

### Output (Sample):

> "AI ke bina aaj kal kuch bhi possible nahi lagta 🚀
> From productivity tools to business decisions, har jagah AI hai.
> The question is – are we ready to adapt fast enough?"

## 🚧 Future Enhancements

- Richer dataset via automated scraping.
- Fine-tuned models for each creator’s style.
- Post-performance prediction.
- Multi-user dashboard with analytics.

## 📌 Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/blazerrt86899/streamlit-linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open browser at:

   ```
   http://localhost:8501
   ```

## 🤝 Contributing

Contributions are welcome! Please open an issue or PR for suggestions, bug fixes, or enhancements.

## 📜 License

MIT License – feel free to use, modify, and share.
