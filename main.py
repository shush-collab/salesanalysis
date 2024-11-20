import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path): # Load Data
    if file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        data = pd.read_csv(file_path)
    return data



def clean_data(data): # Clean Data
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_') # Standardize column names
    data['sales_amount'] = pd.to_numeric(data['sales_amount'], errors='coerce')# Ensure numeric values are valid
    data['purchase_date'] = pd.to_datetime(data['purchase_date'], errors='coerce')# Convert dates
    data = data.dropna()# Drop missing and duplicate data
    data = data.drop_duplicates()
    
    print("Data cleaned successfully!")
    return data

def analyze_expensive_items(data):# Analyze Expensive Items
    expensive_regions = data.groupby('region')['sales_amount'].mean().sort_values(ascending=False)
    print(f"\nRegions with higher average sales amounts:\n{expensive_regions}")
    return expensive_regions


def analyze_demand(data): # Analyze Demand
    demand_by_region = data['region'].value_counts()
    print(f"\nRegions with the most demand:\n{demand_by_region}")
    return demand_by_region


def visualize_expensive_items(expensive_regions): # Visualize Expensive Items
    expensive_regions.plot(kind='bar', title="Average Sales Amount by Region", xlabel="Region", ylabel="Average Sales", color='purple')
    plt.show()


def visualize_demand(demand_by_region): # Visualize Demand
    demand_by_region.plot(kind='bar', title="Number of Orders by Region", xlabel="Region", ylabel="Order Count", color='orange')
    plt.show()


def analyze_trends(data): # Analyze and Visualize Sales Trends
    data['month'] = data['purchase_date'].dt.to_period('M')
    monthly_sales = data.groupby('month')['sales_amount'].sum()
    print(f"\nMonthly sales trends:\n{monthly_sales}")
    return monthly_sales

def visualize_trends(monthly_sales):
    monthly_sales.plot(kind='line', title="Monthly Sales Trends", xlabel="Month", ylabel="Total Sales", color='green', marker='o')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    file_path = "data/crm_data.xlsx"
    data = load_data(file_path)
    
    data = clean_data(data)
        
    expensive_regions = analyze_expensive_items(data)
    visualize_expensive_items(expensive_regions)
    
    demand_by_region = analyze_demand(data)
    visualize_demand(demand_by_region)
        
    monthly_sales = analyze_trends(data)
    visualize_trends(monthly_sales)
