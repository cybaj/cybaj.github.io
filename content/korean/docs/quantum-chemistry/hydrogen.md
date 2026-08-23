---
title: 수소꼴 원자
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 60
item: 2026-08-23-quantum-chemistry
---

지금까지 푼 세 문제는 모두 인공적이었습니다. 무한히 높은 벽도, 완벽한
포물선도, 반지름이 고정된 고리도 자연에는 없습니다. 다만 세 경우 모두
경계조건이 허용되는 해를 걸러내면서 에너지가 띄엄띄엄해졌습니다.

이제 자연에 실제로 있는 퍼텐셜을 넣겠습니다. 핵이 전자를 끌어당기는 Coulomb
퍼텐셜이고, 전자가 하나뿐이라면 이것도 정확히 풀립니다.
(개인 노트: 6장 수소꼴 원자)

## 맞혀야 할 표적

먼저 설명해야 할 것이 있습니다. 수소 기체를 방전시켜 나온 빛을 프리즘에
통과시키면 연속된 무지개가 아니라 정해진 파장의 선 몇 개만 나오는데, 그
파장들이 단순한 규칙을 따릅니다.

{{< katex display=true >}}
\boxed{\;\tilde{\nu} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)\;}
{{< /katex >}}

{{< katex >}}R_H{{< /katex >}} 는 Rydberg 상수이고
{{< katex >}}n_1 < n_2{{< /katex >}} 는 그냥 정수입니다.
{{< katex >}}n_1 = 2{{< /katex >}} 로 두고
{{< katex >}}n_2 = 3, 4, 5, \dots{{< /katex >}} 를 넣으면 가시광선 영역의
Balmer 계열이 나오고, {{< katex >}}n_1 = 1{{< /katex >}} 로 두면 자외선의
Lyman 계열이 나옵니다.

이 식은 실험에서 먼저 발견되었고, 왜 이런 모양인지는 아무도 몰랐습니다. 정수
두 개와 상수 하나로 원자가 내는 모든 빛이 설명된다는 것이
수수께끼였습니다.

## Coulomb 퍼텐셜

핵전하가 {{< katex >}}+Ze{{< /katex >}} 이고 전자가 하나인 계를
수소꼴 원자라 합니다. 수소({{< katex >}}Z=1{{< /katex >}})뿐 아니라
{{< katex >}}\mathrm{He^+}{{< /katex >}},
{{< katex >}}\mathrm{Li^{2+}}{{< /katex >}} 도 포함됩니다.

전자와 핵 사이의 퍼텐셜 에너지는 Coulomb 법칙에서 옵니다.

{{< katex display=true >}}
V(r) = -\frac{Ze^2}{4\pi\varepsilon_0 r}
{{< /katex >}}

부호가 음수인 것은 끌어당기는 힘이기 때문입니다. 전자를 무한히 멀리
떼어놓았을 때를 0 으로 잡았으므로 가까이 올수록 에너지가 내려가고,
{{< katex >}}r \to 0{{< /katex >}} 에서 발산합니다.

앞의 세 퍼텐셜과 결정적으로 다른 점이 있습니다. 이 퍼텐셜은 어느 방향으로나
같아서, {{< katex >}}r{{< /katex >}} 에만 의존하고
{{< katex >}}\theta, \phi{{< /katex >}} 에는 의존하지 않습니다. 구대칭이라는
이 사실 하나가 문제를 절반으로 줄여 줍니다.

Schrödinger 방정식은 3차원이므로 2차 미분이
{{< katex >}}\nabla^2{{< /katex >}} 로 바뀝니다.

{{< katex display=true >}}
-\frac{\hbar^2}{2\mu}\nabla^2\psi - \frac{Ze^2}{4\pi\varepsilon_0 r}\psi = E\psi
{{< /katex >}}

### 환산질량이 여기에도

질량 자리에 {{< katex >}}m_e{{< /katex >}} 가 아니라
{{< katex >}}\mu{{< /katex >}} 가 들어간 것을 눈여겨볼 만합니다.
[조화 진동자]({{< ref "oscillator.md" >}})에서와 같은 이유로, 핵도 가만히 있지
않고 전자와 함께 공통 질량중심 주위를 돌기 때문입니다.

{{< katex display=true >}}
\mu = \frac{m_e m_N}{m_e + m_N}
{{< /katex >}}

양성자가 전자보다 1836 배 무거우므로
{{< katex >}}\mu \approx 0.99946\,m_e{{< /katex >}} 로 거의 차이가 없습니다.
그런데 이 0.05% 가 실제로 측정됩니다. 수소와 중수소는 핵 질량이 두 배
다르므로 {{< katex >}}\mu{{< /katex >}} 가 다르고, 따라서 스펙트럼선이 아주
조금 어긋납니다. 중수소는 이 차이로 발견되었습니다.

## 변수분리: 절반은 이미 풀려 있다

구대칭 덕분에 해를 두 조각의 곱으로 쓸 수 있습니다.

{{< katex display=true >}}
\boxed{\;\psi(r,\theta,\phi) = R(r)\,Y(\theta,\phi)\;}
{{< /katex >}}

{{< katex >}}R(r){{< /katex >}} 는 핵에서 얼마나 떨어져 있는지를,
{{< katex >}}Y(\theta,\phi){{< /katex >}} 는 어느 방향인지를 담당합니다.

그런데 각도 부분은 새로 풀 것이 없습니다. 방정식에서 각도에 관한 부분은
퍼텐셜과 전혀 무관하고, [구면 위의 입자]({{< ref "rotation.md" >}})에서 이미
푼 것과 똑같기 때문입니다. 답은 구면조화함수입니다.

{{< katex display=true >}}
Y(\theta,\phi) = Y_l^{m_l}(\theta,\phi)
{{< /katex >}}

이것이 왜 눈여겨볼 만한 일인지 짚어 두겠습니다. 오비탈의 모양은 전자가 핵에
어떻게 끌리는지와 아무 상관이 없습니다. Coulomb 이든 다른 무엇이든 퍼텐셜이
구대칭이기만 하면 각도 의존성은 같습니다. {{< katex >}}s{{< /katex >}} 가
구형이고 {{< katex >}}p{{< /katex >}} 가 아령인 것은 공간이 3차원이고 방향에
특별함이 없다는 사실에서 나온 것이지 전기력에서 나온 것이 아닙니다.

남은 것은 반지름 방정식뿐입니다.

## 유효 퍼텐셜: 원심력 장벽

반지름 방정식을 정리하면 퍼텐셜이 하나 더 붙은 1차원 문제처럼 보이게 만들 수
있습니다.

{{< katex display=true >}}
\boxed{\;V_{\mathrm{eff}}(r) = -\frac{Ze^2}{4\pi\varepsilon_0 r}
+ \frac{l(l+1)\hbar^2}{2\mu r^2}\;}
{{< /katex >}}

둘째 항은 각운동량에서 온 것입니다. 회전하는 물체를 안쪽으로 끌어당기려면
각운동량을 유지하는 데 드는 에너지를 이겨야 하기 때문입니다. 고전역학의
원심력에 대응하는 항이라 **원심력 장벽**(centrifugal barrier)이라 부릅니다.

부호와 거듭제곱을 보겠습니다. 첫 항은 음수이고
{{< katex >}}1/r{{< /katex >}} 로 잦아들며, 둘째 항은 양수이고
{{< katex >}}1/r^2{{< /katex >}} 로 잦아듭니다. 가까운 거리에서는 둘째 항이
이기므로, {{< katex >}}l > 0{{< /katex >}} 인 전자는 핵에 가까이 갈 수
없습니다.

{{< katex >}}l = 0{{< /katex >}} 이면 둘째 항이 아예 0 이라 장벽이 없고,
{{< katex >}}s{{< /katex >}} 전자만 핵까지 갈 수 있습니다. 이 사실이
[다전자 원자]({{< ref "many-electron.md" >}})에서 결정적으로 쓰이며, 침투와
가림이 모두 여기서 나옵니다.

## 세 개의 양자수

경계조건들이 세 개의 정수를 남깁니다.

{{< katex display=true >}}
\boxed{\;n = 1, 2, 3, \dots \qquad
l = 0, 1, \dots, n-1 \qquad
m_l = 0, \pm1, \dots, \pm l\;}
{{< /katex >}}

{{< katex >}}l{{< /katex >}} 과 {{< katex >}}m_l{{< /katex >}} 은 회전
문제에서 이미 나왔고, 새로 생긴 것은 두 가지입니다.

**{{< katex >}}n{{< /katex >}} 이라는 새 양자수.** 반지름 방향의 경계조건
({{< katex >}}r \to \infty{{< /katex >}} 에서
{{< katex >}}\psi \to 0{{< /katex >}})에서 나옵니다. 주양자수라 부르며 껍질을
매깁니다.

**{{< katex >}}l < n{{< /katex >}} 이라는 제약.** 이쪽이 새롭습니다. 회전
문제에서는 {{< katex >}}l{{< /katex >}} 에 상한이 없었는데 여기서는
{{< katex >}}n{{< /katex >}} 이 막습니다. 원심력 장벽 때문인데,
{{< katex >}}l{{< /katex >}} 이 너무 크면 장벽이 높아져서 그
{{< katex >}}n{{< /katex >}} 에 해당하는 에너지로는 묶인 상태를 만들 수
없습니다. 그래서 {{< katex >}}n=1{{< /katex >}} 껍질에는
{{< katex >}}s{{< /katex >}} 만, {{< katex >}}n=2{{< /katex >}} 에는
{{< katex >}}s{{< /katex >}} 와 {{< katex >}}p{{< /katex >}} 만 있습니다.

## 에너지: 표적을 맞히다

반지름 방정식을 풀면 에너지가 나옵니다.

{{< katex display=true >}}
\boxed{\;E_n = -\frac{hcR_H Z^2}{n^2}\;}
{{< /katex >}}

부호가 음수인 것은 묶인 상태라는 뜻입니다. 전자를 무한히 떼어놓은 상태를
0 으로 잡았으므로, 원자 안에 있는 전자는 그보다 낮은 곳에 있습니다.

이제 두 준위 사이의 전이를 보겠습니다. 광자 하나가 나오면서 원자가
{{< katex >}}n_2{{< /katex >}} 에서 {{< katex >}}n_1{{< /katex >}} 으로
떨어진다면

{{< katex display=true >}}
\Delta E = E_{n_2} - E_{n_1}
= -hcR_H\left(\frac{1}{n_2^2} - \frac{1}{n_1^2}\right)
= hcR_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
{{< /katex >}}

{{< katex >}}\Delta E = hc\tilde{\nu}{{< /katex >}} 이므로 양변을
{{< katex >}}hc{{< /katex >}} 로 나누면

{{< katex display=true >}}
\tilde{\nu} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
{{< /katex >}}

Rydberg 식입니다. 실험에서 규칙으로만 알려져 있던 식이 Coulomb 법칙과
Schrödinger 방정식에서 유도된 것입니다. 정수 두 개는 경계조건이 남긴
양자수이고, Rydberg 상수는 기본 상수들의 조합입니다.

### 이상한 겹침 하나

에너지 식을 다시 보면 이상한 점이 있습니다. {{< katex >}}n{{< /katex >}} 에만
의존하고 {{< katex >}}l{{< /katex >}} 이 들어 있지 않습니다.

{{< katex >}}2s{{< /katex >}} 와 {{< katex >}}2p{{< /katex >}} 의 에너지가
같다는 뜻입니다. 하나는 구형이고 하나는 아령이며 하나는 핵까지 갈 수 있고
하나는 그러지 못하는데도, 에너지는 그 차이를 구별하지 못합니다.

{{< katex >}}m_l{{< /katex >}} 에 대한 겹침은 이해할 수 있습니다.
[회전]({{< ref "rotation.md" >}})에서 본 대로 공간에 특별한 방향이 없기
때문입니다. 그런데 {{< katex >}}l{{< /katex >}} 에 대한 겹침은 그런 대칭에서
나오지 않습니다.

이것을 **우연한 겹침**(accidental degeneracy)이라 하며,
{{< katex >}}1/r{{< /katex >}} 라는 Coulomb 퍼텐셜의 특별한 형태에서만
일어납니다. 퍼텐셜이 조금이라도 {{< katex >}}1/r{{< /katex >}} 에서 벗어나면
곧바로 깨지는데, [다전자 원자]({{< ref "many-electron.md" >}})에서는 다른
전자들 때문에 정확히 그 일이 일어납니다.

따라서 {{< katex >}}n{{< /katex >}} 껍질의 총 겹침 수는

{{< katex display=true >}}
\sum_{l=0}^{n-1}(2l+1) = n^2
{{< /katex >}}

입니다. {{< katex >}}n=1{{< /katex >}} 이면 1 개,
{{< katex >}}n=2{{< /katex >}} 면 4 개,
{{< katex >}}n=3{{< /katex >}} 이면 9 개입니다. 스핀까지 세면 두 배가 되어
{{< katex >}}2n^2{{< /katex >}} 이 되는데, 주기율표에서 각 주기의 길이가
2, 8, 18 인 이유가 여기에 있습니다.

## 오비탈의 모양과 마디

{{< katex >}}(n, l, m_l){{< /katex >}} 하나마다 파동함수가 하나 있고, 이것을
원자 오비탈이라 합니다. 바닥 상태는
{{< katex >}}(1,0,0){{< /katex >}}, 즉 {{< katex >}}1s{{< /katex >}} 이고

{{< katex display=true >}}
\psi_{1s} = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}
{{< /katex >}}

로 간단합니다. {{< katex >}}a_0{{< /katex >}} 는 Bohr 반지름입니다.

{{< katex display=true >}}
a_0 = \frac{4\pi\varepsilon_0\hbar^2}{m_ee^2} = 52.9\ \mathrm{pm}
{{< /katex >}}

마디는 두 종류입니다. 각도 마디는 구면조화함수가 만들어
{{< katex >}}l{{< /katex >}} 개이고, 반지름 마디는 반지름 함수가 만들어
{{< katex >}}n-l-1{{< /katex >}} 개입니다. 합치면

{{< katex display=true >}}
\text{전체 마디 수} = l + (n-l-1) = n-1
{{< /katex >}}

{{< katex >}}n{{< /katex >}} 에만 의존합니다. 그리고 에너지도
{{< katex >}}n{{< /katex >}} 에만 의존합니다. 우연이 아니라, 앞에서 계속 보아
온 곡률이 곧 에너지라는 원리가 여기서도 작동하는 것입니다. 마디가 같으면 곡률이
비슷하고 에너지도 같습니다.

## 확률밀도와 방사방향 분포는 다르다

여기가 처음 배울 때 가장 많이 걸리는 지점입니다.

{{< katex >}}1s{{< /katex >}} 의 확률밀도는

{{< katex display=true >}}
|\psi_{1s}|^2 = \frac{1}{\pi a_0^3}e^{-2r/a_0}
{{< /katex >}}

로 {{< katex >}}r = 0{{< /katex >}} 에서 최대입니다. 그렇다면 전자는 핵 바로
위에 있을 가능성이 가장 큰 것일까요.

한 점만 보면 그렇습니다. 그러나 보통 알고 싶은 것은 "핵에서 거리
{{< katex >}}r{{< /katex >}} 쯤에서 전자를 발견할 확률" 이고, 그러려면 그
거리에 있는 껍질 전체를 봐야 합니다. 반지름 {{< katex >}}r{{< /katex >}},
두께 {{< katex >}}dr{{< /katex >}} 인 구 껍질의 부피는

{{< katex display=true >}}
dV = 4\pi r^2\,dr
{{< /katex >}}

이므로 방사방향 분포함수는

{{< katex display=true >}}
\boxed{\;P(r) = 4\pi r^2|\psi(r)|^2\;}
{{< /katex >}}

가 됩니다. 두 인자가 서로 반대로 움직입니다.
{{< katex >}}|\psi|^2{{< /katex >}} 는 밖으로 갈수록 줄고
{{< katex >}}4\pi r^2{{< /katex >}} 는 밖으로 갈수록 늡니다. 핵 근처에는 확률이
빽빽하지만 담을 공간이 없고, 멀리 나가면 공간은 넓지만 확률이 희박하므로,
둘의 곱이 최대가 되는 어중간한 거리가 생깁니다.

{{< katex >}}1s{{< /katex >}} 에 대해 직접 구해 보겠습니다.

{{< katex display=true >}}
P(r) = 4\pi r^2\cdot\frac{1}{\pi a_0^3}e^{-2r/a_0} = \frac{4}{a_0^3}r^2e^{-2r/a_0}
{{< /katex >}}

미분해서 0 으로 놓으면

{{< katex display=true >}}
\frac{dP}{dr} = \frac{4}{a_0^3}\left[2r - \frac{2r^2}{a_0}\right]e^{-2r/a_0} = 0
{{< /katex >}}

{{< katex display=true >}}
2r\left(1 - \frac{r}{a_0}\right) = 0
\qquad \Longrightarrow \qquad
\boxed{\;r = a_0\;}
{{< /katex >}}

가장 있을 법한 거리가 정확히 Bohr 반지름입니다. Bohr 가 1913 년에 반쯤
고전적인 논증으로 얻었던 그 값이 Schrödinger 방정식에서는 확률분포의
최댓값으로 다시 나온 것입니다. Bohr 의 그림, 즉 정해진 궤도를 도는 전자라는
그림은 틀렸지만 그가 얻은 길이 척도는 옳았습니다.

덧붙이면 평균 거리는 최빈값과 다릅니다.
{{< katex >}}\langle r \rangle = \tfrac{3}{2}a_0 = 79.4\ \mathrm{pm}{{< /katex >}}
로 조금 더 큰데, 분포가 바깥쪽으로 긴 꼬리를 갖기 때문입니다.

## 숫자로 확인하기

**수소의 이온화 에너지.** 바닥 상태는
{{< katex >}}n=1, Z=1{{< /katex >}} 이므로

{{< katex display=true >}}
E_1 = -hcR_H = -13.6\ \mathrm{eV}
{{< /katex >}}

전자를 무한히 떼어내려면 13.6 eV 를 주어야 하고, 실측값은 13.598 eV 입니다.
Coulomb 법칙과 Schrödinger 방정식 말고는 아무것도 넣지 않았는데 소수점 셋째
자리까지 맞습니다.

**Balmer 계열의 첫 선.**
{{< katex >}}n_2 = 3 \to n_1 = 2{{< /katex >}} 이면

{{< katex display=true >}}
\tilde{\nu} = R_H\left(\frac{1}{4} - \frac{1}{9}\right)
= 109677 \times \frac{5}{36} = 1.523\times10^{4}\ \mathrm{cm^{-1}}
{{< /katex >}}

{{< katex display=true >}}
\lambda = \frac{1}{\tilde{\nu}} = 6.57\times10^{-5}\ \mathrm{cm} = 657\ \mathrm{nm}
{{< /katex >}}

**실측 {{< katex >}}H_\alpha{{< /katex >}} 선은 656.3 nm.** 수소 방전관과
성운이 붉게 보이는 것이 이 선 때문입니다.

**{{< katex >}}\mathrm{He^+}{{< /katex >}} 는 얼마나 더 단단히 묶여 있는가.**
{{< katex >}}Z=2{{< /katex >}} 이므로 {{< katex >}}Z^2{{< /katex >}} 만큼,
즉 4 배입니다.

{{< katex display=true >}}
E_1(\mathrm{He^+}) = -13.6 \times 4 = -54.4\ \mathrm{eV}
{{< /katex >}}

핵전하가 두 배가 되면 전자를 떼어내기가 네 배 어려워집니다. 실측값은
54.42 eV 이고, 전자가 하나뿐이면 원자번호가 얼마든 이 식이 그대로 맞습니다.

**전자는 원자 안에서 얼마나 빠른가.** 바닥 상태의 운동에너지는 위치 에너지의
절반 크기이므로(비리얼 정리) 13.6 eV 입니다.

{{< katex display=true >}}
v = \sqrt{\frac{2E_k}{m_e}} = \sqrt{\frac{2(13.6)(1.602\times10^{-19})}{9.109\times10^{-31}}}
= 2.19\times10^{6}\ \mathrm{m/s}
{{< /katex >}}

광속의 약 0.7% 입니다. 상대론적 보정이 아직은 작지만 무시할 수 없는
크기이고, 무거운 원자에서는 이 속도가 커져 상대론이 화학에 직접 영향을 줍니다.
금이 노랗고 수은이 액체인 것이 그 결과입니다.

전자가 하나면 여기까지 정확합니다. 둘부터는 사정이 완전히 달라지는데, 그
이야기를 [다전자 원자]({{< ref "many-electron.md" >}})에서 이어
가겠습니다.
