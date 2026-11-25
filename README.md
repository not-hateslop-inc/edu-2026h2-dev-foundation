# edu-2026h2-dev-foundation

2026 하반기 2회차 **개발환경 세팅과 AI 개발 기초** (EDU-2026-H2-02, 2026-09-10) 실습 저장소입니다.

환경: Python 3.12, Conda 환경 `hs-2026h2`

```bash
conda create -n hs-2026h2 python=3.12 -y
conda activate hs-2026h2
pip install -r requirements.txt
cp .env.example .env
python api_call.py
```

## 구성

| 경로 | 내용 |
| --- | --- |
| `api_call.py` | API 호출과 usage |
| `AGENTS.md` | AI 코딩 도구용 프로젝트 지침서 |
| `skills/new-assignment/` | 과제 폴더를 만드는 Skill |
| `exercise/REQUEST.md` | 실습 5: 지침 유무 비교에 쓰는 요청문 |
| `exercise/compare_sheet.md` | 비교표 |

## 과제

자기 업무의 반복 작업 하나를 `SKILL.md`로 만들고, AI 도구가 그 Skill로 만든 결과물과 함께 PR로 제출합니다. 기한 9/16(수) 23:59.
