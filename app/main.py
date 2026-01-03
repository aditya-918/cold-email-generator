import os

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/116.0 Safari/537.36"
)
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text



def create_streamlit_app(llm, portfolio):
        st.title("Cold Email Generator")
        url_input = st.text_input("Enter a URL:", value="https://careers.nike.com/principal-researcher-basketball-innovation/job/R-74967")

        if st.button("Submit"):
                try:
                        loader = WebBaseLoader([url_input])
                        docs = loader.load()
                        if not docs:
                                st.error("No content could be loaded from this URL.")
                        else:
                                page_content = docs.pop().page_content
                                data = clean_text(page_content)

                                portfolio.load_portfolio()
                                jobs = llm.extract_jobs(data)
                        

                        for job in jobs:
                                skills = job.get('skills', [])
                                links = portfolio.query_links(skills)
                                email = llm.write_mail(job, links)
                                st.code(email, language='markdown')
                except Exception as e:
                        st.error(f"An Error occurred: {e}")



if __name__ == "__main__":
        chain = Chain()
        portfolio = Portfolio()
        st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="")
        create_streamlit_app(chain, portfolio)


