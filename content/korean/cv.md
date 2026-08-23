---
menu:
  after:
    name: cv
    weight: 7
title: cv
type: docs
---

## 연구를 시작하기까지

- 얘기 듣고 나누는 걸 좋아합니다. 어려서부터 메모를 많이 하는데 이십년은 되었고 혼자 정리하는 방법이 생겼습니다.
- 스타를 많이 했을 때는 연습생 제의도 받을 만큼 해보기도 했습니다. 지금은 남이 이런 저런 게임 하는 걸 즐겨봅니다.
- 콘서트나 영화제 가는 것을 좋아하지만, 연구를 시작하고 나서는 못 가봤습니다. 다큐영화제 EIDF 는 가지 않아도 EBS 에서 방영해주는데 챙겨본 지는 십년 쯤 되었습니다. 여러 음악을 좋아하는데 제일은 바로 앞에서 연주 듣는 걸 제일 좋아합니다.
- 늦게 아카데미로 들어와 궁금한 것들을 배우고 생각한 걸 실험적으로 확인 하는 데서 얻는 만족이 큽니다.
- 학부 졸업하고 처음 일한 곳이 챗봇 만드는 스타트업 이었고, 이후 보라매병원, 딥노이드 등 여러 곳에서 기술을 가져다 구현하는 일을 했었습니다. 바탕이 되는 연구를 하고 싶다고 혼자서 공부하다가 이년전에 인공지능 석사과정을 시작하였습니다.

### 출판된 논문

- Physics-informed approach for exploratory Hamilton--Jacobi--Bellman equations via policy iterations, 2025, 공저자, AAAI-2026
- [Acceleration of grokking in learning arithmetic operations via Kolmogorov–Arnold representation](https://www.sciencedirect.com/science/article/pii/S0925231225010197), 2025, 1저자
- [Physics-informed neural networks for optimal vaccination plan in SIR epidemic models](https://www.aimspress.com/article/doi/10.3934/mbe.2025059), 2025, 1저자
- [Deep-Learning-Based Cerebral Artery Semantic Segmentation in Neurosurgical Operating Microscope Vision Using Indocyanine Green Fluorescence Videoangiography](https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2021.735177/full), 2022, 1저자

아래는 제출된 연구 입니다.

- Stabilized Neural Hamilton-Jacobi-Bellman Solvers: Error Analysis and Applications in Model-Based Reinforcement Learning, 2026, 1저자, NeurIPS-2026 submitted
- A Physics-Informed, Global-in-Time Neural Particle Method for the Spatially Homogeneous Landau Equation, 2026, 1저자, JCP submitted

아래는 작성 중인 논문입니다.

- “diffusion for CEV model”, 2026, 1저자
- “inhomogeneous Landau equation”, 2026, 1저자
- “generative model for BGK”, 2026, 1저자

## 경력

- **기획 / 개발** — 서비스 개발, 창업 (2021 – 2023). 풀스택 서비스 개발.
- **연구 / 개발** — 딥노이드, 의료인공지능 (2020 – 2021). 혈관 관련 의료 인공지능 연구 개발.
- **인턴** — 네이버 클로바AI, 인공지능 (2020). 자연어 모델 구현.
- **연구 / 개발** — 서울보라매병원 신경외과, 컴퓨터비전 (2019). 수술 영상을 이용한 혈관 분리 모델 구현.

## 학력

- **인공지능응용 (석사)** — 서울과학기술대학교, 2026년 2월
  - Solving HJB with PINN-PI
  - Grokking in Transformer
  - Physics-informed Neural Network on SIR dynamics
- **건축공학 (공학사), 무인이동체소프트웨어 (공학사), 컴퓨터공학 (부전공)** — 서울과학기술대학교, 2019년 2월
  - LSTM 이용한 자동 설계 (벽 자동 생성) 모델 구현
  - EMG 신호를 통한 손동작 구분 모델 구현

## 박사과정 하고자 하는 연구

- 자연과학에 대한 연구
- 제어에 대한 오랜 연구들과 심층학습을 연결하는 연구
- 만족가능이론들과 심층학습을 연결하는 연구
- 이를 바탕으로 한 어플리케이션 연구
  - VLA, World model, Physical AI 등 Robot 연구
  - ABM 으로 해석하는 Agent 연구

## 석사과정 연구

석사 학생으로 처음 연구를 무엇을 하면 될까 생각하면서 처음 든 생각은 두 가지였습니다.

- 보다 기초의 것을 하고 싶었습니다. 연구를 시작하는 시점에서 기초를 잘해두는 게 나중에 도움이 되겠다 생각이 들었습니다.
- 컴퓨팅 리소스가 적은 걸 하자.  
  무엇보다 이제 배워가는 학생이니 오류가 많을텐데, 가정한 것을 빠르게 돌려보고 확인하고 고치는 과정이 많을 테고 그래서 짧은 것이 유리하다 생각했습니다.

### Grokking 현상 : [Acceleration of grokking in learning arithmetic operations via Kolmogorov–Arnold representation](https://www.sciencedirect.com/science/article/pii/S0925231225010197), 2025, 1저자

어떤 것을 할까 고민하다가 처음 생각한 연구 방향은 데이터 패턴과 뉴럴 네트워크 캐퍼시티에 대한 연구 였습니다. 그래서 처음에는 learning theory, PAC, sample complexity 같은 것을 찾아다녔습니다. 뉴럴 네트워크에 대한 연구들을 살펴보다가 double descent 현상과 grokking 현상에 대한 논문을 보게 되었습니다.  
그로킹은 training accuracy 가 100% 를 도달한 뒤 지수스케일로 학습을 계속하면 어느 시점에서 validation accuracy 가 100%에 도달하는 현상을 말합니다. 아래 연구에서는 “2+10=? mod 10” 와 같이 group operation 의 결과를 맞추는 태스크에 집중합니다.

(Power et al., 2022)

![](/images/cv/fig-01-01982c10.png)

grokking 현상은 그 자체로 흥미로웠습니다. 태스크는 토큰을 예측하는 단순한 것이고 트랜스포머는 익숙하였기 때문에 grokking 재현을 우선 해보게 되었습니다. 공개된 코드가 있고 결과를 보는 건 어렵지 않았지만, 코드에는 없는, 논문 마지막에 첨부된 스캐터 플롯 하나가 제일 신기 하였습니다. 일반화가 이뤄지면 저런 구조가 생기는 게 아닐까 하는 생각이 바로 들었고 이를 재현하게 되었습니다.

(Power et al., 2022)

![](/images/cv/fig-02-01982bcb.png)

(재현한 연구, 2025)

![](/images/cv/fig-03-01982bce.png)

임베딩의 PCA 를 찍어보았습니다. 군이론 공부를 했던 차에 표현론이 있던 것이 떠올랐고, 이를 바탕으로 해석해볼 수 있지 않을까 생각하고 같이 연구하였던 박예찬 박사님과 임베딩 레이어와 디코더로 나누어 (Kolmogorov–Arnold representation theorem) 해석해보았습니다.

여러가지 실험으로 일반화된 것과 같이 학습 되었는지 확인해보았습니다. 두가지 결과가 재미있었는데, 먼저, tokenization 에 permutation 을 주었을 때 결과 였습니다. 토큰 매핑이 랜덤하게 변경된 경우에는 학습이 되지 않았으나, 규칙을 주어 변경한 경우에는 잘 전이 되었습니다.

(재현한 연구, 2025)

![](/images/cv/fig-04-01982bd7.png)

![](/images/cv/fig-05-01982bd8.png)

특히 재미있던 것은, 몇가지 토큰을 학습 데이터에서 제외시켜서 학습한 경우였습니다. 97개의 토큰에 대한 학습데이터 학습한 모델의 임베딩을 보다 어려운 연산으로 전이학습 시킬 때 80개의 토큰에 대한 학습데이터만 이용하여서 학습해보았는데, 그로킹이 되었습니다.

(재현한 연구, 2025)

![](/images/cv/fig-06-01982bd9.png)

이런 연구를 하면서 Group operation 으로 제한된 문제 공간을 간단하게 나마 살펴볼 수 있었습니다. 몇가지 질문이 남았습니다.

- Weight decay 가 그로킹에 영향을 미치는 이유는 무엇인가
- 그로킹에 도달할 수 있는 경우와 그렇지 못한 경우는 어떻게 나눌 수 있는가
- 최적화 과정에서 그로킹에 보다 잘 도달하게 할 수 있는 방법이 있다면 무엇이 있을까
- group operation 에서 보다 그로킹에 잘 도달하는 정도는 신경망 아키텍처를 비교하는데 적절한 지표가 될 수 있는가

### Optimal control using PINN : [Physics-informed neural networks for optimal vaccination plan in SIR epidemic models](https://www.aimspress.com/article/doi/10.3934/mbe.2025059), 2025, 1저자

그러고 나니, 제한된 문제를 신경망으로 여러가지 풀어보는 것이 신경망과 심층학습에 대해 이해하는 방법이 되지 않을까 생각을 하게 되었습니다. PINN 은 그런 면에서 좋은 방향으로 생각합니다. 모델이 없는 비용함수를 만들어 신경망의 학습을 살펴보는 것보다는 명확히 수학으로 기술할 수 있고 해석적으로 살펴볼 수 있는 문제(모델이 있는 문제)가 신경망을 연구할 때 좋은 대상이라고 생각하였습니다. 교수님께 PINN 을 해보고 싶다고 말씀 드리니 감염 역학에 대한 PDE 를 주셨습니다. {{< katex >}}u{{< /katex >}} 는 최적제어 시 일정 역치 밑으로 감염자가 줄어드는데 걸리는 시간 입니다.

(Hynd et al., 2021)

{{< katex display=true >}}
\beta x y \partial_x u + x (\partial_x u)^+ + (\gamma - \beta x) y \partial_y u = 1
{{< /katex >}}

PDE 가 유도되는 과정은 간결하였지만 쓰일 곳이 많다 생각이 들었습니다. Dynamic programming principle 이 적용될 수 있는 모든 문제에 적용될 수 있다고 생각합니다. (경계조건 역시 간결하게 유도될 수 있지만, 최적제어가 “bang-bang” 인 것의 유도는 어려웠습니다.)

라이브러리의 AD 와 그 API 들을 살펴보고 써보면서, 위 PDE 를 풀어보았습니다. PINN 에 적합한 아키텍처는 무엇일까, 스케일이 중요할까, 여러 고민을 하면서 실험해보았습니다.

(PINN 연구, 2025)

![](/images/cv/fig-07-01982bfc.png)

생각보다 잘 계산 되어 놀랐고 교수님께서 컨트롤을 얻어보자는 말씀을 하셨습니다. 최적제어 시 걸리는 시간을 알고 있고, 그것이 dynamic programming 을 따르니, 가지고 있는 {{< katex >}}u{{< /katex >}} 을 컨트롤을 태우면 그 결과에 따라 최적 제어 자체도 얻을 수 있지 않을까 하는 생각이었습니다. 몇 가지 모델을 추가하면 가능하지 않을까 말씀 드렸습니다. “뻔한 제어”에 대한 모델 ( {{< katex >}}u^{r_0}{{< /katex >}}), 감염자, 미감염자 모델을 마찬가지로 각각 PDE, ODEs 로 학습하였습니다.

(PINN 연구, 2025)

![](/images/cv/fig-08-01982c08.png)

그런데 생각처럼 잘 되지 않았습니다. 간단해 보였는데, 잘 되지 않았습니다. 이유를 살펴보기 위해, “뻔한” 제어를 태웠을 때의 결과와 최적 제어를 태웠을 때의 결과를 비교해보았습니다. 보니, “제어가 미치는 영향이 상대적으로 큰” 공간의 크기는 협소하였습니다. 고민을 계속하다가, Hynd et al, 2021 에서 “뻔하지 않은” 영역이 있음을 발견하였습니다. {{< katex >}}\frac{\partial u}{\partial x} \ge 0.0{{< /katex >}} 인 영역, 처음부터 백신을 주는 “뻔한 제어” 인 영역으로 볼 수 있었습니다. 또한 관련하여 페널티로 줄 수 있는 PDE 도 추가할 수 있었습니다.

(PINN 연구, 2025)

![](/images/cv/fig-09-01982c02.png)

![](/images/cv/fig-10-01982c0b.png)

이를 통해 최적제어까지 얻어낼 수 있었습니다. 몇가지가 신기하였습니다. 어떤 신경망 연산은 PINN 에 적합하지 않았습니다. 그것이 간단한 연산이었음에도 적합하지 않았습니다. 스케일링이 영향이 컸습니다. 몇가지 질문이 남았습니다.

- PINN 에 적합한 신경망 연산은 무엇이고 구조는 무엇인가
- 제네릭 피직스는 존재하는가 그리고 도움이 되는가
- 주파수가 큰 문제 외 PINN 으로 풀기 어려운 문제는 무엇이 있는가

### Landau equation

마지막으로는 homogeneous Landau equation 을 풀고 있으며, 생각한 방법론을 몇가지 예에 대해 실험해보았고 좋은 결과를 얻었습니다.

- [BKW 2d](https://youtu.be/tLBht-tc-cU)
- [arxiv](https://arxiv.org/abs/2603.10874)

## 하고 있는 것

### 뉴럴넷을 보는 관점

모델이 없는 목적함수 {{< katex >}}F(\theta)=\frac{1}{n}\sum*{i=1}^n f_i(\theta){{< /katex >}} 에 gradient descent 는 {{< katex >}}\theta*{k+1} = \theta*k - \eta \nabla F(\theta_k){{< /katex >}}인데, 여기서 시간에 대해 선형보간 하고, {{< katex >}}t_k := k\eta{{< /katex >}}, {{< katex >}}\Theta^\eta(t)=\theta_k \quad \text{for } t \in [t_k, t*{k+1}]{{< /katex >}}, 이를 차분하고 스텝에 극한을 취하면, gradient flow 를 얻을 수 있습니다.

{{< katex display=true >}}
\dot{\theta}(t) = -\nabla F(\theta(t)).
{{< /katex >}}

SGD 를 마찬가지로 관점으로 보게 되면, 데이터 분포를 {{< katex >}}\xi{{< /katex >}} 로 보고, {{< katex >}}F(\theta) := \mathbb E*\xi[f(\theta;\xi)]{{< /katex >}} 로 볼 수 있고, 배치에서의 그래디언트를 {{< katex >}}g(\theta_k,\mathcal B_k) := \frac1B \sum*{i\in\mathcal B*k} \nabla f_i(\theta_k){{< /katex >}} 로 볼 수 있는데, 이 노테이션으로 SGD 를 쓰면, {{< katex >}}\theta*{k+1} = \theta_k - \eta g(\theta_k,\mathcal B_k) = \theta_k - \eta \nabla F(\theta_k) - \eta \zeta_k{{< /katex >}} 가 되고, 여기서 데이터 분포를 위너 과정으로 보고, 시간에 대해 연속을 얻으면, 아래 SDE 를 얻을 수 있습니다.

{{< katex display=true >}}
d\theta_t = -\nabla F(\theta_t)dt + \sqrt{\tfrac{\eta}{B}} \Sigma(\theta_t)^{1/2} dW_t.
{{< /katex >}}

이렇게 얻은 연속시간 근사한 SDE 에 따라 최적화가 이뤄진다고 볼 수 있는데, 여러가지 optimizer 가 loss landscape 을 타고 내려가는 다양한 방법을 생각해볼 수 있으며, 예를 들어,

아래와 같이 Langvin dynamics 로 sampling 하면서 최적화를 해볼 수 있다고 생각합니다.

(랑제빈 샘플링 실험)

![](/images/cv/fig-11-01982fce.png)

만약에 이를 네트워크 구조 내에 Reparameterization trick 처럼 사용한다면, 일종의 BNN 으로 볼 수 있다고 생각합니다.

긴 호흡으로 보자면, 문제 공간은 집합, 위상, 그리고 적절한 메트릭을 가진 공간일 수 있습니다. 모델이 있다면 공간을 문제에 대한 상태들에서 유도해볼 수 있고, 문제에 맞는 적절한 메트릭을 고안할 수 있을지 모릅니다. 어떤 위상에 적합할 수도 있을지 모르고(TDA), grokking 연구에서 처럼 안에 군 구조(Lie group)를 가지고 있을지 모릅니다. 실험해보고 landscape 을 눈으로 확인하는 것을 하고 싶습니다.

(Zeyuan Allen-Zhu et al., 2018)

![](/images/cv/fig-12-019831ef.png)

### CFG

CFG 로 딥러닝을 살펴보는 연구에 대한 아이디어가 있었고, 관련 연구를 먼저 박사분 논문을 보면서, 가지고 있던 아이디어를 확장시켜보고 있습니다. [Physics of Language Models - Part 1: Hierarchical Language Structures](https://physics.allen-zhu.com/part-1)
관련 연구를 진행했으나, 여러 관점으로 넓혀서 아이디어를 스케치하고 있는 상태입니다.

![](/images/cv/fig-13-01997112.png)

### 그래프 이론과 데이터 분포

GAN 을 OT 관점에서 살펴보는 여러 연구를 살펴보았고, C-transform, JKO scheme 등 다양한 OT 관련 공부를 하고 있습니다.
그로킹의 group operation 문제는 {{< katex >}}f_n(x_1,...,x_n):=x_1\circ x_2 \circ...\circ x_n{{< /katex >}} 로 볼 수 있는데,

“언제 그로킹이 되고 언제는 안되는가”에 답하는 방법을 고민해보았습니다.

### PINN 에 적절한 아키텍처

어떤 분포에 맞는 Neural network architecture 에 대해서 Geometric Neural network 관점에서 공부했습니다.
transformer 는 PINN 에 적합하지 않았습니다. PINN 으로 최적화하는데 있어 적절한 아키텍처는 무엇인지 고민해보았고, Learning theory 관점으로 해석이 필요하다는 경험을 하고 있습니다.

### 계산과학

결국 세가지 관점에서 계산과학을 공부하고 있습니다.

- 계산할 수 있게 수학을 배우는 것이 수학을 제대로 배우는 것이라는 생각
- 세상의 것들을 보는 관점이 계산이란 목표로 간명해질 수 있음
- 컴퓨터를 더 잘 쓰는 훈련

### World model

HJB equation 을 풀고, 여러 문제에 대해 몇가지 RL 알고리즘과 비교해보면서 경험한 것은, sparse reward, long-horizon reward 가 어렵다는 것이었습니다. 그러다가 올해 KIAS 에서 열렸던 “AI x mathematics” 에서 Sergei Gukov 교수님의 발표를 들으면서 World model 에 관심이 생기게 되었습니다. 단순히 Physics 를 online 으로 동시에 배우게 하는 알고리즘 정도로만 생각했었는데, 이에 대한 연구가 더 방대하고, 구조적으로 중요한 연구가 아닐까 생각하고 있습니다. 현재는 Dreamer 계열의 generated trajectory 를 다루는 큰 구조 자체가 MPC 가 제어에서 큰 역할을 하고 있는 이유와 닮아보여서, 현재는 이 계열의 연구를 살펴보고 있습니다.

### Robot

직전 학기에 연세대학교 신동준 교수님과 서울과학기술대학교 김정엽 교수님의 로봇 수업을 들었습니다. 수업은 한 학기에 kinematics 에서 trajectory planning, motion control 를 넘어서, 설계까지 포함한 방대하고 빠른 수업이었습니다. 처음 이론 부분에서는 Jacobian 을 계산한다는 것이 무엇인지, Redundancy 와 null space 에서 singularity 를 피하면서 제어하는 것이 무엇인지 배웠습니다.

로봇 설계에서 고려해야 할 것들이 무엇이 있는지 Three link-revolve arm 예를 가지고 틀을 잡고, 휴봇을 만들면서 교수님이 겪으셨던 구체적인 경험들, 노하우들, 적어두면 도움이 될 것 같은 얘기들을 소중히 모을 수 있었던 시간 이었습니다. Any2track 같은 imitation learning framework 도 돌려볼 수 있었고, Mujoco 에서 Franka emika panda 제어도 해보았습니다.

- [spot welding panda](https://www.youtube.com/watch?v=Qs4GrFkMw5I)
- [hw2-2 advanced robotics](https://www.youtube.com/watch?v=lzpQXXdP0N0)

### LLM

Chain-of-thought, Prompt, context, harness engineering 까지 LLM 을 사용하는데 있어서 중요한 방법론들이 계속 제안되고, 이 차이를 이해하고 싶어졌습니다. 궁금해서 LoRA, QLoRA 등으로 SFT 도 해보고, 실험해보았습니다. 사용하다보니 결국 점점 저만의 시스템이 필요하다는 생각을 하게 되었고 계속 업데이트하고 있습니다.

![](/images/cv/research-llm.png)

### Lean

수학을 더 공부하고 싶습니다. 교수님과 수학에 집중된 연구를 하다보니, 많은 공부를 할 수 있었습니다. 여러 컨퍼런스, 워크샵, 다른 박사님들과의 협업, 미팅들을 하면서, 많은 공부를 할 수 있었지만, 근래에는 PDE analysis 에 필요한 수학적 프레임워크가 부족하다고 생각하여 이를 공부하고 있습니다. 며칠 전에는 L2 space, test function, weak form, riesz representation theorem 과 weak derivative, FEM 등이 하나로 정리되기도 하였습니다.

이렇게 수학 공부를 하면서, 수학적 지식을 정리해야 할 필요를 느꼈고, 저만의 lean system 을 구축하였습니다. 수학 개념 간 관계를 한눈에 보기 쉽게 하였고, 검증이 쉽게, 관련된 도구를 개발해서 다양하게 사용하고 있습니다.

![](/images/cv/research-lean-01.png)

![](/images/cv/research-lean-02.png)

### ABM

수유너머에서 스터디 할 때 위층에 있는 수많은 책들 중에 눈에 띄었던 것은 행위자 이론 이었습니다. 학부 때 Agent-based modeling 이란 수업을 들었었고 집회에 대해 모델링 해보기도 했습니다. 사회학에서 논의되는 것보다는 공학적인 관점이었지만, 아이디어는 참 재밌다고 생각했습니다. 특히 LLM 의 기능을 Agent 로까지 확장시키고 있는 근래에 LLM 의 기능 생태계에 대한 해석 차원에 도움이 될 뿐 아니라, dynamics 를 수학적으로 표현할 수 있고, 이에 대해 여러 연구를 한 지금에서는 새로운 알고리즘이나, 방법론을 제안하는데 도움이 될 것이라 생각하여 여러가지 해보고 있습니다.

![](/images/cv/research-abm-01.png)

![](/images/cv/research-abm-02.png)

### Ontology

개발일을 할 때, 좀 더 semantic 하게 서비스를 구축하기 위해서 OWL 같은 표준을 공부하고 구축해보기도 하였습니다. 그러나 웹 세상은 훨씬 자유로웠고, 처리는 제한되었습니다. 근래에 LLM alignment 와 safety 에 대해서 ontology 가 중요해졌고 개인적으로도 가지고 있는 지식을 ontology 로 정리하는 것이 도움이 된다고 생각하여서 개인적인 용도의 ontology map 을 구축하고 있습니다.

![](/images/cv/research-ontology-01.png)

![](/images/cv/research-ontology-02.png)
