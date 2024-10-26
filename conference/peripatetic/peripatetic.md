# Dynamics at the verge of Knowledge: good intentions, bad actors and computational means of distinguishing the two on Wikipedia

## Abstract

The talk offers an end-to-end perspective into Wikipedia's article revision process and the challenges it faces, especially in the advent of Generative AI. We will set up the stage with a primer into the platform's features that make is so valuable for natural language processing (NLP) needs. Useful as it is, though, Wikipedia's founding assumptions bring certain risks to the table we need to address. To get a better grip on the "how's" and "why's", we will deep dive into the harm that's already been done (and fixed!) in the past. What connects House Representatives, Indian Enterprenours and the right-wing bias in Croatian politics? With our imagination stimulated, we will examine the tools Wikimedia Foundation has at its disposal to flag ill will and ward off malicious revisions, vandalism and manipulation attempts. Which quirks of the platform make these efforts insufficient? The future is automatic, so our eyes will turn towards the next big thing. In search of neutrality guardrails, preventing us from drifting too far-off, we will explore the ways in which Large Language Models can aid the case. What's their promise? What could go wrong?

# table of contents, slide two

This talk is dedicated to Wikipedia, the unique access to knowledge it offers and the very practical challenges it faces because of it. My aim is to raise about certain things I noticed, the awerness, share themes I found interesting during my research and not to bore you too much, perhaps stir some discussion.

As you see, the talk has a dialectical structure of a thesis, so the good, an antithesis, so its shadow, and a synthesis, so a way in which the tensions is mediated.

I will be talking about a circle and a triangle today.
Please interrupt me as you see fit, so this doesn't feel like a complete rant.

# intro - the "why", slide one

Hello, my name is Jakub Strebeyko

I am a researcher at the University of Warsaw. My academic background is in Applied Social Science and, separately, in Cognitive Science. Besides that, I have nearly 10 years of professional experience as a software engineer, during the most time of which I have been dealing with technicalities of the web. The reasons I am here, though, are first and foremost, personal.

As a person born in the 90s, I had both the priviledge of living in the world before the internet and seeing it boom through my adolescence. I, as many here, have seen it take over the world, reshaping the way we communicate and laisure. Drawing from it's virtually infinite pool of possibilities has arguably become one of the central skills for a city-dweller. The access to knowledge was unparalelled, and it had a profoundly democratizing quality to it. For many (me included), it turned out to have life-transforming properties. For us, it was a place to meet at, learn and exchange, freely.

One of the central symbols of this age was Wikipedia, an online encyclopedia created by the users. Curated by volunteers, it was a common good everybody could take from and contribute to, as long as they followed community guidelines.

# Wikipedia intro, slide 3

Wikipedia as we know has been around since 2001, but the idea is dates much back. The idea for an open-access, community-curated encyclopedia that would offer high quality, comparable to the one of commecial, for-profit offerings dates way back. The earliest known proposal for an online encyclopedia was made by Rick Gates in 1993. He is best known as an organizer of the so-called Internet Hunts, a contest with 10 questions, all of which Gates ensured could be answered using only pre-www resources. He was a visionary, one of the "internet pioneers", an advocate for open knowledge, even in the pre-internet era.

Unfortunately, many of references of his activity are being lost, an interesting thing in itself. The reason I did not include his picture here is that I couldn't find any, but they could be lost in a sea of pictures of Richard William Gates III. He's a political consultant and lobbyist who pleaded guilty to conspiracy against the United States for making false statements in the investigation into Russian interference in the 2016 United States elections. (this actually ties in very nicely, but not gonna spoil it)

The other guy here Richart Stallman, a well known hacker and one of the open source software movement founders. He's sort of an icon in the linux world, having created GNU Operating system and the idea of "free" (not as in "zero-price", but as in "freedom") software and the necessary license scaffolding work, the "copyleft" licenses. They allowed for transfer of work between the open-source creators and contributors to consumers. He's also credited with proposing in 1998 the concept of a free-as-in-freedom online encyclopedia (as opposed to merely open source). Stallman's concept specifically included the idea that no central organization should control editing.

Originally, Wikipedia has been a complementary project to Nupedia, an encyclopedia entries of which where to be authored solely by experts in their fields and submitted through a formal, 7-steps process.

Wikipedia's role in its parent company, Bomis, business, was to serve as a "draftboard" for Nupedia - its less strict format allowed for more discussions and collaboration, which was facilitated by the platform's live-editing features.

Nupedia offered 5 languages and 25 finished articles by the end of September 2003, when it was discontinued. In the meantime, Wikipedia quickly overtook its predecessor, becoming both draft space and home for the polished final product of a global project in hundreds of languages, inspiring a wide range of other online reference projects."

# stats, slide 4

> As of 23 October 2024, there are 6,899,855 articles in the English Wikipedia
> 14,000 new articles every month (as of January 2024)
> Steady increase since 2006 "at roughly 1 gigabyte of (compressed) text added per year"
> This implies that as time progresses, proportionally more content is added to existing articles rather than new articles, and that Wikipedia has maintained the same persistent rate of growth throughout since the 2010s. In other words, over time, the average article size is growing faster than the number of articles.
> (https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia)

332 languages actively developed

> https://en.wikipedia.org/wiki/List_of_Wikipedias

# NLP reaons slide

The are features of wikipedia that make it a great resource for natural language processing tasks. Ultimately, that's a lot of of text of high quality texts from different domains. They are in different languages, adhering to a fixed, encyclopedic style. Thanks to projects like WikiData, they become more and more structured over time, making it easier to consume in automatic means.

- coverage of all sorts of topics, creating a rich dataset of textual data
- variety of languages, all catering to different linguistic and cultural backgrounds. Allows to explore various language patterns, idioms and expressions.
- quality, due to editorial process - well written and (mostly) accurate
- real world application case relevant for topic modelling and information retrieval
- anonimity allows to study communication patterns without risk of revealing sensitive informations about individuals
- available and accessible - its open nature and the API allow to easily obtain the content
- multimodality by offering, besides textual data also images, videos and audio great for multimodal / multitask scenarios
- temporal dimmension, offering insights into language and sentiment evolution

As we see, there seems to be certain feedback loop - wikipedia makes it accessible to study language, while the scientific achievements help to improve wikipedia content. Let's start small.

# the bots, slide 5

Automatic software, which I will refer to as bots here, helped to expand wikipedia in quantitative means from its early stages.

Rambot - automated program

- created in October 2002, Derek Ramsey
- from October 19 to 25 it created stub articles for every missing county, town, city, and village in the United States, based on free information from the United States Census of 2000
- increased the number of Wikipedia articles by 33,832[157], 40%, leading to a record relative increase of article number (in comparison to previous year) of 390%
- In "The Wikipedia Revolution", Andrew Lih called it "the most controversial move in Wikipedia history"

The other case is even more interesting. Who has heard about Cebuano language?
I certainly didn't until recently. Little did I know - it is the second biggest of the all wikipedia language projects!

# Cebuano

- Austronesian dialect used primarily in southern Philippines
- second most spoken language in philippines
  > Cebuano Wikipedia does not appear to be widely used in the Philippines; as of March 2021, 90 percent of Wikipedia views from that country were directed at English Wikipedia, with 5 percent going to Tagalog and 3 percent to Russian Wikipedia. About 30 percent of Cebuano Wikipedia views come from China, 22 percent from the United States, and only about 11 percent from the Philippines (roughly the same number as from France). (https://en.wikipedia.org/wiki/Cebuano_Wikipedia)
- second largest Wikipedia with over 6,116,937 articles
- very few active users - most of its content (circa 99%) was created by bots, automatic programs, most notably

Ljsbot

- according to author, Sverker Johanson, it uses remote databases and websites and compiles them to article, makes 10,000 articles per day
- author of milion-th article in Swedish wikipedia, which made it the second largest wiki project, over 8% of all wikipedia content in 2014

- stubs seem innocent, help to map the known

# Ljsbot

- Sverke Johansson
- according to its user wikitalk page, authored over 17 millions of articles in Wikipedia
- It's author, Sverke Johansson, holds physics PhD (particle physics, experiments at CERN), but is also very deep into linguistigs, authored a book "Dawn Of Languages: how we got to talk"
- criticised for "lack of human touch" and little meaningful content.
  > Johansson countered attacks on his methods by appealing to problems of gender bias on Wikipedia, noting that if the bot does not write articles, "otherwise they're mainly written by young, white, male nerds and reflect male interests.
  > https://en.wikipedia.org/wiki/Lsjbot

> https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia

# growth speed

> (...) such as the Cebuano-language edition of Wikipedia, as well as the Swedish-, Dutch- and the Waray-language editions,(...)

So yes, these were are all good, perhaps a little bit controversial ways in which the Wikipedia grows. Please, hold this notion in mind, the automatized means of editing the data available wil be usefull very soon.

The examples given are made in good faith, but not all edits serve to ground common understanding in truth.

# Hoaxes

- entirely made up person - a polish communist revolutionary, an associate of Ernest Hemingway.
- linking to 17 other articles
- 15 months

# prey

it is an easy prey

- wikipedia is open, meaning anyone can edit articles

But, more over, it is very tasty treat. Many of the reasons why you can guess yourselves - it is just sooo popular.

- wikipedia is "source of truth", used in education

# the other "why"

knowledge panel and SEO

# wikiscanner

Virgil Griffith, a caltech student

- august 2007
- He said he wanted to, "create minor public relations disasters for companies and organizations I dislike (and) to see what 'interesting organizations' (which I am neutral towards) are up to."[57] He also wanted to give Wikipedia readers a tool to check edits for accuracy[56] and allow the automation and indexing of edits.
- Most of the edits were minor or harmless, but the site also allowed to discover the most controversial and embarrassing instances of conflict of interest edits.

proven than,

- Microsoft tried to cover up the XBOX 360 failure rate
- Apple edit Microsoft entries, adding more negative comments about its rival
- Bill Gates revenge? Microsoft edits Apple entries, adding more negative comments about its rival
- The Vatican edits Irish Catholic politician Gerry Adams page
- In the 9/11 Wikipedia article, the NRA added that “Iraq was involved in 9/11”
- Exxon Mobil edits spillages and eco-system destruction from oil spillages article
- FBI edits Guantanamo Bay, removing numerous pictures
- Oil company ChevronTexaco removes informative biodiesel article and deletes a paragraph regarding fines against the company
- Scientology removes criticism and negatives article from Scientology page
- Al Jazeera TV station adds that the foundation of Iraq was just as bad as the Holocaust
- Amnesty International removes negative comments
- Dell Computers deletes negative comments on customer services and removes a passage how the company outsources work to third world countries
- MySpace removes paragraph when their website was hacked
- EA Games deletes whole paragraphs of criticism about employment practices and business methods
- Dog breeding association deletes whole paragraphs about fatal attacks by dogs on humans
- US Republican Party changes the "Post-Saddam" section of the Baath Party article to a different account of the war, changing the language from "US-led occupation" to "US-led liberation"
- Fox News removes all controversial topics against the network from the Fox News page
- News of the World deletes a number of criticism against the paper
- Nestle removes negative comments on its business practices from its page
- UN address calls journalist Oriana Fallaci a racist ‘prostitute’
- Portuguese government removes entries about Prime Minister’s scandals
- DieBold, the company that controversially supplied computerised polling stations in the US elections, removes numerous paragraphs with negative comments
- Walmart removes criticism of outsourcing work. The retailer also changes negative paragraphs of underpaid workforce
- Sony removes harmful paragraphs against blu-ray systems
- Someone at Reuters calls Bush “a mass murderer”
- Coca Cola removes negative content about its effects
- British Conservative Party removes negative references of its MPs and deletes paragraph of the party’s old policies
- US University adds the “prestigious” adjective to its page
- Boeing edits from “Boeing is a leading American aircraft and aerospace manufacturer” to “Boeing is the leading American aircraft and aerospace manufacturer”
- MSN Search is “a major competitor to Google”. That’s what MSN added to their page
- BBC changes Blair's drink from coffee to vodka and his workout from the gym to the bedroom. Someone from the BBC also changes Bush’s page, changing the name from ”George Walker Bush” to “George Wan\*\*\* Bush”
- Someone from The Guardian edits the Wikipedia page of rival newspaper The Times. Originally in the article it is said that The Times sells more than The Guardian. After the edit, The Guardian sells more.
- a Vatican computer was used to remove references to evidence linking Sinn Fein leader Gerry Adams to a decades-old double murder.
- Someone at the US Democratic Party's congressional campaign committee changed a description of conservative radio talk show host Rush Limbaugh to replace "comedian" with "bigot" and dub his listeners "legally retarded."
- A Republican Party computer purportedly was used after the US invasion of Iraq to change "occupying forces" to "liberating forces"
- Wikiscanner also identified a BBC computer as being used to change US President George W. Bush's middle name from "Walker" to "Wanker." A computer belonging to Reuters news service is listed as adding "mass murderer" to a Wikipedia description of Bush.

- "The most shameful Wikipedia spin jobs" Wired user poll
  On December 18, 2007, Fortune magazine mentioned the use of WikiScanner in the 96th of its list of the "101 Dumbest Moments in Business", saying, "A Washington Post employee is found to have changed a reference to the owner of a rival paper from Philip Anschutz to Charles Manson, while someone at The New York Times added the word 'jerk' 12 times to the entry on George W. Bush."

Jimmy Wales, co-founder of Wikipedia, spoke enthusiastically about WikiScanner, noting that "It brings an additional level of transparency to what's going on at Wikipedia"[13] and that it was "fabulous and I strongly support it."[29]

# croatian case

project capture, meaning not a certain article nor discussion, but a whole language wiki project has been overtaken
The editors, who seemed to know each other personally and sharing same political sentiments coordinated and moved strategicly

throughtout a decade, altered or even re-written hundreds of articles on country's history, politics and many other topics
involving right-wing, ultra-conservatist bias to the content

**context**

- Serbo-Croatian Wikipedia’s community was split up into Croatian, Bosnian, Serbian, and the original
  Serbo-Croatian wikis starting in 2003. Although speaking the same language (and perhaps writing it with different scripts), the articles content started to diverge apart, with HR ones taking on a very specific narrative.

distorted the content (...), abused power, and systematically obstructed otherwise
accepted global Wikipedia community practices (...) through sock-puppeting (...) - using inauthentic online identities for the purpose of deception.

it would soon a) branch out from the original topic; b) turn ad hominem; and c) become flooded with irrelevant comments and information.

disinformation and bias

**bias**
by using well-known disinformation tactics, including
relativisation of facts, whataboutism, discreditation of other participants and outright bullying

Framing bias: Also known as emulated neutrality. Giving equal weight to a range of competing claims,
presenting questionable claims side by side with factual truths, or contextualising facts in a way that
misleads readers.

Source bias: Citing non-neutral sources without disclosing their affiliation and/or
providing dubious sources to back up claims presented in the article. Emulated neutrality regularly relies
on this type of bias.

Selection bias: Selectively including and excluding content regardless of its notability
or topical relevance in order to affect the reader’s perception.

The evaluation has shown that Croatian and Serbian language Wikipedia, in 62.5% and 39.1% of
cases, respectively, avoid informing their visitors in the introductory paragraph that the person
they’re reading about is a convicted war criminal who comes from the same ethnic group. (Google Knowledge Panel)

- Whitewashing "our people" was a standard
- relativisation of sources, selective inclussion and omissions and structural changes to the articles
- teaching convtroversy - putting very different estimates (one well documented, one from a questionable source) side by side, relativising the outcome
- introducing dismissive / political labels as actual encyclopedia entries

**governance**
Administrators and sock-puppeteers
The group has been using its on-wiki positions of power to attract new like-minded contributors, silence and ban dissenters, manipulate community elections and subvert Wikipedia’s and the broader movement’s native conflict resolution mechanisms.

Very active in discussions, but going silent in crucial moments to avoid detection

**results**
Political revisionism and manipulation of facts in WikiHR was wide and went on for a decade. Research showed substantial influence on the younger generation. Youth are the main consumers of social media and the main target of misinformation campaigns.

Google’s Knowledge Panel, an info box that appears on the top of the list of
search results. In that sense, an introductory part of any Wikipedia article is by far the most desirable
target for any manipulation of facts.

For it to work, you need a lot of editions and a long period of time.

**as an example**
The case of Croatian language Wikipedia demonstrates that there
could be similar attempts of project capture in other languages as well.
A more resourced and better-organized attempt could be harder to detect and eventually reverse.

Wikipedia is pretty resilent against the pressures from autocratic regimes, but not from taking the project from within

**detection**
The report analysed articles of 32 widely known people from the time and compared the way their biographies are shown.

Identifying disinformation, which usually entails demonstrating intent, on Wikipedia as such is
substantially more difficult.

certain bias in how how some facts are contextualized within wiki projects is unavoidable and part of platform's genome
At the same time,

> bias is usually found, discussed and ultimately corrected by the Wikipedia volunteer communities.
> If may of these biased facts stay on and do not get corrected, it stops being NPOV and contributes to represetation of facts that is part of disinformation campaign

One of solutioons suggested within the report was "developing collaborative solutions that would help monitor communities globally to timely identify major ideological shifts in projects."

# what can be done?

With hundeds of thousands of edits daily, there is simply not enough trained volunteers to be able to assess the incoming tsunami of content

Wikipedia has numerous systems in place to help.

Most of them have been part of ORES (Objective Revision Evaluation Service), a set of ML utils to help quickly assess drafts, articles and revisions
Here we see a typical flow in case of revisions. A constant flow of edits comes in here and each gets asssinged one of three available labels.

#

## Why automatic?

**mention of Wikipedia's scale and governance and feasability of quantitative, human-driven assessment of changes**

## the troubles with automatic detection

1. theory - common definition of unwanted changes
2. practice - why flag (and not block - human in the loop), what to flag

## what Wikipedia currently uses

[!!!]**describe the models**
[!!!]**their shortcomings**

## the future - could LLMs help us monitor revisions?

**LLM features that make them useful in research**

## existing methods **WIKIPEDIA - CURRENT METHODS**

- how does it work - the beauty of the public edits
- why was it researched - the wealth of language knowkedge
- the API
  > todo: examples of great wikipedia research in few domains
- the raise of the automatic research methods: enganglement in LLM datasets.
  > due to it being neutrally formattd
