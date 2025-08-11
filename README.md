# cheonan_data-
# 천안시 공공데이터 경진대회

# 주제 : 법규위반 집중 구간 분석 및 예방 정책 제언

# 사용 데이터:
## 2022 ~ 2024년 천안시 교통사고 데이터 ( 행: 9700개 )/n
data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9708 entries, 0 to 9707
Data columns (total 22 columns):
   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   구분번호        9708 non-null   int64 
 1   발생년월        9708 non-null   object
 2   주야          9708 non-null   object
 3   시군구         9708 non-null   object
 4   사고내용        9708 non-null   object
 5   사망자수        9708 non-null   int64 
 6   중상자수        9708 non-null   int64 
 7   경상자수        9708 non-null   int64 
 8   부상신고자수      9708 non-null   int64 
 9   사고유형        9708 non-null   object
 10  법규위반        9708 non-null   object
 11  노면상태        9708 non-null   object
 12  기상상태        9708 non-null   object
 13  도로형태        9708 non-null   object
 14  가해운전자 차종    9708 non-null   object
 15  가해운전자 성별    9708 non-null   object
 16  가해운전자 연령대   9708 non-null   object
 17  가해운전자 상해정도  9708 non-null   object
 18  피해운전자 차종    9437 non-null   object
 19  피해운전자 성별    9437 non-null   object
 20  피해운전자 연령대   9437 non-null   object
 21  피해운전자 상해정도  9437 non-null   object
dtypes: int64(5), object(17)

## 2022 ~ 2024년 천안시 교통량 데이터 /n

## data.info()
Data columns (total 7 columns):
    Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   도로명            2028 non-null   object
 1   구간명            2028 non-null   object
 2   평균속도(km/h)     2028 non-null   int64 
 3   통행속도 최저(km/h)  2028 non-null   int64 
 4   통행속도 최고(km/h)  2028 non-null   int64 
 5   교통량(대)         2028 non-null   int64 
 6   혼잡시간           2028 non-null   int64 
dtypes: int64(5), object(2)
memory usage: 111.0+ KB

# 분석 내용

아래와 같은 내용을 분석하여 인사이트를 도출하고, 정책을 제언

'교통량이 많을 수록, 교통사고가 많은지' <br>
'혼잡시간에 교통사고량이 많은지'  <br>
'특정지역에 교통사고가 많은지' <br>
'가해운전자 연령대별 교통사고' <br>
'도로형태별 교통사고 현황' <br>
'시간대별(주간, 야간) 교통사고 현황' <br>
