# AGENTS.md

이 저장소에서 AI 코딩 도구가 지켜야 할 규칙입니다.

- Python 3.12. 패키지는 `requirements.txt`에 있는 것만 쓴다. 추가가 필요하면 먼저 물어본다
- API Key는 `.env`에서만 읽는다. 코드·출력·로그에 키를 남기지 않는다
- 과제 코드는 `submissions/{이름}/` 안에만 만든다. 다른 폴더는 수정하지 않는다
- 외부 API 호출에는 timeout과 예외 처리를 넣는다
- Agent 코드에는 최대 실행 횟수와 Trace 기록을 넣는다
- 완료 전에 `python -m pytest submissions/{이름}`이 통과해야 한다
