# -- 코드를 입력하세요
# SELECT MCDP_CD AS 진료과코드,
# count(APNT_YMD) AS 5월예약건수
# From APPOINTMENT
# where APNT_YMD like '2022-05-%'
# GROUP BY 진료과코드
# ORDER BY 5월예약건수 ASC, 진료과코드 ASC