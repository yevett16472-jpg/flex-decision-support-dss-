import pandas as pd
import sqlite3

def get_surge_data():
    # Connect to the primary vault
    conn = sqlite3.connect('flex_system.db')
   
    try:
        # Querying the confirmed Pasadena_Surges table
        query = "SELECT * FROM Pasadena_Surges ORDER BY timestamp ASC"
        df = pd.read_sql_query(query, conn)
       
        # Calculate price delta for trend analysis
        df['price_diff'] = df['offer_amount'].diff()
       
        # Flag reset events (drops > $50) for the Pandora's Box logic
        df['is_reset'] = df['price_diff'] < -50
       
        return df
       
    except Exception as e:
        print(f"Error querying table: {e}")
        return pd.DataFrame() # Return empty if table not found
    finally:
        conn.close()

if __name__ == "__main__":
    data = get_surge_data()
    print("Data successfully retrieved:")
    print(data.tail())