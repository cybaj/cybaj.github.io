---
menu:
  after:
    name: portfolio at 2024
    weight: 8
title: portfolio at 2024
type: docs
---

# portfolio at 2024

> "서비스 개발자가 되었는데 시뮬레이션과 모델 학습을 엮는 연구를 하고 싶습니다."
>
> PORTFOLIO 2024 · KIM MIN-SEOK

---

## 소개

- **전공** 건축공학 / **복수전공** 무인이동체소프트웨어전공 / **부전공** 컴퓨터공학
- **학교** 서울과학기술대학교 (2014.3. ~ 2019.2., 취득학점 188학점)
- 무인이동체소프트웨어전공은 자율전공으로 전자공학 + 컴퓨터공학 수업으로 이뤄짐
- 이후 주로 연구원으로 일해왔으며, 최근 기획한 서비스를 개발 마무리 중

| 링크 | 주소 |
| --- | --- |
| GitHub | https://github.com/cybaj |
| SlideShare | https://www.slideshare.net/ssuser2992b21 |
| Memo blog | https://llkor.blogspot.com/ |
| Reading | https://cybaj.github.io/reading |
| Coding study | https://cybaj.github.io/mycodeschema |

---

## Timeline

| 연도 | 활동 |
| --- | --- |
| **2022** | 가칭 'TH' 서비스 개발 · 영상 분류 모델 개발 · *Frontiers in Neurorobotics* 논문 게재 |
| **2021** | 가칭 'TH' 서비스 기획 · 웹 프레임워크(React, Vue)와 인프라(Kubernetes) 공부 · 연구원 활동 |
| **2020** | NAVER AI RUSH 참여 및 이후 인턴 · 보라매병원, 딥노이드에서 연구원 활동 |
| **2019** | 졸업 · Node 기반 웹개발 공부 · 선형 시스템 다이나믹스, 군론, 람다대수 공부 |
| **2018** | '텍스트팩토리' 연구/개발 인턴 · '싸이버스' AI 스터디 그룹 · 인공신경망, 신경과학 공부 |
| **2017** | 건축 BIM 데이터 RNN 활용 연구(논문 게재, 과내 졸업작품 우수상) · '직공' 서비스 창업동아리장 |
| **2016** | 겨울방학 딥러닝 세미나 주제 · WebGL 전시공간 구축(논문 1건, 학회 포스터 1건) · 국가기록원 연구과제 '다양한 전시 디스플레이 방법 구현' · '빅토리' 빅데이터 연합동아리(데이터 경진대회 최우수상) |
| **2015** | 국가기록원 연구과제 '실감형 색상 구현' · '헝그리' 맛집 어플리케이션 개발(안드로이드, PHP 서버) |
| **2014** | 한글 교육 어플리케이션 개발(안드로이드) |

---

## 목차

- [들어가며 — 2024년 대학원을 지원하면서](#들어가며)
- [논문](#논문)
  - [ICG를 이용한 혈관 구분 모델 개발 (2021–2022)](#icg를-이용한-혈관-구분-모델-개발-20212022)
  - [건축 BIM 데이터 RNN 활용 연구 (2017)](#건축-bim-데이터-rnn-활용-연구-2017)
  - [WebGL을 통한 전시공간 구축 (2016)](#webgl을-통한-전시공간-구축-2016)
- [연구 활동 및 스터디](#연구-활동-및-스터디)
- [졸업 작품](#졸업-작품)
- [대회 참가](#대회-참가)
- [기타 프로젝트](#기타-프로젝트)

---

## 들어가며

**2024년 대학원을 지원하면서**

시뮬레이션이 동원되는 연구에 관심이 많습니다. Lake, Ullman, Tenenbaum, Gershman의
**'Building Machines That Learn and Think Like People' (2017)** 에서 발췌한 내용을 정리했습니다.

- 논문 Figure 4의 **Intuitive Physics Engine** 파이프라인 — Inputs → 물리 엔진 → Outputs(`Will it fall?`, `Which direction?`). 입력을 바꾸면(블록 재질이 스티로폼/납/점액, 테이블이 유사, 중력이 반대) 같은 엔진으로 다른 예측을 만든다 (Battaglia et al., 2013 인용).
- Facebook AI의 **PhysNet** (Lerer, Gross & Fergus, 2016)은 CNN으로 블록 타워 안정성을 예측하고 합성 이미지에서는 사람을 능가하지만, 10만~20만 장 규모의 장면 학습이 필요하다. 사람은 훨씬 적은 경험으로 새로운 판단에 일반화한다는 대비가 핵심.
- 신경망을 시뮬레이션 없이 **general-purpose physics simulator** 로 학습시킬 수 있는가에 대한 논의.

![](/images/portfolio-2024/p06-1.webp)
![](/images/portfolio-2024/p07-1.webp)
![](/images/portfolio-2024/p07-2.webp)

---

## 논문

### ICG를 이용한 혈관 구분 모델 개발 (2021–2022)

**Deep-Learning-Based Cerebral Artery Semantic Segmentation in Neurosurgical Operating Microscope Vision Using Indocyanine Green Fluorescence Videoangiography**
· *Frontiers in Neurorobotics*
· https://www.frontiersin.org/articles/10.3389/fnbot.2021.735177/full

수술 현미경 영상에서 ICG 형광 혈관조영 영상을 입력으로 뇌혈관을 semantic segmentation 하는 모델.
클래스 정의는 동맥(Class 1) 대 정맥·배경 및 비혈관 해부 구조(Class 0) 이진 구분.
정성 비교는 **Ground Truth / DeepLabv3+ / FCN / DeepLabv3 / U-Net** 다섯 행으로 수술 영상 케이스별 예측 마스크를 오버레이해 제시.

![](/images/portfolio-2024/p08-1.webp)
![](/images/portfolio-2024/p09-1.webp)

### 건축 BIM 데이터 RNN 활용 연구 (2017)

**인공신경망 활용을 위한 BIM 데이터 구조화 연구 — 건축정보 온톨로지를 중심으로**
(*A Study about BIM Data Structuring for Artificial Neural Network*) · 주저자 김민석 · 과내 졸업작품 우수상

IFC 파일을 파싱해 각 벽 중심선의 global coordinates를 뽑고, 정렬(chain sorting)을 거쳐
`{1x, 1y, 2x, 2y, length, radian}` 6차원 벡터 시퀀스(sequence length 6)로 구조화한 뒤 **RNN(LSTM)** 으로 다음 벽을 예측.
학회 포스터 *'인공신경망을 이용한 BIM 설계자동화 방법의 기초연구'* 로도 발표 (Keywords: BIM, Design Automation, Artificial Neural Network, IFC).

![](/images/portfolio-2024/p10-1.webp)
![](/images/portfolio-2024/p11-1.webp)
![](/images/portfolio-2024/p11-2.webp)

### WebGL을 통한 전시공간 구축 (2016)

**웹 3D 디스플레이를 통한 3D 콘텐츠의 전시 및 정보제시 방법에 대한 고찰 — 웹을 통한 사이버박물관의 구축을 중심으로**
(*The 3D Contents and Information Display in the Web*) · 주저자 김민석 · 행정자치부 국가기록원 '기록보존기술 연구개발 사업' 지원

BIM 툴(ARCHICAD)로 전시 공간을 만들고 → WebGL에 적합한 3D 데이터(JSON)로 내보내고 → Three.js로 로딩·씬 구성하는
작업 흐름으로 **'국가기록원 가상전시관'** 을 구현. 기존 VRML 기반 공간 기술의 비용·렌더링 제약과 대비하고,
사이버 전시공간의 비물리성, 움직임의 자유(freedom of movement)와 컨트롤을 논의. 학회 포스터로도 발표.

![](/images/portfolio-2024/p12-1.webp)
![](/images/portfolio-2024/p13-1.webp)
![](/images/portfolio-2024/p13-2.webp)

---

## 연구 활동 및 스터디

### Computational neuroscience 공부 (2022)

CMU **Dave Touretzky** 의 강의(2017)와 교재 *Mathematics for Neuroscientists*, USC CSCI534 affective computing 을 따라 계산신경과학을 공부하였습니다.
뉴런이 받는 입력의 개수가 세포마다 크게 다르다는 것(소뇌 granule cell은 평균 4개, Purkinje cell은 10만여 개), 이온 채널이 **passive / active(voltage-gated) / ligand-gated** 로 나뉜다는 것, 그리고 cell body와 물질, 안정막전위가 약 −70 mV인 membrane potential을 정리하였습니다.
이어서 **Nernst potential** 과 Fick's law `J(r) = −D·dc/dr` 와 `D = μkT` 까지 공부하였고, MATLAB으로 back-Euler 적분 뉴런 모델을 직접 구현해 V(mV)–t 와 I(A/cm²)–t 를 플롯해 보았습니다.

![](/images/portfolio-2024/p14-1.webp)
![](/images/portfolio-2024/p14-2.webp)
![](/images/portfolio-2024/p15-1.webp)
![](/images/portfolio-2024/p15-2.webp)
![](/images/portfolio-2024/p15-3.webp)

### 서울보라매병원 및 딥노이드에서의 연구 활동 (2016~) — 혈관에 대한 다양한 연구

Ground Truth 영역을 **skeletonize** 해 혈관 구조를 그래프로 만들고 **networkx** 로 시각화.
뇌혈관 해부(MCA의 M1 horizontal / M2 Sylvian / M3 cortical segment, Willis 환의 ACA·ACOM·ICA·PCOM·PCA·BA·VA)를 정리하고,
3D 혈관 모델을 혈관구조 이름 group 으로 저장하는 annotation 툴을 만들어 semantic map 용 렌더링을 계획.
함께 **meta-learning**의 optimization-based approach(**MAML**: φᵢ ← θ − α∇L(θ, Dᵢᵗʳ), θ ← θ − β∇ΣL(φᵢ, Dᵢᵗᵉˢᵗ), 2차 미분 비용과 First-Order MAML)를 정리.

![](/images/portfolio-2024/p16-1.webp)
![](/images/portfolio-2024/p16-2.webp)
![](/images/portfolio-2024/p16-3.webp)
![](/images/portfolio-2024/p17-1.webp)
![](/images/portfolio-2024/p17-2.webp)
![](/images/portfolio-2024/p17-3.webp)

### 논문 리뷰 — PersonLab / Detectron2 (2020–2021)

**PersonLab**: keypoint-level detection과 person pixel의 **long-range offsets** 라는 geometric embedding으로
instance segmentation을 디코딩. 비교 대상인 *Associative Embedding*(같은 instance면 attract, 아니면 repel)은
representation을 해석하기 어렵다는 문제가 있음.
실제 수술 영상에 **Detectron2** 계열 instance segmentation을 적용해 `angio` 클래스로 신뢰도(100%, 99%, 86% 등)와 마스크를 출력했고,
instance가 겹치는 사례도 함께 정리.

![](/images/portfolio-2024/p18-1.webp)
![](/images/portfolio-2024/p19-1.webp)

### 논문 리뷰 — STN Neuron Model과 인공신경망을 이용한 Desynchronization (2020–2021)

뇌파를 만드는 신경 oscillator들을 수학적으로 모델링하고 그 dynamics를 딥러닝으로 다루는 연구.
**DBS**(deep brain stimulation)의 주된 기전으로 이해되는 **subthalamic nucleus (STN)** 집단의 desynchronization을 다루며,
기존에는 stimulus amplitude·frequency를 수동 튜닝해야 했던 문제에 신경망을 도입.
*Maximally Efficient Desynchronization* 에서는 두 뉴런의 spike time 차이를 `Δt_total = Δt + Δt_final` 로 두고
`Q(x,y) = −(t¹_final − t²_final) / (α∫I(t)²dt + ε)` 를 최소화하도록 control을 설계.

![](/images/portfolio-2024/p20-1.webp)
![](/images/portfolio-2024/p21-1.webp)

### 범주론 공부 (2019)

**Functor** 부터 공부하였습니다. 구조를 보존하며 Category A를 Category B로 보내는 사상으로, 대상 a,b와 morphism f를 Fa, Fb, Ff로 대응시키고 hom-set 수준에서는 `C(a,b) → D(Fa, Fb)` 가 된다는 것을, Natural Transformation으로 가기 위한 준비 단계로 정리하였습니다.
Haskell에서의 대응도 함께 보았습니다 — `class Functor f where fmap :: (a -> b) -> f a -> f b`, lifting, 그리고 type class와 ad-hoc polymorphism입니다.
이어서 **Monoidal Categories** 와 Monoid의 항등원을 공부하였고, "Haskell의 `()` = 집합론의 singleton set = 범주론의 terminal object" 라는 대응까지 정리하였습니다.

![](/images/portfolio-2024/p22-1.webp)
![](/images/portfolio-2024/p23-1.webp)
![](/images/portfolio-2024/p23-2.webp)

### 선형시스템 공부 (2019)

선형 시스템 이론을 공부하였습니다.

- 미분방정식 자체를 하나의 시스템(Solver System)으로 보는 블록 다이어그램을 정리하였습니다.
- **Time invariance** — u(t+T)에 대해 출력이 그대로 이동하면 time-invariant이고, RLC 회로를 예로 현실의 회로는 time-varying이라는 것을 보았습니다.
- 고유값·고유벡터와 geometric multiplicity, 그리고 similarity transformation에서 eigenvalue가 보존된다는 것을 공부하였습니다.
- **Generalized eigenvector와 Jordan block**, **Cayley–Hamilton 정리** `γ(A) = 0` 을 따라갔습니다.
- **Variation of Constant Formula** `x(t) = Φ(t,t₀)x(t₀) + ∫Φ(t,τ)B(τ)u(τ)dτ` 를 정리하였습니다.
- 비선형 모델의 equilibrium과 **linearization**(테일러 전개로 `ẋ = Ax + Bu`), 그리고 **Lyapunov stability** 의 정의까지 공부하였습니다.

![](/images/portfolio-2024/p24-1.webp)
![](/images/portfolio-2024/p24-2.webp)
![](/images/portfolio-2024/p25-1.webp)
![](/images/portfolio-2024/p25-2.webp)
![](/images/portfolio-2024/p25-3.webp)
![](/images/portfolio-2024/p25-4.webp)
![](/images/portfolio-2024/p26-1.webp)
![](/images/portfolio-2024/p26-2.webp)
![](/images/portfolio-2024/p27-1.webp)
![](/images/portfolio-2024/p27-2.webp)
![](/images/portfolio-2024/p27-3.webp)
![](/images/portfolio-2024/p27-4.webp)

### 군론 공부 (2019)

직사각형 퍼즐의 전체 구성도에서 generator와 **Cayley diagram** 을 읽는 것부터 공부하였습니다.
7가지 frieze pattern과 **Braid group** `B₄ = ⟨σ₁, σ₂, σ₃⟩` 의 관계식을 정리하였고, **Symmetric group** 의 원소를 cycle 표기로 나열해 r, r², f, fr, fr², e 와 대응시켜 보았습니다.
`ℤ/4ℤ` 의 코셋 분해와 normalizer(`gH ≈ Hg`), transposition 분해(`(1,2,3,4) = (1,4)(4,3)(3,2)`) 까지 공부하였습니다.

![](/images/portfolio-2024/p28-1.webp)
![](/images/portfolio-2024/p28-2.webp)
![](/images/portfolio-2024/p29-1.webp)
![](/images/portfolio-2024/p29-2.webp)
![](/images/portfolio-2024/p29-3.webp)
![](/images/portfolio-2024/p29-4.webp)
![](/images/portfolio-2024/p29-5.webp)

### 신경과학 공부 (2018) — 셈하는 뇌와 장기기억

셈하는 뇌와 장기기억을 공부하였습니다.

- **보편적 수리력** — 영아의 수 인지를 습관화(habituation)와 기대 위반(violation of expectancy)으로 측정한다는 것, 그리고 수학 교육을 거의 받지 못한 브라질 길거리 아동의 암산 사례(Nunes et al., 1993)를 보았습니다.
- **숫자의 의미** — numerosity를 공부하였고, 셈하기가 집합의 물체를 수 또는 내적·외적 기록과 일대일 대응시키는 과정이라는 것을 정리하였습니다.
- **SNARC 효과** — 작은 수는 왼손, 큰 수는 오른손 반응이 빠르고 주의도 좌/우로 치우친다는 것을 공부하였습니다. 3 이상의 수를 지칭하는 단어가 없는 부족 사례로 상징적 표상과 비상징적 표상을 비교해 보았습니다.
- **신경학적 기반** — intraparietal sulcus의 중요성을 fMRI, subliminal priming, distance effect로 확인한 연구들을 보았습니다.
- **기억** — Rundus(1971)의 초두효과와 되뇌기, Wickens(1976)의 순행간섭과 해제, 그리고 시각·청각·의미적 부호화를 정리하였습니다.

![](/images/portfolio-2024/p30-1.webp)
![](/images/portfolio-2024/p31-1.webp)
![](/images/portfolio-2024/p31-2.webp)

### '텍스트 팩토리' 연구개발 (2018) — Task-Driven / RL 관련 Deep NLP 논문 리뷰

*Episodic Curiosity through Reachability* (Savinov et al., Google Brain·DeepMind·ETH Zürich) —
episodic memory 안의 관측과 현재 관측의 도달 가능성을 비교해 bonus를 주고 `reward = task reward + bonus` 로 삼는 방식.
**Deep Dyna-Q (DDQ)** 대화 정책 학습 — real experience buffer와 world model이 만든 simulated experience buffer를 함께 쓰는
알고리즘, NLU / Dialogue State Tracker / Dialogue Policy / NLG 구성.
그 밖에 Gaussian process 기반 task success predictor, dialogue embedding, composite task의 sub-domain 자동 분해 논문까지 리뷰.

![](/images/portfolio-2024/p32-1.webp)
![](/images/portfolio-2024/p32-2.webp)
![](/images/portfolio-2024/p33-1.webp)
![](/images/portfolio-2024/p33-2.webp)
![](/images/portfolio-2024/p33-3.webp)

### '텍스트 팩토리' 연구개발 (2018) — E2E Deep NLP 시스템 구현

기존 3개 도메인 시뮬레이터를 분석해 연결하고, State Tracker를 붙이고, DDQ 환경을 구성.
`DM.next_turn()` 을 중심으로 User Simulator ↔ State Tracker ↔ Agent 의 호출 흐름
(`get_state_for_agent()` → `state_to_action()` → `add_nl_to_action()` → `register_experience_replay_tuple()`)을 시퀀스 다이어그램으로 정리하고,
학습에 쓸 (S, A, R, S′, episode_over) 튜플이 `experience_replay_pool` 에 쌓이는 구조를 확인.
슬롯 31종(address, city, cuisine, restaurantname, starttime …)과 dialogue act 11종(inform, request, confirm_answer, deny …)을 정리하고
DialogManager / StateTracker / Seq2Seq / NLU / NLG 클래스 다이어그램을 작성.

![](/images/portfolio-2024/p34-1.webp)
![](/images/portfolio-2024/p35-1.webp)
![](/images/portfolio-2024/p35-2.webp)
![](/images/portfolio-2024/p35-3.webp)
![](/images/portfolio-2024/p35-4.webp)

### '텍스트 팩토리' 연구개발 (2018) — 트위터 담화형 비정형 데이터 크롤러

코퍼스 확보를 위해 트위터 크롤러(+유튜브 크롤러)를 개발하고 수집된 한국어 대화를 분석.
- 화자 2명인 대화가 전체의 약 **90%** (14,140쌍), 모두 2턴
- 화자 3명 대화 816건 중 사실상 2명 대화가 815건 (전체의 약 5%)
- 5턴 이상 이어지는 대화는 전체의 1~2%에 불과

![](/images/portfolio-2024/p36-1.webp)
![](/images/portfolio-2024/p36-2.webp)
![](/images/portfolio-2024/p37-1.webp)
![](/images/portfolio-2024/p37-2.webp)

### '싸이버스' AI 스터디 그룹 활동 (2018)

- **PGM 발표** — Overlapping Plates(Difficulty/Grade/Intelligence, Courses·Students 플레이트), Context-Specific Independence, Tree CPD
- **TensorFlow Eager execution 발표** — CS 20SI 강의자료 기반. 선언적 그래프 방식의 디버깅 어려움(에러가 그래프 구성 한참 뒤에 보고됨, pdb·print로 디버깅 불가)을 대비로 제시

![](/images/portfolio-2024/p38-1.webp)
![](/images/portfolio-2024/p39-1.webp)

### '싸이버스' 발표 내용 (2018) — VAE / Hopfield network

**VAE** — 정보량 `h(x) = −log p(x)` 와 엔트로피 `H[x] = −Σ p(x)log₂p(x)` 부터 시작해,
`q_φ(z|x)` 가 intractable하므로 KL divergence로 근사하는 Variational Inference, 그리고 Encoder–N(μ,σ)–z–Decoder 구조.

**Hopfield network** — 연결강도는 대칭(`w_ij = w_ji`)이고 자기 자신으로 돌아가는 path가 없으며,
뉴런이 **비동기적으로** 동작할 때만 안정 상태에 도달한다(동기적으로 동시에 갱신하면 깨짐 → 앞 라인에 대기열 필요).
갱신 규칙은 `sᵢ ← +1 if Σⱼ w_ij sⱼ ≥ θᵢ, else −1`.

![](/images/portfolio-2024/p40-1.webp)
![](/images/portfolio-2024/p40-2.webp)
![](/images/portfolio-2024/p41-1.webp)
![](/images/portfolio-2024/p41-2.webp)

### '싸이버스' 발표 내용 Overview (2018)

**Template models** — `X(U₁,…,U_k)` 형태의 template variable이 여러 번 인스턴스화되는 구조
(Location(t), Genotype(person), Label(pixel), Grade(course, student)).
Dynamic Bayesian network(시간), Object-relational model(사람·과목·픽셀), Plate model(directed)/undirected 로 분류.
함께 대화형 언어이해(SLU) 서베이를 리뷰 — HMM+GMM 음향 모델을 DNN이 대체한 흐름(Hinton et al., 2012),
그리고 pre-deep-learning 시대에 SVM(intent)과 CRF(slot filling)로 나뉘어 있던 문제를
**joint multitask multi-domain modeling** 으로 하나의 모델에 담는 흐름.

![](/images/portfolio-2024/p42-1.webp)
![](/images/portfolio-2024/p42-2.webp)
![](/images/portfolio-2024/p43-1.webp)
![](/images/portfolio-2024/p43-2.webp)
![](/images/portfolio-2024/p43-3.webp)

### 인공신경망에 대한 공부 (2018)

인공신경망의 연산을 하나씩 손으로 따라가며 공부하였습니다.

- **Convolution layer** — input volume(7×7×3, pad 1), filter W0/W1(3×3×3), bias, output volume(3×3×2)까지 손으로 따라가며 입력 채널 수와 filter 채널 수의 대응, `C_out` 배의 filter tensor, 그리고 depthwise·cross-channel 개념을 정리하였습니다.
- **Torch Bilinear** — `y = x₁Ax₂ + b` 의 텐서 shape을 추적하고, `tf.nn.conv1d/2d/3d` 의 입출력 레이아웃(batch, depth, height, width, channels)을 공부하였습니다.
- **Gradient / backpropagation** — `B.backward()` 예제에서 `∂C/∂b₁ = 1/5` 를 직접 유도해 보았고, "계산 네트워크를 바꾼다 = 각 부분을 차이에 기여한 만큼 바꾼다" 로 chain rule을 직관화하였습니다.
- **multi-layer Elman RNN** — `nn.RNN(input_size, hidden_size, num_layers)` 의 입출력 shape `(seq_len, batch, ...)` 과 `(num_layers, batch, hidden)` 을 정리하였습니다.
- **Transpose convolution** — `(1,2,14,14) → (2,224,224)`, `(1,2,1,1) → (2,14,14)` 의 매핑 과정을 따라갔습니다.

![](/images/portfolio-2024/p44-1.webp)
![](/images/portfolio-2024/p45-1.webp)
![](/images/portfolio-2024/p45-2.webp)
![](/images/portfolio-2024/p46-1.webp)
![](/images/portfolio-2024/p46-2.webp)
![](/images/portfolio-2024/p47-1.webp)
![](/images/portfolio-2024/p48-1.webp)
![](/images/portfolio-2024/p49-1.webp)

### Multiple View Geometry 공부 (2018)

2D projective plane의 동차좌표 표현부터 공부하였습니다. 직선 `ax + by + c = 0` 은 `(a,b,c)` 로 쓸 수 있고, 스칼라 배가 같은 것끼리 동치류(homogeneous vector)를 이루며 이것이 P²를 구성한다는 것입니다.
이어서 central projection이 점을 점으로, 선을 선으로 보내는 projectivity이고 `x' = Hx` 로 표현된다는 것, conic이 대칭행렬로 표현되고 다섯 점이면 결정되며 접선이 `l = Cx` 라는 것까지 따라갔습니다.
마지막으로 1D projective geometry의 cross-ratio로 사진 속 가게 폭을 실제 미터로 계산하는 예제를 풀어 보았고, line at infinity와 circular point를 이용해 affine·metric 성질을 복원하는 rectification을 공부하였습니다.

![](/images/portfolio-2024/p50-1.webp)
![](/images/portfolio-2024/p50-2.webp)
![](/images/portfolio-2024/p51-1.webp)
![](/images/portfolio-2024/p51-2.webp)
![](/images/portfolio-2024/p51-3.webp)
![](/images/portfolio-2024/p51-4.webp)

### 겨울방학 딥러닝 세미나 주제 (2016)

스터디 모집과 운영을 직접 주도 — Crawling Bot 만들기(마이크로 서비스 지향, Graph DB 저장),
머신러닝·인공신경망 공부(Udacity·Coursera 강의 + Python 실습), 데이터 분석 스터디(매주 데이터 선정·분석·발표).
온라인 강의는 Andrew Ng의 *Machine Learning*(8주차 Unsupervised Learning까지)과
Geoffrey Hinton의 *Neural Networks for Machine Learning*(RNN 이해까지)을 목표로 설정.
토이 프로젝트로 **한국영화진흥원**에서 받은 1만여 건 데이터로 감독·제작사·수입사·배급사를 인자 삼아
**TensorFlow** feedforward network로 개봉 영화 관객 수를 regression 하고, 영화-제작사 관계를 웹에서 시각화.

![](/images/portfolio-2024/p52-1.webp)
![](/images/portfolio-2024/p52-2.webp)
![](/images/portfolio-2024/p52-3.webp)
![](/images/portfolio-2024/p53-1.webp)
![](/images/portfolio-2024/p53-2.webp)

### 실감형 색상 구현 (2015) — 국가기록원 연구과제

3D 모델 포맷(**.OBJ**의 vertex data·elements·grouping·render attributes, ASCII/Binary **STL** 구조와 헥스덤프 분석)을 정리하고,
색지각의 물리적 모델을 다룸 — 세 원뿔세포 반응 `S_i(λ)` 에 대해 세 단색광으로 같은 색지각을 만드는 연립방정식을 풀면
X, Y, Z 중 하나가 음수가 되어(예: 500nm에 대해 X = −0.356) 세 원색으로 재현할 수 없는 색이 존재함을 보임.
**BRDF** `f_r(ωᵢ,ωₒ) = dL_r(ωₒ)/(L_i(ωᵢ)cosθᵢ dωᵢ)` 와 반사율 방정식을 난반사 표현식으로 사용하고,
색띠 원통을 여러 각도에서 촬영한 데이터를 MATLAB **Fourier2** 모델로 커브 피팅(R-square 1).

![](/images/portfolio-2024/p54-1.webp)
![](/images/portfolio-2024/p54-2.webp)
![](/images/portfolio-2024/p55-1.webp)
![](/images/portfolio-2024/p55-2.webp)
![](/images/portfolio-2024/p56-1.webp)
![](/images/portfolio-2024/p56-2.webp)
![](/images/portfolio-2024/p56-3.webp)
![](/images/portfolio-2024/p56-4.webp)
![](/images/portfolio-2024/p56-5.webp)
![](/images/portfolio-2024/p57-1.webp)
![](/images/portfolio-2024/p57-2.webp)

---

## 졸업 작품

### 무인이동체소프트웨어전공 졸업작품 (2018) — EMG 생체신호 손동작 딥러닝 분류기

**MyoArmband** 로 남성 3명에게서 7개 클래스(natural, radial deviation, wrist flexion, ulnar deviation,
wrist extension, hand close, hand open) 동작을 4회씩 수집. 8채널 × 길이 1000의 시계열.
`scipy.signal.spectrogram` 으로 채널별 스펙트로그램을 통으로 구해 최종 데이터 형태는 `(84, 8, 129, 985)`.
- **time domain 모델**: 8ch → 1D conv → 8ch → 1D conv → 5ch → reshape → 7-d category
- **spectrogram domain 모델**: 8ch 2D map → 2D conv → 8ch → 2D conv → 5ch → reshape → 7-d category

학습 loss는 1.10 부근에서 시작해 약 1,600k step에서 0 근처로 수렴.

![](/images/portfolio-2024/p58-1.webp)
![](/images/portfolio-2024/p58-2.webp)
![](/images/portfolio-2024/p58-3.webp)
![](/images/portfolio-2024/p59-1.webp)
![](/images/portfolio-2024/p59-2.webp)

### 건축 BIM 데이터 RNN 활용 연구 (2017) — 과내 졸업작품 우수상

악보를 파싱해 `<음 A><음계>15</음계><박자>4</박자></음 A>` 형태의 시퀀스로 만들고 RNN으로 생성하듯,
IFC 건축 데이터를 파싱해 `<벽 A><위치><x>15</x><y>20</y></위치><길이>50</길이></벽 A>` 로 토큰화한 뒤
같은 방식으로 생성한다는 **IFC → RNN → Generating** 개념도.
트레이닝 변수(epoch, batch size, sequence length, sorting algorithm, activation function 등)를 바꿔가며 25개 모델을 학습하고
그 결과를 표(Chain Sort, seq length 4/6/8, batch 10, lr 0.002, relu, epoch 1000, Mean square, LSTM, hidden 150, Adam)로 비교.

![](/images/portfolio-2024/p60-1.webp)
![](/images/portfolio-2024/p61-1.webp)

---

## 대회 참가

### NAVER CLOVA AI RUSH (2020)

- **1라운드** — 워드 임베딩을 이용한 BiRNN. 댓글의 혐오 정도를 0~1 score로 예측하는 문제로, 베이스라인은 `1D Conv → BiRNN → RNN` (PyTorch), 평가는 혐오 클래스 F1-score(threshold 0.5). 데이터는 지적재산권 문제로 음절 단위 토크나이징 후 numerical indexing만 제공되고 vocabulary는 비공개
- **2라운드** — 스팸 필터링. BERT와 GPT-2의 작은 모델을 직접 구현해 사용 (`n_layers=2, n_heads=12, max_len=513, d_ff=384*4, d_k=64`, GELU, LayerNorm, decoder가 embedding weight 공유)

6015 vocab size로 재학습하며 embedding 모듈을 BERT에 어떻게 결합할지, 시퀀스를 둘로 나눠 학습할 필요가 있는지,
masking 없이 전체 길이를 쓰고 BERT를 freezing 하는 방식 등을 실험 로그와 loss 곡선으로 비교.

![](/images/portfolio-2024/p62-1.webp)
![](/images/portfolio-2024/p62-2.webp)
![](/images/portfolio-2024/p63-1.webp)
![](/images/portfolio-2024/p63-2.webp)

### '빅토리' 빅데이터 연합동아리 활동 (2016) — 데이터 경진대회 최우수상

주제: **공영자전거 활성화를 위해 어떤 곳에 스테이션을 설치해야 하는가?**
창원 누비자, 대전 타슈, 순천 온누리, 여수 유바이크 관계자 인터뷰에서 가장 중요한 입지조건이 **유동인구** 임을 확인하고,
스테이션 사용량을 예측하는 모형으로 후보지 적합성 판정 정확도를 높이는 접근을 택함.
**회귀분석**과 **10-fold cross validation** 을 사용하고 **SPSS Modeler** 로 파이프라인을 구성.
데이터는 448개 레코드 × 22개 속성 — 월평균 사용량(Quantity), 인구수·젊은층 비율·인구밀도, 공시지가, 공원 면적비율,
학교·학생·교직원 수, 시장 수, 관광지까지의 거리 등.

![](/images/portfolio-2024/p64-1.webp)
![](/images/portfolio-2024/p64-2.webp)
![](/images/portfolio-2024/p65-1.webp)
![](/images/portfolio-2024/p65-2.webp)

---

## 기타 프로젝트

### 한글 교육 어플리케이션 개발 (2014, 안드로이드) — 한국콘텐츠진흥원

`Hanguel_Sumbaggokjil` 안드로이드 앱. 오디오 녹음과 저장소 권한을 사용.
**2014 콘텐츠코리아 랩 공모전(한글상품 아이디어 부문) 장려상** 수상 (문화체육관광부·한국콘텐츠진흥원·다음카카오 주최).

![](/images/portfolio-2024/p66-1.webp)
![](/images/portfolio-2024/p66-2.webp)

### 서비스 (가칭) 'TH' 프로젝트 기획·개발 (2021–2022)

2021년 기획, 2022년 개발. 5월 경 서비스 예정.

### 웹 프레임워크 및 인프라 공부 (2020)

웹 프레임워크와 인프라를 공부하였습니다.

- **React** — 컴포넌트 구조와 렌더링에 전달되는 정보를 공부하고, 상태 끌어올리기와 Context API/Redux, ref, portal, render prop, HOC를 견주어 보았습니다. 로직은 hooks로 옮긴다는 것, 상태가 local·shared·remote·meta·router 다섯 종류로 나뉜다는 것, 그리고 Reconciliation과 Fiber, 제어/비제어 form까지 정리하였습니다.
- **React Native** — iOS와 Android를 동시에 개발하는 구조와 bridge, Animation과 Gesture Responder System, native modules, deep linking을 공부하였고, bundle identifier 변경이나 SafeAreaView height, TabBar/StatusBar height 같은 실전 HOWTO를 정리하였습니다.
- **Kubernetes** — 컴포넌트와 오브젝트, pod/node/cluster의 구분, K8s API 접근 방식과 Web UI Dashboard를 공부하였습니다. 개발 과정에서 Jenkins, skaffold, helm, telepresence, local k8s / docker-compose를 어떻게 쓰는지도 함께 보았습니다.

![](/images/portfolio-2024/p68-1.webp)
![](/images/portfolio-2024/p69-1.webp)
![](/images/portfolio-2024/p69-2.webp)

### Node 기반 웹개발 (2018) — NER을 위한 채팅 웹 시스템

개체명 인식용 데이터를 모으기 위한 채팅 웹 시스템을 구현.
수집된 개체명을 노드-링크 그래프로 시각화하는 화면과, 실제 채팅방 UI를 함께 개발.

![](/images/portfolio-2024/p70-1.webp)
![](/images/portfolio-2024/p70-2.webp)

### '직공' 서비스 창업동아리장 (2017)

사람을 중심으로 주변 가게·장소를 관계형으로 보여주는 모바일 서비스를 기획.
앱 UI 목업과 전체 화면 전이도, 4인 팀(백엔드·프론트엔드·디자인) 구성으로 진행.

![](/images/portfolio-2024/p71-1.webp)
![](/images/portfolio-2024/p71-2.webp)
![](/images/portfolio-2024/p71-3.webp)

### 토이 프로젝트

**카메라 계산기** — 손으로 쓴 수식을 카메라로 읽어 계산. 영상에서 operand와 operator를 구분하고 계산까지 수행.
MNIST 영상을 편집해 데이터를 만들고, 1자리 십진수와 `+` 연산자로 범위를 한정해 테스트
(인식 결과 예: `2, accuracy: 1.000000` / `3, accuracy: 0.988863` / `sum is 5`). OpenCV의 thresholding·contour 사용.

**변조** — 다중 주파수 메시지(`f_m1=30, f_m2=60`, `f_c1=100, f_c2=200`)의 신호·스펙트럼 비교와
원본 대비 변조 음원(`Alarm01.wav` vs `Newalarm01.wav`)의 스펙트로그램 비교.

**시위대 외침 시뮬레이션 (Agent-based programming)** — 시위에서 외침이 어떻게 이어지는지, 그리고 '맞추기(adjustment)'의 문제를 이해하는 것이 목표.
모델의 다섯 가지 요소는 **Anger**(집단의 분노 정도), **Sensitivity**(맞춤의 척도), **Density**(군중 밀도),
**Fatigue**(외침으로 인한 피로), **Sonic Area**(맞춤이 일어나는 영역). density, anger 등을 슬라이더로 조절하며 시뮬레이션.

![](/images/portfolio-2024/p72-1.webp)
![](/images/portfolio-2024/p73-1.webp)
![](/images/portfolio-2024/p73-2.webp)
![](/images/portfolio-2024/p73-3.webp)
![](/images/portfolio-2024/p73-4.webp)

