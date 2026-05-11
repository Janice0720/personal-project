"""Task 1 EDA 驗證腳本"""
import pandas as pd

df_20     = pd.read_csv('data/raw/111_綜所稅各類所得20分位統計.csv')
df_5      = pd.read_csv('data/raw/111_綜所稅各類所得5分位統計.csv')
df_region = pd.read_csv('data/raw/111_全國各縣市鄉鎮村里所得統計.csv')

print("=== 各檔案形狀 ===")
print(f"20分位統計: {df_20.shape}")
print(f"5分位統計:  {df_5.shape}")
print(f"村里統計:   {df_region.shape}")

print("\n=== 20分位欄位 ===")
print(df_20.columns.tolist())

print("\n=== 5分位欄位 ===")
print(df_5.columns.tolist())

print("\n=== 20分位所得結構（前5列）===")
df_20_clean = df_20[df_20.iloc[:, 0].str.contains("第", na=False)].copy()
cols_show = [c for c in ['分位別','薪資所得','股利所得','利息所得','租賃及權利金','執行業務所得'] if c in df_20.columns]
print(df_20_clean[cols_show].head().to_string(index=False))

print("\n=== 5分位薪資收入均值（千元）===")
df_5_clean = df_5[df_5.iloc[:, 0].str.contains("第", na=False)].copy()
cols5 = [c for c in ['分位別','薪資所得','股利所得','利息所得','薪資收入'] if c in df_5.columns]
print(df_5_clean[cols5].to_string(index=False))

print("\n=== 村里統計欄位 ===")
print(df_region.columns.tolist())
print(f"村里統計筆數（扣除標題）: {len(df_region)}")
print(f"中位數範圍: {df_region['中位數'].min()} ~ {df_region['中位數'].max()} 千元")
