# Manner

이 저장소에서 발행되는 모든 글에 적용되는 문체와 인용 규칙.

item 마다 있는 `manner.md` 는 이 문서를 **덮어쓰지 않고 더한다**. 둘 다 읽고,
충돌하는 곳에서는 item 이 이긴다. 다만 벗어날 때는 item 쪽에
`## 공통 manner 에서 벗어나는 점` 을 두고 이유를 적는다 — 벗어나는 것은
괜찮지만, 모르는 사이에 벗어나는 것은 아니다.

## Voice

1인칭을 쓰지 않는다. 이 저장소의 글은 대체로 의견이 아니라 설명이다.

단정할 수 있으면 단정한다. 대신 모르는 것은 모른다고 쓴다. "대략",
"알려져 있다" 같은 말로 얼버무리지 않는다 — 증명된 것과 수치해석으로만 아는
것과 추측은 서로 다른 것이고, 독자가 구별할 수 있어야 한다.

조건이 붙는 주장은 조건을 적는다. 특수한 경우의 결과를 일반적인 것처럼 쓰지
않는다.

## Formatting

- 제목은 h2 부터. h1 은 제목이 차지하므로 본문에서 쓰지 않는다.
- 한 쪽에 한 가지. 길어지면 쪽을 나눈다 — `docs` item 이라면 파일을 더하면
  된다.
- 한국어 글에서 영어 원어는 처음 나올 때만 괄호로 병기한다:
  결합 침투(bond percolation). 그 뒤로는 한국어만 쓴다.
- 수식은 KaTeX 숏코드로 쓴다.

      인라인  {{</* katex */>}}p_c{{</* /katex */>}}
      블록    {{</* katex display=true */>}} ... {{</* /katex */>}}

## Citations

reference 는 **제목으로 인용하고 url 을 링크로 건다.** 파일명은 쓰지 않는다 —
발행된 글의 독자에게 `20260812-en-wikipedia-org-….md` 는 아무 의미가 없다.

    ([Percolation threshold](https://en.wikipedia.org/w/index.php?oldid=1368848989))

열 수 없는 locator — `docs://` 같은 것 — 는 링크를 걸지 않는다.

### type 라벨

reference 의 `type` 은 라벨로 옮겨 붙인다. 무엇을 근거로 한 문장인지 독자가
알 수 있어야 한다.

| `type` | ko | en |
|---|---|---|
| `encyclopedia` | 링크만 | link only |
| `note` | 개인 노트 | personal note |
| `documentation` | 링크만 | link only |
| `article` | 링크만 | link only |
| `paper` | 링크만 | link only |

링크가 걸리는 것에는 라벨을 붙이지 않는다. 독자가 눌러서 직접 확인할 수 있기
때문이다. `note` 만 라벨을 갖는 이유도 같다 — 확인할 수 없으므로, 확인할 수
없다는 사실을 라벨이 대신 알린다.

**`docs` 소스에서 온 reference 는 `type` 이 언제나 `note` 다.** 개인 문서
서버의 비공개 노트이므로 예외가 없고, 따라서 `docs` 인용은 항상 라벨로만
나가고 링크가 걸리지 않는다.

    (개인 노트: how to make research about Percolation theory)

개인 노트를 본문에 인용하면 그 제목이 공개된다. 인용할지 말지는 매번
판단한다 — 기본값은 인용하지 않는 쪽이다(`sources/docs/usage.md`).
