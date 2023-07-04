import psycopg2
import os
# Database connection configuration
# Database connection configuration
# DB_HOST = 'dpg-cih699tgkuvojj9dkc1g-a.singapore-postgres.render.com'
# DB_NAME = 'techrs'
# DB_USER = 'raj'
# DB_PASSWORD = 'YTDz4j8qlITR9etxzzWeNZ6nV4Lr02ER'
# DB_PORT = '5432'

# url = 'postgres://raj:YTDz4j8qlITR9etxzzWeNZ6nV4Lr02ER@dpg-cih699tgkuvojj9dkc1g-a.singapore-postgres.render.com/techrs'

url = os.environ.get('DATABASE_URL')
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    url
    # host=DB_HOST,
    # database=DB_NAME,
    # user=DB_USER,
    # password=DB_PASSWORD,
    # port=DB_PORT
)
