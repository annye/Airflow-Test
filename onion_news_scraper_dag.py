from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
import requests
import json
import time
from bs4 import BeautifulSoup


from plugins.onion_scraper.scrape_onion import scrape_onion
from plugins.onion_scraper.scrape_check_these_out import scrape_check_these_out
from plugins.onion_scraper.scrape_trending import scrape_trending
from plugins.onion_scraper.scrape_watch import scrape_watch





default_args = {
    'owner': 'annye',
}

@dag(dag_id='dag_scraper_taskflow',
     description='DAG using the scrapers in a TaskFlow API',
     default_args=default_args,
     start_date=days_ago(1),
     schedule_interval='@once',
     tags=['dependencies', 'python', 'taskflow_api'])
def dag_scraper_taskflow_api():
    
    @task
    def task_scrape_onion():
        scrape_onion()
    
    @task
    def task_scrape_check_these_out():
        scrape_check_these_out()
    
    @task
    def task_scrape_trending():
        scrape_trending()
    
    @task
    def task_scrape_watch():
        scrape_watch()
    
    @task
    def task_combine_results():
        # Combine results if needed, this is just an example
        print("Combining results from all scrapers")

    task_onion = task_scrape_onion()
    task_check_these_out = task_scrape_check_these_out()
    task_trending = task_scrape_trending()
    task_watch = task_scrape_watch()
    task_combine = task_combine_results()

    [task_onion, task_check_these_out, task_trending, task_watch] >> task_combine

dag_scraper_taskflow_api()
