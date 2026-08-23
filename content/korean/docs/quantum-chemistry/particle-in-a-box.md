---
title: 상자 속 입자
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 30
item: 2026-08-23-quantum-chemistry
---

[파동함수와 Schrödinger 방정식]({{< ref "wavefunction.md" >}})에서 방정식을
세우기는 했지만 아직 한 번도 풀어 보지는 않았습니다. 풀려면 퍼텐셜
{{< katex >}}V(x){{< /katex >}} 를 정해 주어야 하는데, 어떤 퍼텐셜부터
시작하는 것이 좋을까요.

가장 단순한 것부터 시작하는 편이 좋겠습니다. 그리고 그 단순한 퍼텐셜
하나만으로도 에너지가 왜 띄엄띄엄해지는지는 충분히 드러납니다.
(개인 노트: 3장 병진 운동: 상자 속 입자)

## 먼저 자유로운 입자

퍼텐셜이 아예 없는 경우부터 보겠습니다. 어디서나
{{< katex >}}V(x) = 0{{< /katex >}} 이면 방정식은 이렇게 됩니다.

{{< katex display=true >}}
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi
{{< /katex >}}

말로 옮기면 "두 번 미분하면 자기 자신의 상수배가 되는 함수를 찾아라" 입니다.
그런 함수라면 지수함수와 삼각함수가 익숙합니다. 복소수 형태로 쓰면

{{< katex display=true >}}
\psi(x) = e^{ikx} \quad \text{또는} \quad e^{-ikx}
{{< /katex >}}

이고, 실제로 넣어 보면

{{< katex display=true >}}
\frac{d^2}{dx^2}e^{ikx} = (ik)^2 e^{ikx} = -k^2 e^{ikx}
{{< /katex >}}

이므로 방정식은

{{< katex display=true >}}
-\frac{\hbar^2}{2m}\left(-k^2\right)\psi = E\psi
\qquad \Longrightarrow \qquad
E = \frac{\hbar^2k^2}{2m}
{{< /katex >}}

가 됩니다. 여기서 {{< katex >}}k{{< /katex >}} 가 무엇인지 짚어 두겠습니다.
{{< katex >}}e^{ikx}{{< /katex >}} 는 파장이
{{< katex >}}\lambda = 2\pi/k{{< /katex >}} 인 파동이므로,
{{< katex >}}k{{< /katex >}} 는 파수, 즉 단위 길이에 파동이 몇 번
들어가는지를 재는 양입니다. de Broglie 관계식
{{< katex >}}p = h/\lambda = \hbar k{{< /katex >}} 를 쓰면 위 식은
{{< katex >}}E = p^2/2m{{< /katex >}} 이 되어 고전역학의 운동에너지와 정확히
같아지는데, 새 이론이 옛 결과를 품고 있다는 것을 확인해 주는 대목입니다.

눈여겨볼 것은 그다음입니다. {{< katex >}}k{{< /katex >}} 에는 아무런 제약이
없어서, 어떤 실수를 넣어도 위 함수는 멀쩡한 파동함수가 되고, 따라서 에너지도
어떤 양수든 될 수 있습니다.

{{< katex display=true >}}
E \in [0, \infty) \quad \text{연속}
{{< /katex >}}

자유로운 입자는 양자화되지 않습니다. 이 점을 먼저 확인해 두는 것이
중요한데, 양자역학이라고 해서 무엇이든 저절로 띄엄띄엄해지는 것은 아니기
때문입니다. 양자화가 일어나려면 무언가가 더 있어야 합니다.

## 이제 가둬 보자

그 무언가가 무엇인지 보기 위해 입자를 좁은 영역에 가둬 보겠습니다.

폭이 {{< katex >}}L{{< /katex >}} 인 상자를 생각합니다. 안쪽
({{< katex >}}0 < x < L{{< /katex >}})에서는 퍼텐셜이 0 이고, 바깥에서는
무한대입니다.

{{< katex display=true >}}
V(x) = \begin{cases}
0 & 0 < x < L \\
\infty & \text{그 밖}
\end{cases}
{{< /katex >}}

무한대라는 말이 과격해 보이지만 뜻은 단순합니다. 바깥으로는 절대 나갈 수
없다는 것, 아무리 에너지가 커도 넘을 수 없는 벽이라는 뜻입니다. 물론 실제
세계에 이런 벽은 없습니다. 그렇지만 전자가 분자 안에 갇혀 있거나 반도체
우물에 갇혀 있는 상황은 이것으로 꽤 잘 근사되고, 무엇보다 정확히 풀립니다.

나갈 수 없으니 바깥에서 입자를 발견할 확률은 0 이고, 따라서 파동함수도
0 입니다. 여기에 [파동함수의 조건 3]({{< ref "wavefunction.md" >}}), 즉
파동함수는 연속이어야 한다는 조건을 더하면, 벽에 딱 붙은 자리에서도 이미
0 이어야 합니다.

{{< katex display=true >}}
\boxed{\;\psi(0) = 0, \qquad \psi(L) = 0\;}
{{< /katex >}}

이 두 줄이 경계조건입니다. 앞으로 벌어지는 일은 모두 여기서 나옵니다.

## 경계조건이 정수를 만든다

상자 안쪽에서는 퍼텐셜이 0 이므로 방정식이 자유입자와 똑같습니다. 그러니
해도 같은 꼴인데, 이번에는 지수함수보다 삼각함수 형태로 쓰는 편이 편합니다.
경계에서 0 이 되는 조건을 다루기 쉽기 때문입니다.

{{< katex display=true >}}
\psi(x) = A\sin kx + B\cos kx
{{< /katex >}}

첫 번째 조건부터 적용해 보겠습니다.
{{< katex >}}x = 0{{< /katex >}} 에서
{{< katex >}}\sin 0 = 0{{< /katex >}} 이고
{{< katex >}}\cos 0 = 1{{< /katex >}} 이므로

{{< katex display=true >}}
\psi(0) = A\cdot 0 + B\cdot 1 = B = 0
{{< /katex >}}

코사인 항이 통째로 사라지고, 남는 것은

{{< katex display=true >}}
\psi(x) = A\sin kx
{{< /katex >}}

입니다. 이제 두 번째 조건입니다.

{{< katex display=true >}}
\psi(L) = A\sin kL = 0
{{< /katex >}}

이 식이 성립하는 길은 {{< katex >}}A = 0{{< /katex >}} 이거나
{{< katex >}}\sin kL = 0{{< /katex >}} 이거나, 둘뿐입니다.

{{< katex >}}A = 0{{< /katex >}} 이면 파동함수가 어디서나 0 이고, 그러면
{{< katex >}}|\psi|^2 = 0{{< /katex >}} 이라 입자를 발견할 확률이 전 공간에서
0 이 됩니다. 입자가 없다는 뜻이므로 버리고 나면, 남는 것은

{{< katex display=true >}}
\sin kL = 0
{{< /katex >}}

이고, 사인이 0 이 되는 자리는 {{< katex >}}0, \pi, 2\pi, 3\pi, \dots{{< /katex >}}
로 띄엄띄엄합니다. 따라서

{{< katex display=true >}}
kL = n\pi \qquad (n = 1, 2, 3, \dots)
\qquad \Longrightarrow \qquad
\boxed{\;k = \frac{n\pi}{L}\;}
{{< /katex >}}

정수 {{< katex >}}n{{< /katex >}} 이 나왔습니다. 이것은 가정한 것이
아닙니다. Planck 처럼 "에너지가 덩어리져 있다고 하자"고 놓은 것이 아니라,
방정식을 풀고 경계조건을 적용했더니 사인 함수의 영점이 띄엄띄엄하다는
사실만으로 정수가 따라 나온 것입니다.

기타 줄을 생각하면 익숙한 일입니다. 양 끝이 고정된 줄에서는 아무 파장이나
울리지 않고 정해진 파장만 울리는데, 조건이 같으니 수학도 같습니다.

## 에너지 준위

{{< katex >}}k{{< /katex >}} 가 정해졌으니 에너지도 정해집니다.
자유입자에서 얻은 {{< katex >}}E = \hbar^2k^2/2m{{< /katex >}} 에 그대로
넣습니다.

{{< katex display=true >}}
E_n = \frac{\hbar^2}{2m}\left(\frac{n\pi}{L}\right)^2
= \frac{n^2\pi^2\hbar^2}{2mL^2}
{{< /katex >}}

{{< katex >}}\hbar = h/2\pi{{< /katex >}} 를 넣어 정리하면
{{< katex >}}\pi^2{{< /katex >}} 이 약분되면서 더 익숙한 꼴이 됩니다.

{{< katex display=true >}}
\frac{\pi^2\hbar^2}{2m} = \frac{\pi^2}{2m}\cdot\frac{h^2}{4\pi^2} = \frac{h^2}{8m}
{{< /katex >}}

{{< katex display=true >}}
\boxed{\;E_n = \frac{n^2h^2}{8mL^2}\;}
{{< /katex >}}

세 가지를 읽어 둘 만합니다.

에너지는 {{< katex >}}n^2{{< /katex >}} 으로 자랍니다. 준위 간격이 위로
갈수록 벌어진다는 뜻입니다.

{{< katex >}}L{{< /katex >}} 이 커지면 에너지가 내려가는데, 그것도
{{< katex >}}L^2{{< /katex >}} 에 반비례해서 빠르게 내려갑니다. 넓은
상자일수록 준위가 촘촘해지는 셈이고, 뒤에서 염료의 색을 설명할 때 이
의존성이 그대로 쓰입니다.

{{< katex >}}m{{< /katex >}} 이 커져도 에너지가 내려갑니다. 무거운
입자일수록 양자 효과가 작다는 뜻이고, 야구공에서 양자역학이 보이지 않는
이유도 같은 이야기입니다.

### de Broglie 로 다시 보기

같은 결과를 파동의 언어만으로도 얻을 수 있습니다. 양 끝이 고정된 정상파가
상자 안에 들어가려면 반파장의 정수배가 상자 길이와 같아야 합니다.

{{< katex display=true >}}
L = n\cdot\frac{\lambda}{2}
\qquad \Longrightarrow \qquad
\lambda = \frac{2L}{n}
{{< /katex >}}

de Broglie 관계식 {{< katex >}}p = h/\lambda{{< /katex >}} 를 쓰면

{{< katex display=true >}}
p = \frac{nh}{2L}
\qquad \Longrightarrow \qquad
E = \frac{p^2}{2m} = \frac{n^2h^2}{8mL^2}
{{< /katex >}}

같은 답입니다. 미분방정식을 푸는 길과 파장을 세는 길이 같은 곳에서 만난다는
것은, 양자화가 방정식의 기교가 아니라 파동이 갇혔다는 사실 자체에서 온다는
뜻입니다.

## 정규화와 확률밀도

{{< katex >}}A{{< /katex >}} 는 아직 정해지지 않았습니다. 확률의 합이 1
이라는 조건으로 정하는데, 계산은
[파동함수 문서]({{< ref "wavefunction.md" >}})에서 이미 해 두었고 결과는

{{< katex display=true >}}
\boxed{\;\psi_n(x) = \sqrt{\frac{2}{L}}\,\sin\frac{n\pi x}{L}\;}
\qquad
|\psi_n(x)|^2 = \frac{2}{L}\sin^2\frac{n\pi x}{L}
{{< /katex >}}

입니다.

**예.** {{< katex >}}n=1{{< /katex >}} 상태에서 입자가 왼쪽 4분의 1
({{< katex >}}0 \le x \le L/4{{< /katex >}})에 있을 확률을 구해 보겠습니다.
고전적으로 생각하면 상자 안을 고르게 돌아다닐 테니 25% 여야 합니다.

{{< katex display=true >}}
P = \frac{2}{L}\int_0^{L/4}\sin^2\frac{\pi x}{L}\,dx
= \frac{2}{L}\int_0^{L/4}\frac{1 - \cos(2\pi x/L)}{2}\,dx
{{< /katex >}}

{{< katex display=true >}}
= \frac{1}{L}\left[x - \frac{L}{2\pi}\sin\frac{2\pi x}{L}\right]_0^{L/4}
= \frac{1}{L}\left[\frac{L}{4} - \frac{L}{2\pi}\sin\frac{\pi}{2}\right]
{{< /katex >}}

{{< katex >}}\sin(\pi/2) = 1{{< /katex >}} 이므로

{{< katex display=true >}}
P = \frac{1}{4} - \frac{1}{2\pi} = 0.250 - 0.159 = 0.091
{{< /katex >}}

9.1% 로, 고전적 기대인 25% 보다 훨씬 작습니다. 바닥 상태의 파동함수는
가운데가 불룩하고 벽 근처에서 0 으로 잦아들기 때문에, 입자는 벽 쪽보다
가운데에 있을 확률이 훨씬 큽니다. 균일하게 퍼져 있다는 고전적 그림이 맞지
않는다는 것을 숫자가 보여 줍니다.

## 마디, 곡률, 그리고 에너지

{{< katex >}}\psi_n{{< /katex >}} 을 그려 보면 {{< katex >}}n{{< /katex >}} 이
커질수록 파동이 더 자주 출렁입니다. 벽을 제외하고 파동함수가 0 이 되는 지점을
**마디**(node)라 하는데, {{< katex >}}n{{< /katex >}} 번째 상태의 마디 수는

{{< katex display=true >}}
\text{내부 마디 수} = n - 1
{{< /katex >}}

입니다. 바닥 상태는 마디가 없고, 두 번째 상태는 가운데에 하나, 세 번째
상태는 둘을 갖습니다.

마디가 왜 에너지와 관계있는지는 방정식을 다시 보면 알 수 있습니다.
운동에너지 연산자는

{{< katex display=true >}}
\hat{T} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
{{< /katex >}}

로 2차 도함수, 즉 곡률입니다. 마디가 많다는 것은 같은 폭 안에서 파동이 더
급하게 휜다는 뜻이고, 곡률이 크다는 뜻이며, 그대로 운동에너지가 크다는
뜻입니다.

곡률이 곧 운동에너지라는 이 관계는 뒤에서도 계속 쓰입니다. 결합성 오비탈의
에너지가 낮은 이유도([분자 오비탈 이론]({{< ref "molecular-orbital.md" >}}))
결국 마디가 없다는 데 있습니다.

## 영점에너지: 왜 0 이 될 수 없는가

{{< katex >}}n{{< /katex >}} 이 1 부터 시작한다는 것은 최저 에너지가

{{< katex display=true >}}
E_1 = \frac{h^2}{8mL^2} \neq 0
{{< /katex >}}

이라는 뜻입니다. 이것을 **영점에너지**(zero-point energy)라 하며, 아무리
식혀도 남는 에너지입니다.

{{< katex >}}n = 0{{< /katex >}} 이 왜 안 되는지는 세 가지로 말할 수 있는데,
셋 다 결국 같은 이야기입니다.

**수학적으로.** {{< katex >}}n=0{{< /katex >}} 이면
{{< katex >}}k=0{{< /katex >}} 이고
{{< katex >}}\psi = A\sin 0 = 0{{< /katex >}} 입니다. 파동함수가 통째로 0
이면 정규화할 수 없고, 확률의 합이 1 이 아니라 0 이 되어 버립니다.

**파동으로.** {{< katex >}}n=0{{< /katex >}} 은 파장이 무한대라는 뜻인데,
길이 {{< katex >}}L{{< /katex >}} 인 상자 안에 무한히 긴 파동을 넣을 수는
없습니다.

**불확정성으로.** 입자를 폭 {{< katex >}}L{{< /katex >}} 안에 가뒀으므로
{{< katex >}}\Delta x \approx L{{< /katex >}} 이고, 따라서

{{< katex display=true >}}
\Delta p \gtrsim \frac{\hbar}{2L}
{{< /katex >}}

입니다. 운동량이 확실히 0 일 수 없으니 운동에너지도 0 일 수 없습니다.
실제로 이 {{< katex >}}\Delta p{{< /katex >}} 로 만든
{{< katex >}}(\Delta p)^2/2m{{< /katex >}} 은
{{< katex >}}E_1{{< /katex >}} 과 같은 자릿수입니다.

가둔다는 것 자체가 에너지를 요구하는 셈입니다. 상자에만 있는 이야기가 아니라
조화 진동자에서도, 원자 속 전자에서도 같은 일이 일어납니다.

## 준위 간격과 대응원리

이웃한 두 준위의 간격은

{{< katex display=true >}}
\Delta E = E_{n+1} - E_n
= \frac{h^2}{8mL^2}\left[(n+1)^2 - n^2\right]
= \frac{(2n+1)h^2}{8mL^2}
{{< /katex >}}

입니다. 간격 자체는 {{< katex >}}n{{< /katex >}} 이 커질수록 커집니다.
그런데 에너지 대비 상대적인 간격을 보면 이야기가 달라집니다.

{{< katex display=true >}}
\frac{\Delta E}{E_n} = \frac{2n+1}{n^2} \xrightarrow{\;n\to\infty\;} 0
{{< /katex >}}

큰 양자수에서는 준위가 상대적으로 촘촘해져 연속처럼 보입니다. 확률밀도도
마찬가지여서, {{< katex >}}n{{< /katex >}} 이 크면
{{< katex >}}\sin^2{{< /katex >}} 의 마루와 골이 너무 촘촘해지는 탓에 웬만한
분해능으로 보면 평평하고 균일한 분포로 보입니다. 고전역학이 말하던 "상자
안을 고르게 돌아다닌다"가 되돌아오는 셈입니다.

이것을 **대응원리**(correspondence principle)라 합니다. 양자역학은 고전역학을
부정하는 것이 아니라 포함하며, 고전역학이 맞던 영역에서는 고전역학으로
돌아갑니다.

## 2차원과 3차원, 그리고 겹침

상자를 넓혀도 논의는 자연스럽게 확장됩니다. 변수분리를 쓰면 각 방향이
독립적인 1차원 문제가 되므로, 2차원 직사각형 상자에서는

{{< katex display=true >}}
E_{n_x,n_y} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2}\right)
{{< /katex >}}

이고 3차원 직육면체에서는 항이 하나 더 붙습니다. 양자수도 방향마다 하나씩
생깁니다.

여기서 새로운 현상이 나타납니다. 정사각형 상자
({{< katex >}}L_x = L_y = L{{< /katex >}})를 생각해 보겠습니다.

{{< katex display=true >}}
E_{1,2} = \frac{h^2}{8mL^2}(1 + 4) = \frac{5h^2}{8mL^2}
{{< /katex >}}
{{< katex display=true >}}
E_{2,1} = \frac{h^2}{8mL^2}(4 + 1) = \frac{5h^2}{8mL^2}
{{< /katex >}}

두 상태의 에너지가 같습니다. 하나는 가로로 마디가 있고 다른 하나는 세로로
있어서 파동함수는 전혀 다른데도, 에너지는 그 차이를 구별하지 못합니다.
이렇게 서로 다른 상태가 같은 에너지를 갖는 것을 **겹침**(degeneracy)이라
합니다.

겹침은 우연이 아니라 대칭성의 결과입니다. 정사각형에서는 가로와 세로가
구별되지 않으므로 둘을 맞바꾼 상태의 에너지가 같을 수밖에 없습니다. 실제로
직사각형({{< katex >}}L_x \neq L_y{{< /katex >}})으로 만들면 대칭이 깨지면서
겹침도 풀립니다.

같은 논리가 원자에서도 반복됩니다.
[수소꼴 원자]({{< ref "hydrogen.md" >}})의 오비탈이 겹쳐 있는 것도 구대칭
때문이고, 자기장을 걸어 대칭을 깨면 겹침이 풀립니다.

## 실제로 쓰이는 곳: 염료의 색

지금까지의 이야기가 추상적으로 들린다면, 이 모형이 실제로 색을 예측하는 데
쓰이는 모습을 보는 것이 도움이 됩니다.

공액(conjugated) 분자에서는 {{< katex >}}\pi{{< /katex >}} 전자가 특정 결합
하나에 묶여 있지 않고 사슬 전체에 퍼져 있습니다. 사슬 안에서는 퍼텐셜이
대체로 평평하고 양 끝에서 급격히 올라가므로, 이 전자들을 길이
{{< katex >}}L{{< /katex >}} 인 1차원 상자 속 입자로 근사할 수 있습니다.
자유전자 모형(free-electron model)이라 부릅니다.

전자가 모두 {{< katex >}}N{{< /katex >}} 개라고 하겠습니다. Pauli 원리에
의해 한 준위에 둘씩 들어가므로 아래에서부터 {{< katex >}}N/2{{< /katex >}}
개의 준위가 찹니다. 가장 높은 찬 준위(HOMO)가
{{< katex >}}n = N/2{{< /katex >}}, 가장 낮은 빈 준위(LUMO)가
{{< katex >}}n = N/2 + 1{{< /katex >}} 입니다. 빛을 흡수한다는 것은 전자가
HOMO 에서 LUMO 로 올라가는 일이므로

{{< katex display=true >}}
\Delta E = \frac{h^2}{8mL^2}\left[\left(\tfrac{N}{2}+1\right)^2 - \left(\tfrac{N}{2}\right)^2\right]
= \frac{(N+1)h^2}{8mL^2}
{{< /katex >}}

예를 들어 {{< katex >}}n = 6 \to 7{{< /katex >}} 전이라면

{{< katex display=true >}}
\Delta E = \frac{(49-36)h^2}{8mL^2} = \frac{13h^2}{8mL^2}
{{< /katex >}}

이고, {{< katex >}}\Delta E = hc/\lambda{{< /katex >}} 이므로

{{< katex display=true >}}
\boxed{\;\lambda = \frac{8mL^2c}{13h}\;}
{{< /katex >}}

흡수 파장이 {{< katex >}}L^2{{< /katex >}} 에 비례합니다. 사슬이 길어지면
흡수가 긴 파장 쪽, 즉 붉은 쪽으로 이동한다는 뜻입니다. 실제로 시아닌 염료
계열에서 공액 사슬을 한 단위씩 늘리면 색이 노랑에서 빨강, 파랑으로
옮겨가는데, 이 모형은 그 경향을 정성적으로 맞히고 자릿수도 맞힙니다.

물론 근사입니다. 전자–전자 반발을 무시했고, 사슬 안 퍼텐셜이 완전히
평평하지도 않으며, 끝을 어디로 잡을지도 애매합니다. 그래서 파장을 정확히
맞히지는 못합니다. 그런데도 색이 왜 그 방향으로 변하는지를 설명하는 데는
충분합니다.

같은 논리가 반도체 양자우물과 양자점에도 그대로 적용됩니다. 양자점의 색이
크기에 따라 달라지는 것은 상자의 {{< katex >}}L{{< /katex >}} 을 바꾸는 것과
같아서, 작은 점은 준위 간격이 크므로 파란빛을, 큰 점은 붉은빛을 냅니다.

## 숫자로 확인하기

**1.0 nm 상자 속 전자의 바닥 상태.**

{{< katex display=true >}}
E_1 = \frac{h^2}{8mL^2}
= \frac{(6.626\times10^{-34})^2}{8(9.109\times10^{-31})(1.0\times10^{-9})^2}
{{< /katex >}}

분자는 {{< katex >}}4.39\times10^{-67}{{< /katex >}}, 분모는
{{< katex >}}7.29\times10^{-48}{{< /katex >}} 이므로

{{< katex display=true >}}
E_1 = 6.02\times10^{-20}\ \mathrm{J} = 0.376\ \mathrm{eV}
{{< /katex >}}

첫 전이는 {{< katex >}}E_2 - E_1 = 3E_1 = 1.13\ \mathrm{eV}{{< /katex >}} 로
파장 약 1100 nm, 근적외선입니다.

**같은 상자 속 야구공.** 질량만 {{< katex >}}0.145\ \mathrm{kg}{{< /katex >}}
으로 바꾸면 {{< katex >}}E_1{{< /katex >}} 은
{{< katex >}}9.1\times10^{-31}/0.145 \approx 6\times10^{-30}{{< /katex >}} 배,
즉 {{< katex >}}10^{-49}\ \mathrm{J}{{< /katex >}} 정도가 됩니다. 준위
간격이 어떤 측정으로도 잡히지 않는 크기입니다. 같은 식이 전자에서는 화학을
지배하고 야구공에서는 아무 의미가 없습니다.

**염료의 색.** {{< katex >}}L = 1.5\ \mathrm{nm}{{< /katex >}} 인 공액 사슬에서
{{< katex >}}n = 6 \to 7{{< /katex >}} 전이를 보면

{{< katex display=true >}}
\lambda = \frac{8(9.109\times10^{-31})(1.5\times10^{-9})^2(2.998\times10^{8})}{13(6.626\times10^{-34})}
= 5.7\times10^{-7}\ \mathrm{m} = 570\ \mathrm{nm}
{{< /katex >}}

초록빛을 흡수하고, 초록을 흡수하면 눈에는 그 보색인 자홍색으로 보입니다.
전자를 상자에 넣었을 뿐인데 염료의 색까지 나온 것입니다.

가장 단순한 퍼텐셜 하나에서 양자화와 영점에너지, 겹침과 대응원리, 그리고
염료의 색까지 나왔습니다. 다음에는 벽 대신 용수철을 놓아 조금 더 현실적인
퍼텐셜을 다루는 [조화 진동자]({{< ref "oscillator.md" >}})로
넘어가겠습니다.
