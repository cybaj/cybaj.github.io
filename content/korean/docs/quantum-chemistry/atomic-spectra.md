---
title: 원자 스펙트럼
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 80
item: 2026-08-23-quantum-chemistry
---

[다전자 원자]({{< ref "many-electron.md" >}})에서 에너지 준위의 구조를
세웠습니다. 그런데 그 준위들을 직접 본 사람은 아무도 없습니다. 실제로 보이는
것은 원자가 내놓거나 삼키는 빛뿐입니다.

구조는 그 빛에서 읽어내야 합니다. 그리고 모든 준위 쌍이 선을 만들지는
않습니다.
(개인 노트: 8장 원자 스펙트럼)

## 전이와 진동수 조건

원자가 에너지 {{< katex >}}E_2{{< /katex >}} 상태에서
{{< katex >}}E_1{{< /katex >}} 상태로 떨어지면서 광자 하나를 내놓습니다.
에너지 보존에서

{{< katex display=true >}}
\boxed{\;h\nu = |E_2 - E_1| = |\Delta E|\;}
{{< /katex >}}

이고, 분광학에서 즐겨 쓰는 파수로는

{{< katex display=true >}}
|\Delta E| = \frac{hc}{\lambda} = hc\,\tilde{\nu}
{{< /katex >}}

입니다. 스펙트럼선 하나가 준위 차이 하나에 대응하므로, 선의 위치를 재면 원자
내부의 에너지 구조를 알 수 있습니다. 선스펙트럼은 원자의 지문인 셈입니다.

여기까지는 [양자 가설]({{< ref "origins.md" >}})에서 이미 본 이야기입니다.
새로운 질문은 이것입니다. 원자에 준위가 수없이 많다면 그 모든 쌍 사이에서 선이
나와야 하지 않을까요.

그렇지는 않습니다. 실제 스펙트럼에는 있어야 할 선의 상당수가 빠져 있고, 그
사실이 오히려 원자에 대해 더 많은 것을 알려 줍니다.

## 세기를 정하는 것: 전이 쌍극자 모멘트

빛과 원자가 어떻게 상호작용하는지 생각해 보면 답이 나옵니다. 빛은 진동하는
전기장이고, 전기장은 전하 분포를 흔듭니다. 원자가 빛을 흡수하려면 전이 과정에서
전하 분포가, 정확히는 전기 쌍극자 모멘트가 진동해야 합니다.

이것을 정량화한 것이 전이 쌍극자 모멘트입니다.

{{< katex display=true >}}
\boxed{\;\boldsymbol{\mu}_{fi} = \int \psi_f^*\,\hat{\boldsymbol{\mu}}\,\psi_i\,d\tau\;}
{{< /katex >}}

{{< katex >}}\psi_i{{< /katex >}} 는 처음 상태,
{{< katex >}}\psi_f{{< /katex >}} 는 나중 상태,
{{< katex >}}\hat{\boldsymbol{\mu}} = -e\mathbf{r}{{< /katex >}} 는 쌍극자
연산자입니다. 전이의 세기는 이 값의 제곱에 비례합니다.

{{< katex display=true >}}
\boldsymbol{\mu}_{fi} \neq 0 \Rightarrow \text{허용 전이(allowed)}
{{< /katex >}}
{{< katex display=true >}}
\boldsymbol{\mu}_{fi} = 0 \Rightarrow \text{금지 전이(forbidden)}
{{< /katex >}}

적분이 0 이 되는 것은 우연이 아니라 대칭성 때문입니다. 그리고 대칭성
때문이라면 계산하지 않고도 미리 알 수 있습니다.

### 대칭성으로 적분이 죽는 방식

가장 단순한 예로 감을 잡아 보겠습니다. 1차원에서 홀함수를 대칭 구간에서
적분하면 정확히 0 입니다.

{{< katex display=true >}}
\int_{-a}^{a} x\,dx = 0
{{< /katex >}}

왼쪽과 오른쪽이 정확히 상쇄되기 때문입니다. 전이 쌍극자 적분에서도 같은 일이
일어납니다. {{< katex >}}\hat{\boldsymbol{\mu}} \propto \mathbf{r}{{< /katex >}}
는 홀함수(반전에 대해 부호가 바뀜)이므로, 처음과 나중 상태의 반전 대칭성이
같으면 전체 피적분 함수가 홀함수가 되어 적분이 0 이 됩니다.

전이가 일어나려면 처음과 나중 상태의 패리티가 달라야 한다는 뜻입니다.

## 선택 규칙

이 논증을 각운동량까지 포함해 끝까지 밀고 가면 **선택 규칙**(selection
rule)이 나옵니다.

{{< katex display=true >}}
\boxed{\;\Delta l = \pm 1, \qquad \Delta m_l = 0, \pm 1, \qquad \Delta S = 0\;}
{{< /katex >}}

각각의 뜻을 보겠습니다.

{{< katex >}}\Delta l = \pm 1{{< /katex >}} 은 각운동량 보존입니다. 광자는
스핀 1 을 가진 입자이고 각운동량 {{< katex >}}\hbar{{< /katex >}} 를 하나
나르므로, 원자가 광자를 하나 내놓으면 원자의 각운동량이 정확히 그만큼 바뀌어야
합니다. 그래서 {{< katex >}}\Delta l = 0{{< /katex >}} 은 안 됩니다. 광자가
가져간 각운동량을 아무도 내주지 않은 셈이 되기 때문입니다.
{{< katex >}}\Delta l = \pm2{{< /katex >}} 도 광자 하나가 나를 수 있는 양을
넘으므로 안 됩니다.

{{< katex >}}\Delta m_l = 0, \pm1{{< /katex >}} 은 그 각운동량의 방향
성분으로, 광자가 어느 쪽으로 편광되어 있느냐에 대응합니다.

{{< katex >}}\Delta S = 0{{< /katex >}} 은 스핀이 바뀌지 않는다는 뜻입니다.
쌍극자 연산자 {{< katex >}}-e\mathbf{r}{{< /katex >}} 에는 스핀이 들어 있지
않아 스핀 좌표에 대해서는 아무 일도 하지 않으므로, 스핀 상태가 다르면 그 부분의
적분이 직교성에 의해 0 이 됩니다.

선택 규칙은 금지 목록이 아니라 보존 법칙의 다른 표현입니다. 무엇이 금지되는지
외우는 것보다 왜 금지되는지 아는 편이 훨씬 쓸모 있습니다.

한 가지 덧붙이면 "금지" 가 절대적이지는 않습니다. 쌍극자 근사를
넘어서면(사중극자 전이, 스핀–궤도 혼합) 아주 약하게 일어날 수 있습니다. 금지
전이는 일어나지 않는 것이 아니라 아주 느리게 일어나며, 이것이 곧 인광을
설명합니다.

## 단일항과 삼중항

전자가 둘 있는 계에서는 스핀을 합치는 방법이 두 가지입니다.

두 스핀이 반대로 짝지으면 총 스핀이 0 입니다.

{{< katex display=true >}}
S = 0, \qquad 2S+1 = 1 \qquad \textbf{단일항 singlet}
{{< /katex >}}

나란하면 1 입니다.

{{< katex display=true >}}
S = 1, \qquad 2S+1 = 3 \qquad \textbf{삼중항 triplet}
{{< /katex >}}

{{< katex >}}2S+1{{< /katex >}} 을 스핀 다중도라 하며, 삼중항이 셋인 것은
{{< katex >}}m_S = -1, 0, +1{{< /katex >}} 세 상태가 있기 때문입니다.

스핀 함수를 명시적으로 쓰면 왜 그런지 보입니다. 반대칭인 조합은 하나뿐이고

{{< katex display=true >}}
\sigma_-(1,2) = \frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) - \beta(1)\alpha(2)\right]
{{< /katex >}}

대칭인 조합은 셋입니다.

{{< katex display=true >}}
\alpha(1)\alpha(2), \qquad
\frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) + \beta(1)\alpha(2)\right], \qquad
\beta(1)\beta(2)
{{< /katex >}}

### 삼중항이 더 안정한 이유

같은 전자배치라도 삼중항이 단일항보다 에너지가 낮습니다.

{{< katex display=true >}}
E_{\text{triplet}} < E_{\text{singlet}}
{{< /katex >}}

이유는 [Hund 규칙]({{< ref "many-electron.md" >}})과 완전히 같습니다. 전체
파동함수가 반대칭이어야 하므로, 스핀 부분이 대칭인 삼중항은 공간 부분이
반대칭이어야 합니다. 반대칭 공간 함수는 두 전자가 같은 자리에 있을 때 0 이
되므로 전자들이 서로를 피하게 되고, 그만큼 반발이 줄어듭니다.

여기서도 자기적인 힘이 아니라 대칭성이 에너지를 낮춘 것입니다.

## 헬륨이 보여 주는 것

헬륨 스펙트럼이 이 규칙들의 좋은 시험대입니다. 헬륨의 들뜬 상태는 단일항
계열과 삼중항 계열로 뚜렷이 갈라져 있는데, 두 계열 사이의 전이선이 거의 보이지
않습니다.

{{< katex >}}\Delta S = 0{{< /katex >}} 규칙이 그것을 금지하기 때문입니다.
한때는 이 현상 때문에 헬륨이 두 종류의 기체(파라헬륨, 오르토헬륨)라고
생각되기도 했습니다. 실제로는 하나의 원소이고, 스핀 선택 규칙이 두 계열을
갈라놓고 있었을 뿐입니다.

금지 규칙이 스펙트럼에서 선을 지운 결과가 새로운 원소처럼 보인 것입니다. 없는
선이 있는 선만큼이나 많은 것을 말해 준다는 좋은 예입니다.

## 스핀–궤도 상호작용과 미세구조

마지막으로 준위가 한 번 더 갈라지는 이야기입니다.

전자는 스핀 때문에 작은 자석처럼 행동합니다. 그리고 핵 주위를 도는 전자의
입장에서 보면 핵이 자기 주위를 도는 것처럼 보이는데, 도는 전하는 자기장을
만듭니다. 그러니 전자의 스핀 자석이 자기 궤도 운동이 만든 자기장 속에 놓이게
됩니다.

이 상호작용을 **스핀–궤도 결합**(spin–orbit coupling)이라 합니다. 에너지는 두
자기 모멘트의 상대적 방향에 의존하므로, 스핀이 궤도 각운동량과 나란한지
반대인지에 따라 에너지가 갈라집니다.

그러면 {{< katex >}}\mathbf{l}{{< /katex >}} 과
{{< katex >}}\mathbf{s}{{< /katex >}} 가 각각 따로 보존되지 않고, 보존되는
것은 그 합입니다.

{{< katex display=true >}}
\boxed{\;\mathbf{j} = \mathbf{l} + \mathbf{s},
\qquad j = l + \tfrac12 \ \text{또는}\ \left|l - \tfrac12\right|\;}
{{< /katex >}}

예를 들어 {{< katex >}}p{{< /katex >}} 전자({{< katex >}}l=1{{< /katex >}})는
{{< katex >}}j = 3/2{{< /katex >}} 와 {{< katex >}}j = 1/2{{< /katex >}} 두
상태로 갈라집니다. 이 갈라짐이 **미세구조**(fine structure)입니다.

상태를 요약해 적는 표기는 **항 기호**(term symbol)입니다.

{{< katex display=true >}}
{}^{2S+1}L_J
{{< /katex >}}

{{< katex >}}L{{< /katex >}} 은 총 궤도 각운동량으로
{{< katex >}}0,1,2,3{{< /katex >}} 에 각각
{{< katex >}}S, P, D, F{{< /katex >}} 를 씁니다. 나트륨의 바닥 상태는
{{< katex >}}{}^2S_{1/2}{{< /katex >}} 이고, 첫 들뜬 상태는
{{< katex >}}{}^2P_{1/2}{{< /katex >}} 와
{{< katex >}}{}^2P_{3/2}{{< /katex >}} 둘입니다.

스핀–궤도 결합의 세기는 대략 {{< katex >}}Z^4{{< /katex >}} 에 비례합니다.
전자가 핵 가까이 갈수록 느끼는 자기장이 세지기 때문입니다. 그래서 가벼운
원자에서는 미세구조가 아주 작고 무거운 원자에서는 큽니다. 수소에서는 겨우
보이는 정도이지만 무거운 원소에서는 준위 구조 자체를 바꿔 놓습니다.

## 숫자로 확인하기

**나트륨 D선.** 가로등의 주황색 빛입니다. 자세히 보면 하나가 아니라 두
개입니다.

{{< katex display=true >}}
\lambda_1 = 589.0\ \mathrm{nm} \quad ({}^2P_{3/2} \to {}^2S_{1/2})
{{< /katex >}}
{{< katex display=true >}}
\lambda_2 = 589.6\ \mathrm{nm} \quad ({}^2P_{1/2} \to {}^2S_{1/2})
{{< /katex >}}

전이 자체의 에너지는

{{< katex display=true >}}
\Delta E = \frac{hc}{\lambda} = \frac{(6.626\times10^{-34})(2.998\times10^{8})}{589.3\times10^{-9}}
= 3.37\times10^{-19}\ \mathrm{J} = 2.10\ \mathrm{eV}
{{< /katex >}}

갈라짐은 파수로 재는 편이 편합니다.

{{< katex display=true >}}
\Delta\tilde{\nu} = \frac{1}{589.0\times10^{-7}\,\mathrm{cm}} - \frac{1}{589.6\times10^{-7}\,\mathrm{cm}}
= 17.3\ \mathrm{cm^{-1}}
{{< /katex >}}

에너지로 바꾸면

{{< katex display=true >}}
\Delta E_{\text{fs}} = hc\,\Delta\tilde{\nu}
= (6.626\times10^{-34})(2.998\times10^{10})(17.3)
= 3.44\times10^{-22}\ \mathrm{J} = 2.1\times10^{-3}\ \mathrm{eV}
{{< /katex >}}

**비율로 보면**

{{< katex display=true >}}
\frac{\Delta E_{\text{fs}}}{\Delta E} = \frac{2.1\times10^{-3}}{2.10} = 1.0\times10^{-3}
{{< /katex >}}

천분의 일이라 미세구조라 부릅니다. 그런데도 값싼 분광기로 두 선이 갈라져
보일 만큼은 됩니다. 그리고 이 작은 숫자가 전자에 스핀이 있다는 증거입니다.
스핀이 없었다면 D선은 하나였을 것입니다.

**왜 3p → 3s 는 되고 3s → 3s 는 안 되는가.** 나트륨의 바닥 상태는
{{< katex >}}3s{{< /katex >}}({{< katex >}}l=0{{< /katex >}})이고 첫 들뜬
상태는 {{< katex >}}3p{{< /katex >}}({{< katex >}}l=1{{< /katex >}})
입니다.

{{< katex display=true >}}
\Delta l = 1 - 0 = +1 \quad \checkmark
{{< /katex >}}

허용됩니다. 반면 {{< katex >}}4s \to 3s{{< /katex >}} 는
{{< katex >}}\Delta l = 0{{< /katex >}} 이라 금지되고, 실제로 그 전이의 선은
스펙트럼에서 보이지 않습니다. 에너지 차이는 분명히 존재하는데 선이 없는
것이니, 선택 규칙이 실재한다는 직접적인 증거입니다.

**인광은 왜 느린가.** 유기 분자의 삼중항 들뜬 상태에서 단일항 바닥 상태로
가는 전이는 {{< katex >}}\Delta S = 0{{< /katex >}} 을 어깁니다.
형광(단일항 → 단일항)의 수명이 나노초 정도인 데 비해, 인광은 밀리초에서 초
단위입니다.

{{< katex display=true >}}
\frac{\tau_{\text{인광}}}{\tau_{\text{형광}}} \sim \frac{10^{0}\,\mathrm{s}}{10^{-9}\,\mathrm{s}} = 10^{9}
{{< /katex >}}

십억 배 느립니다. 금지 전이가 정말로 일어나기는 하되 얼마나 억눌리는지를
보여 주는 숫자입니다. 야광 스티커가 불을 끈 뒤에도 한참 빛나는 것이 이
{{< katex >}}\Delta S = 0{{< /katex >}} 규칙 덕분입니다.

원자에 관한 이야기는 여기까지입니다. 이제 원자를 붙여 분자를 만들 차례이고,
[Born–Oppenheimer 근사]({{< ref "born-oppenheimer.md" >}})에서 시작하겠습니다.
