


translation unit 

.o , .o  링크 -> exe 파일 


각각의 transfer unit 에서 

1. 전역 변수, 전역 변수 -> ( 이름 충돌 )
2. static 변수, 전역 변수 -> ( 충돌 안남, internal linkage )
3. 젼역 변수, extern -> (충돌 안남, external linkage)
4. static, extern -> ( 빌드에러 , external 찾지 못함. )