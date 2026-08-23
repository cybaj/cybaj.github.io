---
title: 파동함수와 Schrödinger 방정식
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 20
item: 2026-08-23-quantum-chemistry
---

[양자 가설]({{< ref "origins.md" >}})은 고전물리학이 무너진 자리를 보여 주었을
뿐, 그 자리에 무엇을 놓아야 하는지는 말해 주지 않았습니다. 실험이 요구한
것은 분명했습니다. 에너지가 띄엄띄엄하다는 것과 물질이 파동이라는 것을 함께
담는 기술입니다.
(개인 노트: 2장 파동함수와 Schrödinger 방정식)

## 궤적을 버려야 하는 이유

고전역학에서 입자의 상태는 두 개의 양으로 완전히 정해집니다. 지금 어디
있는가({{< katex >}}x{{< /katex >}}), 그리고 어떻게 움직이는가
({{< katex >}}p{{< /katex >}}). 이 둘을 알면 운동 방정식이 나머지를 전부
결정합니다. 내일의 위치도, 100 년 뒤의 위치도 마찬가지입니다.

그런데 불확정성 원리가 그 두 양을 동시에 지정하는 것을 금지합니다. 그렇다면
고전적 의미의 상태라는 것이 아예 존재하지 않으니, 다른 것으로 상태를 기술해야
합니다.

양자역학이 택한 것은 **파동함수**(wavefunction)
{{< katex >}}\psi{{< /katex >}} 입니다. 공간의 각 점마다 하나의 값을 갖는
함수이고, 그 값은 일반적으로 복소수입니다. 이 함수 하나가 계에 관해 알 수 있는
전부를 담습니다.

무엇을 얻는 대신 무엇을 잃었는지 분명히 해 두는 것이 좋겠습니다.

**잃은 것.** "이 순간 여기 있다" 는 말입니다. 파동함수는 위치를 하나로
지정하지 않습니다.

**얻은 것.** 파동함수는 모든 위치에 대해 동시에 무언가를 말해 줍니다. 그리고
파동이므로 겹칠 수 있고, 겹치면 간섭합니다. 전자가 이중 슬릿에서 무늬를 만드는
것이 이 때문이며, 궤적으로는 끝내 설명되지 않던 현상입니다.

궤적을 포기한 것이 손해만은 아니라는 뜻입니다.

## Schrödinger 방정식

파동함수를 구하려면 방정식이 있어야 합니다. 시간에 무관한 형태는 이렇게
생겼습니다.

{{< katex display=true >}}
\boxed{\;\hat{H}\psi = E\psi\;}
{{< /katex >}}

{{< katex >}}\hat{H}{{< /katex >}} 는 Hamiltonian 연산자로 계의 총에너지에
대응하고, {{< katex >}}E{{< /katex >}} 는 에너지 값,
{{< katex >}}\psi{{< /katex >}} 는 찾고자 하는 파동함수입니다.

이 방정식은 유도된 것이 아닙니다. 뉴턴의 제2법칙이 유도된 것이 아닌 것과
같습니다. 가정해 놓고 결과가 실험과 맞는지 확인하는 종류의 식입니다. 다만 그
형태가 어떻게 정해졌는지는 따라갈 수 있습니다.

### Hamiltonian 은 어떻게 만들어지는가

고전역학에서 총에너지는 운동에너지와 퍼텐셜에너지의 합입니다.

{{< katex display=true >}}
E = \frac{p^2}{2m} + V(x)
{{< /katex >}}

양자역학은 여기서 물리량을 연산자로 바꿉니다. 연산자란 함수에 작용해 다른
함수를 내놓는 것이고, 여기서 필요한 것은 둘입니다.

{{< katex display=true >}}
\hat{x} = x, \qquad
\hat{p} = -i\hbar\frac{d}{dx}
{{< /katex >}}

위치는 그냥 곱하는 연산이고, 운동량은 미분입니다.

**왜 하필 미분인가?** 임의로 고른 것이 아닙니다. 확인해 보겠습니다.
de Broglie 파 {{< katex >}}\psi = e^{ikx}{{< /katex >}} 에 이 연산자를
작용시키면

{{< katex display=true >}}
\hat{p}\,e^{ikx} = -i\hbar\frac{d}{dx}e^{ikx}
= -i\hbar\,(ik)\,e^{ikx} = \hbar k\, e^{ikx}
{{< /katex >}}

{{< katex >}}-i \times i = 1{{< /katex >}} 이므로 부호가 맞아떨어집니다.
나온 값이 {{< katex >}}\hbar k{{< /katex >}} 이고,
{{< katex >}}k = 2\pi/\lambda{{< /katex >}} 이므로

{{< katex display=true >}}
\hbar k = \frac{h}{2\pi}\cdot\frac{2\pi}{\lambda} = \frac{h}{\lambda}
{{< /katex >}}

정확히 de Broglie 관계식입니다. 운동량 연산자의 저 모양은
[양자 가설]({{< ref "origins.md" >}})의 실험 결과가 저절로 나오도록 역으로
정해진 것입니다. 연산자는 하늘에서 떨어진 것이 아니라 실험을 담도록
만들어졌습니다.

이제 {{< katex >}}p^2{{< /katex >}} 을 바꿉니다. 연산자를 두 번 적용하면

{{< katex display=true >}}
\hat{p}^2 = \left(-i\hbar\frac{d}{dx}\right)\left(-i\hbar\frac{d}{dx}\right)
= (-i)^2\hbar^2\frac{d^2}{dx^2} = -\hbar^2\frac{d^2}{dx^2}
{{< /katex >}}

{{< katex >}}(-i)^2 = -1{{< /katex >}} 이라 음부호가 남습니다. 따라서

{{< katex display=true >}}
\boxed{\;\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)\;}
{{< /katex >}}

이고 방정식 전체는

{{< katex display=true >}}
\boxed{\;-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi\;}
{{< /katex >}}

가 됩니다.

이 식이 앞으로 하는 일의 전부입니다. 퍼텐셜
{{< katex >}}V(x){{< /katex >}} 를 하나 정해 주면 허용되는
{{< katex >}}\psi{{< /katex >}} 와 {{< katex >}}E{{< /katex >}} 가 나옵니다.
[상자 속 입자]({{< ref "particle-in-a-box.md" >}})부터
[분자 오비탈 이론]({{< ref "molecular-orbital.md" >}})까지 남은 내용은 모두
이 방정식에 서로 다른 {{< katex >}}V(x){{< /katex >}} 를 넣는 일입니다.

## 왜 "고유값 문제" 인가

{{< katex >}}\hat{H}\psi = E\psi{{< /katex >}} 를 다시 보면 보통의
미분방정식과 성격이 다릅니다.

보통은 "이 방정식을 만족하는 함수를 찾아라" 입니다. 그런데 이 식은 연산자를
작용시킨 결과가 원래 함수의 상수배가 되기를 요구합니다. 모양은 그대로여야 하고
크기만 바뀔 수 있다는 뜻입니다.

이런 방정식을 **고유값 문제**(eigenvalue problem)라 하고,
{{< katex >}}\psi{{< /katex >}} 를 고유함수,
{{< katex >}}E{{< /katex >}} 를 고윳값이라 합니다.

아무 {{< katex >}}E{{< /katex >}} 를 넣어도 미분방정식 자체는 해를 가지므로
수학적으로는 문제가 없습니다. 그런데 그 해가 아래에서 볼 물리적 조건들까지
만족하는 것은 특정한 {{< katex >}}E{{< /katex >}} 에서뿐입니다.

에너지가 띄엄띄엄해지는 이유는 방정식이 아니라 조건에 있다는 뜻입니다. 이
점을 붙잡아 두면 뒤에 이어지는 세 문제가 모두 같은 이야기로 읽힙니다.

## Born 해석: 파동함수는 무엇인가

방정식은 세웠지만 {{< katex >}}\psi{{< /katex >}} 가 대체 무엇인지는 아직
말하지 않았습니다. 복소수 값을 갖는 함수이니 그 자체로는 측정되지 않습니다.

Born 이 준 답은 다음과 같습니다.

{{< katex display=true >}}
\boxed{\;|\psi(x)|^2\,dx = x \text{ 와 } x+dx \text{ 사이에서 입자를 발견할 확률}\;}
{{< /katex >}}

{{< katex >}}|\psi|^2{{< /katex >}} 이 확률밀도입니다. 파동함수 자체가
아니라 그 절댓값의 제곱이 물리적 의미를 갖습니다.

이 해석에서 세 가지가 따라 나옵니다.

확률밀도는 항상 실수이고 음이 아닙니다.
{{< katex >}}|\psi|^2 = \psi^*\psi \ge 0{{< /katex >}} 이므로 자동으로
보장되며, 복소수 파동함수를 써도 관측량은 실수로 나옵니다.

파동함수의 부호는 그 자체로 관측되지 않습니다.
{{< katex >}}\psi{{< /katex >}} 와 {{< katex >}}-\psi{{< /katex >}} 는 같은
확률밀도를 줍니다.

그런데 파동함수를 더할 때는 부호가 결과를 바꿉니다. 이것이 세 번째입니다.

{{< katex display=true >}}
|\psi_1 + \psi_2|^2 \neq |\psi_1|^2 + |\psi_2|^2
{{< /katex >}}

두 파동함수를 겹치면 교차항이 생기고, 그 항의 부호에 따라 확률이 커지기도
작아지기도 합니다. 이것이 간섭입니다.
[분자 오비탈 이론]({{< ref "molecular-orbital.md" >}})에서 결합성과 반결합성
오비탈이 갈리는 것도 정확히 이 부호 하나 때문입니다.

## 정규화

입자가 어딘가에는 있어야 하므로, 전 공간에 대한 확률의 합은 1 이어야
합니다.

{{< katex display=true >}}
\int_{-\infty}^{\infty} |\psi(x)|^2\,dx = 1
{{< /katex >}}

이것을 **정규화**(normalisation)라 합니다. 그런데 방정식을 풀어서 나온 해가
이 조건을 자동으로 만족하지는 않습니다. 다행히 Schrödinger 방정식은 선형이라
{{< katex >}}\psi{{< /katex >}} 가 해이면 상수배
{{< katex >}}N\psi{{< /katex >}} 도 해이므로,
{{< katex >}}N{{< /katex >}} 을 이 조건으로 정하면 됩니다.

**직접 해 보겠습니다.** 구간
{{< katex >}}0 \le x \le L{{< /katex >}} 에서
{{< katex >}}\psi(x) = N\sin(\pi x/L){{< /katex >}} 을 정규화합니다. 조건은

{{< katex display=true >}}
N^2\int_0^L \sin^2\!\left(\frac{\pi x}{L}\right)dx = 1
{{< /katex >}}

{{< katex >}}\sin^2{{< /katex >}} 을 그대로 적분하기는 번거로우므로 배각
공식 {{< katex >}}\sin^2\theta = \tfrac12(1-\cos 2\theta){{< /katex >}} 를
씁니다.

{{< katex display=true >}}
\int_0^L \sin^2\!\left(\frac{\pi x}{L}\right)dx
= \frac{1}{2}\int_0^L\left[1 - \cos\frac{2\pi x}{L}\right]dx
{{< /katex >}}

{{< katex display=true >}}
= \frac{1}{2}\left[x - \frac{L}{2\pi}\sin\frac{2\pi x}{L}\right]_0^L
{{< /katex >}}

{{< katex >}}x=L{{< /katex >}} 에서
{{< katex >}}\sin 2\pi = 0{{< /katex >}} 이고
{{< katex >}}x=0{{< /katex >}} 에서도 0 이므로 둘째 항이 통째로 사라집니다.
남는 것은

{{< katex display=true >}}
\frac{1}{2}\left[L - 0\right] = \frac{L}{2}
{{< /katex >}}

따라서

{{< katex display=true >}}
N^2\cdot\frac{L}{2} = 1
\qquad \Longrightarrow \qquad
\boxed{\;N = \sqrt{\frac{2}{L}}\;}
{{< /katex >}}

이 결과는 [상자 속 입자]({{< ref "particle-in-a-box.md" >}})에서 그대로
쓰입니다.

## 파동함수가 만족해야 할 네 조건

모든 함수가 파동함수가 될 수 있는 것은 아닙니다. 확률로 해석되려면 다음을
만족해야 합니다.

1. 유한해야 합니다. 어떤 유한한 영역에서 무한대가 되면 확률밀도도 무한대가
되고, 그러면 적분이 발산해 정규화가 불가능해집니다.

2. 일가함수여야 합니다. 한 위치에서 두 개 이상의 값을 가지면 그 위치의
확률밀도가 둘이 되는데, 같은 자리에서 확률이 두 개일 수는 없습니다. (이 조건이
[회전]({{< ref "rotation.md" >}})에서 각운동량을 양자화합니다.)

3. 연속이어야 합니다. 확률밀도가 갑자기 끊기면 그 지점에서 입자를 발견할
확률이 정의되지 않습니다.

4. 1차 도함수도 연속이어야 합니다. 방정식에
{{< katex >}}d^2\psi/dx^2{{< /katex >}} 이 들어 있으므로,
{{< katex >}}d\psi/dx{{< /katex >}} 가 꺾이면 2차 도함수가 무한대가 되어
방정식이 성립하지 않습니다. 다만 퍼텐셜 자체가 무한대로 뛰는 자리에서는 이
조건이 완화되며, 상자 속 입자의 벽에서 실제로 그런 일이 일어납니다.

이 네 조건이 양자화를 만듭니다. 방정식은 어떤
{{< katex >}}E{{< /katex >}} 에도 해를 주지만, 그중 네 조건을 모두 통과하는
것은 띄엄띄엄한 {{< katex >}}E{{< /katex >}} 뿐입니다. 양자수란 그
걸러내기에서 살아남은 것들에 번호를 붙인 것입니다.

이어지는 세 문제가 같은 일을 세 가지 퍼텐셜에서 직접 보여 줍니다. 벽에 갇힐 때
([상자]({{< ref "particle-in-a-box.md" >}})), 용수철에 묶일 때
([진동자]({{< ref "oscillator.md" >}})), 한 바퀴 돌아 제자리로 올 때
([회전]({{< ref "rotation.md" >}}))입니다.

## 연산자와 기대값

측정을 예측하는 방법도 필요합니다. 물리량 {{< katex >}}A{{< /katex >}} 에
연산자 {{< katex >}}\hat{A}{{< /katex >}} 가 대응할 때, 정규화된
{{< katex >}}\psi{{< /katex >}} 에 대한 기대값은

{{< katex display=true >}}
\boxed{\;\langle A \rangle = \int \psi^*\hat{A}\psi\,d\tau\;}
{{< /katex >}}

입니다. 같은 상태를 여러 번 준비해 같은 양을 반복 측정했을 때의
평균값입니다.

**흔한 오해를 하나 짚어 두겠습니다.** 기대값은 "매번 이 값이 측정된다" 는 뜻이
아닙니다. 측정값은 매번 다를 수 있고 그 평균이 이 값이라는 뜻입니다. 주사위의
기대값이 3.5 이지만 3.5 가 나오는 일은 없는 것과 같습니다.

다만 특별한 경우가 있습니다. {{< katex >}}\psi{{< /katex >}} 가
{{< katex >}}\hat{A}{{< /katex >}} 의 고유함수이면, 즉
{{< katex >}}\hat{A}\psi = a\psi{{< /katex >}} 이면

{{< katex display=true >}}
\langle A \rangle = \int \psi^*(a\psi)\,d\tau = a\int \psi^*\psi\,d\tau = a
{{< /katex >}}

가 되고, 이때는 매번 정확히 {{< katex >}}a{{< /katex >}} 가 측정됩니다.
{{< katex >}}\hat{H}\psi = E\psi{{< /katex >}} 를 만족하는 상태에서 에너지가
확정값을 갖는 이유가 여기에 있습니다.

그런데 같은 상태에서 위치는 확정값을 갖지 않습니다. 한 상태가 모든 물리량에
대해 동시에 고유상태일 수는 없으며, 그 사실을 정량적으로 표현한 것이 불확정성
원리입니다.

## 숫자로 확인하기

**정규화 상수의 크기와 단위.**
{{< katex >}}L = 1.0\ \mathrm{nm}{{< /katex >}} 이면

{{< katex display=true >}}
N = \sqrt{\frac{2}{1.0\times10^{-9}\ \mathrm{m}}} = 4.5\times10^{4}\ \mathrm{m^{-1/2}}
{{< /katex >}}

단위가 {{< katex >}}\mathrm{m^{-1/2}}{{< /katex >}} 인 것이 어색해 보이지만
맞는 결과입니다. {{< katex >}}|\psi|^2{{< /katex >}} 이 단위 길이당 확률이어야
하므로 {{< katex >}}|\psi|^2{{< /katex >}} 의 단위가
{{< katex >}}\mathrm{m^{-1}}{{< /katex >}} 이고, 따라서
{{< katex >}}\psi{{< /katex >}} 는 그 제곱근인
{{< katex >}}\mathrm{m^{-1/2}}{{< /katex >}} 입니다. 3 차원이면
{{< katex >}}\mathrm{m^{-3/2}}{{< /katex >}} 이 됩니다.

**왼쪽 절반에 있을 확률.** 같은 파동함수로

{{< katex display=true >}}
P\left(0 \le x \le \tfrac{L}{2}\right)
= \frac{2}{L}\left[\frac{x}{2} - \frac{L}{4\pi}\sin\frac{2\pi x}{L}\right]_0^{L/2}
{{< /katex >}}

{{< katex >}}x = L/2{{< /katex >}} 에서
{{< katex >}}\sin\pi = 0{{< /katex >}} 이므로 둘째 항이 또 사라지고

{{< katex display=true >}}
P = \frac{2}{L}\cdot\frac{L}{4} = \frac{1}{2}
{{< /katex >}}

정확히 절반입니다. 당연한 결과이지만, 당연하다는 점이 중요합니다. 파동함수가
상자 가운데에 대해 좌우 대칭이므로 왼쪽과 오른쪽의 확률이 같아야 하기
때문입니다. 계산이 대칭성이 요구하는 답을 내놓는지 확인하는 것은 값싸고
효과적인 검산입니다.

같은 계산을 왼쪽 4 분의 1 에 대해 하면 25% 가 아니라 9.1% 가 나옵니다.
거기서는 대칭이 도와주지 않아 고전적 직관과 어긋나는 답이 나오는데, 자세한
내용은 [상자 속 입자]({{< ref "particle-in-a-box.md" >}})에서 다시
다루겠습니다.

방정식과 해석이 갖춰졌으니 이제 퍼텐셜을 넣을 차례입니다. 가장 단순한 퍼텐셜인
[상자 속 입자]({{< ref "particle-in-a-box.md" >}})로 넘어가겠습니다.
