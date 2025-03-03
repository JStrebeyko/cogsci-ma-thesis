# `p r o g r e s s`

## 4.11

antivirus work

## 5.11

antivirus work, procrastination

## 6.11

digesting "The case of Croatian Wikipedia"
reach out to #wikimedia-ml

## 7.11

reach out to #wikimedia-research
reading: [Research:Interpolating quality dynamics in Wikipedia and demonstrating the Keilana Effect](https://meta.wikimedia.org/wiki/Research:Interpolating_quality_dynamics_in_Wikipedia_and_demonstrating_the_Keilana_Effect)

- interesting, a model for assessing article quality using "actionable metrics" is pretty ok in assessing article class. Cool references, found one similar
  written to a friend to suggest someone from [ZIL PAN](https://zil.ipipan.waw.pl/), two of their research interests fall close to the subject: sentiment analysis and
  credibility assessment of online content

## 8.11

- check access to ORES

  - checked, it became one of many models available at LeftWing. The problem is the API expects existing revisions and not arbitrary data, making it difficult to use with a made up dataset;

- [ZIL PAN](https://www.upf.edu/web/erinia): the way things "sound": A.Wawer
- [ZIL PAN](https://www.upf.edu/web/erinia) / [upf](https://www.upf.edu/web/erinia): fact-checking: P. Przybyła.

## 10.11

- reachout: [EDMO](https://edmo.eu/), [DEMAGOG](https://demagog.org.pl/), [SWPS](https://swps.pl/kontakt/nauka-i-badania/);
- write to the promotor;
- set a meeting with P.Przybyła;

## 11.11

- went go through arxiv on two queries: "bias detection llms" and "wikipedia llms"

Yet another 20 articles to read, with at least 2 seemingly very relevant

## 12.11

investigate the edits quantitatively: get number per date and plot, reach to article content before / after
read two most relevant articles, inc. the wiki npov / llm article (too relevant to postpone)

- early results: LLMs are very bad at detecting biased text (~61%, a little more than a coinflip)
  prepared a little presentation for tomorrow

## 13.11

meet with PP. The [notes are here](./reachout/13.11.md) (in PL)

important possible shortcomings of the current direction:

- seeking intention, which is classically very difficult;
- seems like a pretty complex expertise knowledge is needed, something LLMs out of the box do not have, and which would be necessary for zero / few shot.
- to fine-tune we would need few tousands labeled examples. the endavour would necessitate countless hours and shouldn't be performed by a single person by definition
- PP pretty optimistic about the pivot, modelling the "heatmap" of the most commonly changes parts of the article

## 14.11

### seach APD

"Wikipedia" MA

- 10 papers
- _tools_: "Wikipulse: supporting Wikipedians through article suggestion" (2016),
  _comparative research_: "“Difficult Issues” in Polish-Russian Relations in 20th and 21st Century in Polish and Russian Wikipedia" (2015),
  _reviews_: "Mechanisms involved in written language simplification: A case of Simple English Wikipedia" (2017)

"NLP" MA

- at least half of these is about neurolinguistic programming coatching paradigm
- _tools_: "Automation of Media Bias Detection - NLP Methods App\lication to Polish Media Content on Twitter" (2021)

## 15.11

### redirection genAI suggests

- [v] read [AIGen'ed suggestions AA got for me](./reachout/14.11_aa.md)

Many good:
_text classification algorithms_: Logistic Reg, SVM, Random Forest - yet all require data
_Deep Learning_: RNNs, LSTM for context considerations, CNNs - effective with word embeddings, plus transformers like BERT / GPT with finetuning, RoBERTa, DeBERTa for robustness
_Fact checking models_: "cross-lingual"?, evidence-based classigication, database verification, Knowledge Graphs
_content-based approaches_: semantic similarity, topic modelling
_contextual analysis_: Sentiment Analysis (mostly for extreme language, tho), Temporal Analysis (of spread pattern in case of fake news), fake news detection models (using textual features of contents from LIAR / FakeNewsNet datesets, metadata and propagation patterns)
_methods to improve the classification results_: ensamble learning (RF, SVM), stacking - using a meta model to combine predictions from different models
_transfer learning_: fine-tuning BERT or GPT with labeled data can drastically decrease the number of labeled examples to be given to the model during inference.
_data fusion / multimodality_: combining different modalities (text, video, image, social) for holistic approach
_challenges_: scarsity of data (robust datasets needed), evolving nature of misinformation, explainability

> "In practice, the most effective misinformation detection systems often combine multiple algorithms and methods, from traditional classifiers to advanced deep learning architectures. Fine-tuning and domain-specific training are crucial for maximizing accuracy in real-world applications."

suggestions:

- Temporal Dynamics of Misinformation Spread on Social Media
- Creation of a Dynamic Labeled Dataset for Misinformation Detection
- Evolving Misinformation Detection Models
- Limitations of Large Language Models in Misinformation Detection
- Impact of Temporal Factors on Misinformation Labeling and Detection
- Cross-Domain Temporal Misinformation Detection (platform specificity)
- Fact-checking Websites and Misinformation Spread: a temporal perspective
- Modeling the Lifecycle of Misinformation - What are key temporal milestones in misinformation lifecycle?

## 16.11

### temporal analysis

- a qualitative, human-driven one OR...
- using existing NLP toolkit of spaCy etc for SA / NER accross revisions, seeing if "the needle tweaks"
- this could be supplemented by LLM, to try to gauge who would the change benefit

### comparative analysis: LLMs on SA tasks

- benchmark a model or two on polish SA (PLLuM vs Bielik vs ChatGPT / Llama)
- use the winning model to run through the Wiki

### comparative analysis: Ukrainian Conflict in English and Polish wiki

- topological, sentiment, facts structure et al.

## 17.11 - discussing alternative paths

### model access

- [x] access to PLLuM
- doesn't seem to be ready as for Nov 2024 (source: timetable on [the website](https://pllum.clarin-pl.eu/#efects))
- ⏳ reach out to PLLuM via email.
- [x] check access to Bielik
- ✅ written on Discord -> it's on [ollama](https://ollama.com/search?q=bielik)!

### comparisons

- [x] find that one article that was doing comparative studies. [Found](https://arxiv.org/pdf/2410.04282).

### outreach

- [x] ⏳ write to AZ regarding to set up a meeting

## 18.11

### data

- [x] explore the data a bit:
- ✅ allow getting _all_ the revisions for a given article;
- ✅ create a pipeline for saving the revisions in csv files;

## 19.11

see like ai [reading](./references/00_see_like_ai.md)

## 20.11

finish [reading](./references/00_see_like_ai.md), new ideas

## 21.11

- [x] cleanup tasks
- [x] extract steps from [the reading](./references/00_see_like_ai.md) - create a [notebook](./notebooks/ashkinaze.ipynb)

## 26.11

- [x] meet the promotor: [notes](./reachout/1126_az.md) and consider pivots

## 25.11

"Winners write Wikipedia"

- create a simple pipeline
- [] get wikipedia textual content
- [] find a useful model (ollama?)
- [] create the prompting pipeline
- [] run for 6 persons

### 30.11

Continuing pivot - setting up the summarization and embedding models using `ollama` on colab.

### 1.12

- [x] send the colab to A
- [ ] include a metric, prompt engineer summarization
      pivot

---

### 8.12

- [x] improving the pipeline, cleaning the wiki data a bit
- [] inspecting the comparisons

- [] preparing to do the "rough-emotional" compression of bios (2.1)

Q: Wouldn't it be awesome to calculate the article intro vs the rest mismatch _with actual maths_???

- drawing the relation as two "spheres in the vector space"

### 241226

new take ([notebook](./notebooks/02_pivot_first_paragraph/21_is_biogram_biased_considering_this.ipynb))

- [x] create `./scripts` and move answer retrieval there

  - allows for importing variables from `.py` files, but I see no IDE support (resulting in a "[variable] not found" error)

- [x] Respond to Demagog through A. Sz

### 250101

- [x] read about [SPINACH](https://meta.wikimedia.org/wiki/Research:Newsletter/2024/November)
- it is cool see how powerful the `SPARQL` is for parsing the Knowledge Graph is;
- good work, Ms. Lam! state-of-the-art retrieval by grounding in Wikipedia a finetuned OpenLLama model;
- cool [initiative](https://diff.wikimedia.org/2024/09/23/wikidata-and-artificial-intelligence-simplified-access-to-open-data-for-open-source-projects/) by `Wikimedia Deutchland` and `Jina AI` + `DataStax`: opening wikipedia's /vectorized/ knowledge, infrastructure for providing semantic embeddings of the site's content. Beta tests in 2025!
  - WATCH [THE VIDEO](https://www.youtube.com/watch?v=r7Qbb1yuLkE);
- found a paper: [automatic quality assessment of wikipedia articles - literature revirew](https://dl.acm.org/doi/10.1145/3625286)
- [x] consider, whether it is valuable - not _that_ useful in the context of preventing mass edits. It is great for improved retrieval!
- as per Chris A., the Wikimedia ML Engineer, you cannot ask models (say, `engoodfaith`) about arbitrary text using API only. Apparently, these are containers that do the pre-processing to pass in the strings to the model
- [x] ✖ check the containers for the models on LiftWing - is is possible to edit them to accept pure text?
  - they come as a docker image. I tried extracting it using `docker save` into a `.tar`. Upon inspection besides a manifest these are just opaque blobs, unreadable. What makes sense in many ways (compression, sort of secrecy even?)
- [x] try to copy-paste paragraphs ("the rest") to a more effective model, see whether it is capable to produce a "5 adjectives only" output;
  - Roosevelt's too long to copy into [ChatGTP](chat.com)

### 250101

- [x] prepare for MLSTA screening tomorrow
- [x] Reply to WikiResearch, access to ORES? -> no way of inspecting the model and prividing it with arbitrary text because the container it is in.

### 250102

- [ ] prepare a talk with Zadrożny

## THE TASK STACK

### reachout

- [] set up a meeting with DEMAGOG(AS)

### reading

- [ ] Croatian digest
- [ ] [Wikimedia data for AI: a review of Wikimedia datasets for NLP tasks and AI-assisted editing](https://arxiv.org/pdf/2410.08918)
- [ ] ⭐ [Automatically Neutralizing Subjective Bias in Text](https://arxiv.org/pdf/1911.09709)
- [ ] ⭐ [WIKIBIAS: Detecting Multi-Span Subjective Biases in Language](https://cocoxu.github.io/files/EMNLP2021findings_WikiBias.pdf)
- [ ] [Investigating Bias in LLM-Based Bias Detection: Disparities between LLMs and Human Perception](https://arxiv.org/pdf/2403.14896)
- [ ] compare the three texts and extract methods: [Seeing like AI](./references/00_see_like_ai.md), [Automatically Neutralizing Subjective Bias in Text](https://arxiv.org/pdf/1911.09709),

### data

- group and plot revisions per rev - non-rev
- learn to identify "difficult subjects" computationally, like with wikidata topology, (cat: history, inc. Poland / Ukraine)

### model access

- [ ] find (maybe on [this SpeakLeash GH project](https://github.com/speakleash/Bielik-how-to-start)) out if I can used unquantized version of Bielik somewhere

### comparisons

- [ ] check for methods used for comparative Wikipedia studies [in this article that I found](https://arxiv.org/pdf/2410.04282).
- [ ] check polish SA datasets
- [ ] check HF's [evaluation guidebook](https://github.com/huggingface/evaluation-guidebook)

- go through NLP presentations seeking inspiration
