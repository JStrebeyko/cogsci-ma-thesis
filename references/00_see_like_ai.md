> LLMs struggled with bias detection, achieving only 64% accuracy on

> To steer models towards specific norms and values, there is a growing trend of stating high-level rules as prompts. For

> mirrors earlier debates in human-AI interaction and beyond. For instance,Lucy Suchman’s 1987 “Plans and Situated Actions” frameworkcontrasted predetermined procedures derived from universal principles (“plans”) with context-dependent actions based on concrete circumstances (“situated actions”). She argued that AI systems execute plans, while humans perform situated actions. This distinction relates to James Scott’s [41] concept of _“seeing like a state”_ — the idea that the large-scale plans of centralized authorities often break down when faced with complex, local realities.

### research categories

> We position our work in the context of Wikipedia neutrality research (2.1), automated moderation of Wikipedia (2.2), and broader conversations around the role of general-purpose LLMs in community moderation (2.3).

### NPOV

> Specifically, NPOV is described by a set of principles (...) Avoid stating opinions as facts; Avoid stating seriously contested assertions as facts; Avoid stating facts as opinions; Prefer nonjudgmental language; Indicate the relative prominence of opposing views.

### NPOV is difficult in practice

> The broader NPOV policy encompasses various complex assessments (e.g., covering viewpoints in proportion to their prominence in reliable sources).

> Third, Wikipedia’s NPOV has a unique tension: while clearly-articulated and well-documented in theory, it is complex in practice

### why is the research interesting?

> Evaluating LLMs on Wikipedia’s NPOV policy is an interesting test case of model abilities for three reasons.

interesting, because

1. LLMs used in very different contexts
2. non-neutrality is nuanced, goes beyond literal meaning
3. tension between too easy it is to articulate N Pov and how complex it is to implement

### why is the research timely?

> LLMs excel at zero-shot annotation

> Second, Wikipedia has historically used automated moderation tools [52], but there are contentious internal debates about the use of ChatGPT [14].

### Why such a weak dection capabilits?

> Analysis of LLM rationales and errors suggested LLMs relied (sometimes to a fault) on simple heuristics like the presence of a highly subjective adjective.

> Because LLMs are explicitly trained for natural language generation, they may be more effective at generation than detection.

### metrics

> (...) moderators indicated models should have recall and precision above 70%.

(reddit rule-of-thumb)

### appealing generation

> AI models arguably applied NPOV more faithfully than human editors

### models

> We chose these models because GPT 4 is state-of-the-art, ChatGPT 3.5 is widely used, and Mistral-Medium is from an open-source developer.

> high-recall but low-precision editing.

> Models exhibited biases that persisted across prompts.

> Understanding model idiosyncrasies is crucial. It is not clear that, when a new model appears on the scene, we will know what its priors are.

> For model builders, we suggest several actionable steps to improve detection and generation abilities: Retrieval-augmented generation (e.g., incorporating Wikipedia Talk page conversations to simulate editors’ community knowledge) or multi-agent systems [15, 17] (simulating Wikipedia-style debates) may enhance detection capabilities. Fine-tuning models on expert feedback can increase alignment with domain specialists. Refining Constitutional AI to emphasize preserving original text may improve revision precision.

#### detection easier on inappropriate tasks:

> ChatGPT largely agrees with both crowds and experts when detecting inappropriate words in Reddit comments

### dataset

> While NPOV is a set of multiple rules, the WNC consists of edits that violated a particular subset of NPOV—biased language (framing, epistemological, and demographic bias).

> rules, the WNC consists of edits that violated a particular subset of NPOV—biased language (framing, epistemological, and demographic bias).

> Number of edits for each topic. The data consists of rewrites of biased edits.

even split between biased/non biased from each of article category (STEM, Culture, Geography....)

### experiment

> (...) conducted a multi-model prompt experiment (N = 5,348 annotations) where the task was to classify if a given Wikipedia edit was biased or neutral.

> 3.2.1 Factor 1: Definitions Provided (minimal / NPOV / NPOV-Scoped, where additional bias information is provided)
> 3.2.2 Factor 2: Examples Provided. (few-shot)

### prompts engineering

Used a single prompting technique and DSPY for insignificantly better results

- perhaps these could be improved with better techniques?

> (...) use with chain-of-thought (CoT) reasoning and DSPy’s ‘BootstrapFewShot’ module. In CoT, a model is instructed to reason step by step to get to its answer, which can improve performance [50].

### further directions

...bigger models

> Notably, the largest model did the best. Perhaps even larger models would do better.

...finetuning

> Alternatively, low performance may be due to a more fundamental aspect of LLMs. For example, it may be that LLMs effectively ‘over-learn’ a notion (e.g., neutrality) from broad web corpora, and specializing this notion to a community’s norms requires changing a model’s parameters. In any case, our study suggests two future directions. First, fine-tuning may improve performance. However, fine-tuning may also risk overfitting [26].

...rag, conversationr retrieval

> Another approach involves more advanced use of retrieval-augmented-generation (RAG). Can incorporating conver sations from Wikipedia Talk pages or other Wikipedia data simulate the community knowledge that editors have?

...multi-agent (mentioned in the context of generation, but who knows)

> Perhaps a multi-agent system simulating ‘debates’ [15, 17] can better apply nuanced rules than an individual agent in isolation.

> → Improving Detection: Retrieval-augmented generation (integrating Wikipedia’s Talk pages) that provides models with additional context for labels or multi-agent systems (simulating Wikipedia-style debates) may enhance norm violation detection capabilities.

...automatic triggering of neutralizing edition logic by scanning discussion pages for traces of neutrality violitions

> For instance, models could monitor Wikipedia Talk pages for comments suggesting NPOV violations. Based on automated triggers, these models could then offer neutralizations.

... other types of NPOV violations

... more models to be able to generalize better

... better prompting

> Fifth, no prompt experiment can rule out that some (untested) prompts may have worked better. Though we explored a diverse range of prompting strategies. Our main experiment centered around providing LLMs with the text of NPOV, which is a reasonable prompt strategy. We then systematically ablated examples and definitions. Subsequent experiments incorporated chain-of-thought reasoning, LLM-generated rationales, and LLM self-generated prompts. We encourage future research to explore additional techniques, such as more sophisticated few-shot example selection and retrieval-augmented generation.

... wider context:

> Sixth, our dataset is noisy: Edits appear without the full article context

### why improving detection is needed?

> LLMs’ poor detection performance limits their usability. (...) Therefore, effective detection would have amplified the usability of effective generation.

### analysis

graphical:

> (a) Accuracy by models and conditions. Error bars are 95% CIs. (b) Proportion of edits predicted to be biased. Error bars are 95% CIs.

> Across zero-shot conditions, ChatGPT 3.5 predicted that 83% of classifications were biased but across few-shot conditions, ChatGPT 3.5 predicted 59% were biased, two-tailed permutation test p < 0.001.

### the risk of using llms for wiki study

> LLMs are trained on Wikipedia data, so this poor performance existed despite a potential data leakage.

### techniques

- [ ] two-tailed permutation testing for cross-condition comparison
- [ ] two-tailed binomial test for assessing statistical significance of patterns of model-specific differences
- [ ] TF-IDF logistic regression for predicting accuracy given words in explanation
- [ ] two-tailed binomial tests and conditional logistic regressions for comparing responder's rating responses between conditions

### further reading

Wikipedia Neutrality Corpus
please check

- its format & edit article's content length (context)
- could it be easily translated
- could it be used for fine-tuning

task-specific models of neutralization: 34, 37
two datasets: 34, 37
npov: 36, 46
automatic moderation: 53 (please check)
text metrics - LIWC: 33, similarity to prompts with SBERT: 38
by Orme’s rule of thumb: 31

NPOV

```md
# B.4 Detection: LLM Bootstrapped Prompt (NPOV-Scoped)

This prompt format follows DSPY’s Chain of Thought implementation.

Note: This prompt format follows DSPY’s Chain of Thought implementation.
Act like an expert Wikipedia editor. Classify if this Wikipedia edit is neutral or biased.
A Wikipedia edit is biased if it violates Wikipedia's neutral point of view (NPOV) policy.
Neutral point of view policy:

- Policy 1: Avoid subjective and judgmental language. Word choice should use a disinterested,
  impartial tone and avoid language that sympathizes with or disparages the subject.
- Policy 2: Avoid phrasing that implies how 'believable' a statement is. Word choice can imply
  how believable the author considers a statement to be.
- Policy 3: Avoid stereotypes. Word choice can imply stereotypes about gender, race or other
  demographic categories.
- Policy 4: Avoid presenting opinions as facts. Opinions should be attributed to a person, a group of people who hold the opinion, or where appropriate, described as a widespread view.
  Note that even if it slightly violates the NPOV policy, it is considered biased and not neutral.

---

Follow the following format.
Edit: edit
Reasoning: Let's think step by step in order to ${produce the answer}. We ...
Answer: neutral or biased

---

Edit: hydrogen pipelines are unfortunately more expensive than even long-distance electric lines.
Reasoning: Let's think step by step in order to produce the answer. We first identify if the edit uses subjective or
judgmental language. The word "unfortunately" introduces a subjective viewpoint, implying a negative aspect of
hydrogen pipelines compared to electric lines. This word choice violates Policy 1 by not maintaining an impartial tone.
It also subtly presents an opinion
as a fact, which is against Policy 4, as it does not attribute this viewpoint to a specific source or
acknowledge it as a perspective rather than an objective truth. Therefore, the edit does not adhere to the neutral
point of view policy.
Answer: biased

---

## (...Omitting more examples for space...)

Edit: {EDIT_HERE}
Reasoning: Let's think step by step in order to
```

...also check:
Detection: LLM Bootstrapped Prompt (NPOV)

```md
# B.6 Detection: LLM Auto-Generated Prompt

This prompt format follows DSPY’s Chain of Thought implementation.

Please meticulously evaluate the content of the indicated Wikipedia edit. Our aim is to determine its alignment with the
principles of neutrality and objective information presentation. An edit falls under "neutral" if it maintains or improves
the essential impartial perspective of the topic by offering well-referenced data, balanced interpretation, and avoids
espousing a specific ideology, viewpoint, or favoritism towards any subject matter or entity portrayed. Conversely,
categorize an edit as "biased" when it skews towards advocating a singular perspective: conspicuously highlighted
by the use or omission of particular terminologies, incorporation or deletion of facts that possess agenda-driven subtexts,
or through nuanced alteration playing to subjective opinions, ideologies, or non-verifiable anecdotes that conspicuously
colour the narrative away from evidentiary neutrality. In making your categorization, lavish detail on linguistic nuances,
presentation styles, and contextual frame shifts evoked by the edit, analyzing its departure from or congruity to
non-partisan, factual, information dissemination aimed at fostering an informed readership.
...
```
