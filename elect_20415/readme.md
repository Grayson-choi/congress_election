django 2.x 버전

1. 카카오 챗봇 만들기로 챗봇 생성
2. 스킬 탭에서 새 스킬 생성
3. URL / Test URL 에(둘다 등록) url 등록하는데 ngrok.exe 사용!
  * $ ngrok.exe http 포트번호 
  * 위처럼 입력하면 https 주소가 있는데 그걸로 외부 접속 가능
  * 해당 주소에 kakao/checkserver/ 경로로 url 등록하면됨.
4. 해당 스킬 설정창 하단에 스킬 테스트 항목이 있음
  * TestURL 선택하고 스킬서버로 전송하면 아래에 응답이 돌아옴.
  * 해당 응답 보고 통신 상태 확인. 

5. 제대로 응답하면 시나리오 하나 만들고 스킬 붙여주면됨.
https://i.kakao.com/docs/skill-block#%EB%B8%94%EB%A1%9D%EA%B3%BC-%EC%8A%A4%ED%82%AC-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0

여기 참고
