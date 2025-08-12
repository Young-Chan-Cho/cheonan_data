import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
# 윈도우: Malgun Gothic / 맥: AppleGothic
plt.rc('font', family='Malgun Gothic')  # 또는 'AppleGothic'
plt.rc('axes', unicode_minus=False)     # 마이너스 기호 깨짐 방지
# 데이터 불러오기
df = pd.read_excel('main_dataset.xlsx') # 교통사고 데이터
df2 = pd.read_excel('traffic_data.xlsx') # 교통량 데이터

df.info()
df2.info()
len(df2['구간명'].unique())

# '발생년월'을 datetime 형식으로 변환
df['발생년월_dt'] = pd.to_datetime(df['발생년월'], format='%Y년 %m월')
# 시간순 정렬
df.sort_values('발생년월_dt',inplace=True)
# 월별 건수 집계 (시간순)
counts = df['발생년월_dt'].value_counts().sort_index()
# 교통사고 시간별 시각화
plt.figure(figsize=(12, 6))
sns.barplot(x=counts.index.strftime('%Y-%m'), y=counts.values, palette='viridis')
plt.xticks(rotation=45)
plt.xlabel('발생년월')
plt.ylabel('사고 건수')
plt.title('발생년월별 사고 건수')
# ✅ y축 간격 줄이기 (예: 100 단위)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25))
plt.show()

# 시군구별 교통사고 건수 집계
counts = df['시군구'].value_counts()
# 시군구별 시각화
plt.figure(figsize=(12, 6))
sns.barplot(x=counts.index, y=counts.values, palette='viridis')
plt.xticks(rotation=45)
plt.xlabel('시군구')
plt.ylabel('사고 건수')
plt.title('시군구별 교통사고 건수')
plt.show()

# 가해자차종/ 피해자차종 차종 시각화
# 데이터 집계
counts_gahae = df['가해운전자 차종'].value_counts()
counts_pihae = df['피해운전자 차종'].value_counts()

# 가해운전자 차종 시각화
plt.figure(figsize=(12, 5))
sns.barplot(x=counts_gahae.index, y=counts_gahae.values, palette='Reds')
plt.xticks(rotation=45)
plt.title('가해운전자 차종별 사고 건수')
plt.xlabel('차종')
plt.ylabel('사고 건수')
plt.show()

# 피해운전자 차종 시각화
plt.figure(figsize=(12, 5))
sns.barplot(x=counts_pihae.index, y=counts_pihae.values, palette='Blues')
plt.xticks(rotation=45)
plt.title('피해운전자 차종별 사고 건수')
plt.xlabel('차종')
plt.ylabel('사고 건수')
plt.show()


df2['구간명'].value_counts()

# 교차로 사고 데이터만 필터링
df.head()
df['도로형태'].unique()
df_cross = df[df['도로형태'].str.startswith('교차로')]
df_cross.reset_index(inplace=True,drop=True)
df_cross # 교차로 사고 데이터프레임

# 교차로에서 많이 사고가 나타나는 차종 유형 
counts_type = df_cross['가해운전자 차종'].value_counts()
sns.barplot(x=counts_type.index, y=counts_type.values, palette='Blues')
plt.xticks(rotation=45)
plt.title('교차로 가해운전자 차종별 사고 건수')
plt.xlabel('차종')
plt.ylabel('사고 건수')
plt.show()

# 단일로 사고 데이터만 필터링
df_straight = df[df['도로형태'].str.startswith('단일로')]
df_straight.reset_index(inplace=True,drop=True)
df_straight # 단일로 사고 데이터프레임
# 단일로에서 많이 사고가 나타나는 차종 유형 
counts_type = df_straight['가해운전자 차종'].value_counts()
sns.barplot(x=counts_type.index, y=counts_type.values, palette='Blues')
plt.xticks(rotation=45)
plt.title('단일로 가해운전자 차종별 사고 건수')
plt.xlabel('차종')
plt.ylabel('사고 건수')
plt.show()

# 교통량 많은 구간 
len(df2['구간명'].unique())
df2['구간명'].value_counts()
df2_group = df2.groupby(['도로명','구간명'])['교통량(대)'].mean().reset_index()
df2_group.head(30)
df2_group.sort_values('교통량(대)',ascending=False).head(30)

df_cross

counts = df_cross['발생년월_dt'].value_counts().sort_index()
# 교통사고 시간별 시각화
plt.figure(figsize=(12, 6))
sns.barplot(x=counts.index.strftime('%Y-%m'), y=counts.values, palette='viridis')
plt.xticks(rotation=45)
plt.xlabel('발생년월')
plt.ylabel('사고 건수')
plt.title('발생년월별 사고 건수')
# ✅ y축 간격 줄이기 (예: 100 단위)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25))
plt.show()

df.columns
df['피해운전자 차종'].value_counts()
df['가해운전자 차종'].value_counts()

df.info()
df2.info()

df2_group

636.2




