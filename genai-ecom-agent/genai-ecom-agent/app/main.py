from fastapi import FastAPI
from pydantic import BaseModel
from app.llm_agent import generate_sql
from app.query_engine import run_sql_query

app = FastAPI()

class Question(BaseModel):
    user_question: str

@app.post("/ask")
def ask_question(data: Question):
    schema_hint = """
    ad_sales_metrics(item_id, date, ad_sales, impressions, ad_spend, clicks, units_sold),
    total_sales_metrics(item_id, date, total_sales, total_units_ordered),
    eligibility(item_id, eligibility_datetime_utc, eligibility, message)
    """


    sql = generate_sql(data.user_question, schema_hint)
    result = run_sql_query(sql)
    return {"query": sql, "result": result}
