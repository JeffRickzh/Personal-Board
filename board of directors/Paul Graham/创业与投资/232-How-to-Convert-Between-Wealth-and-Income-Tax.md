232 How to Convert Between Wealth and Income Tax

May 2026

How do you convert between wealth and income tax? If a government imposes a wealth tax of 1%, what’s the equivalent in income tax?

It’s clear from the way most politicians talk about the subject that they not only don’t know the answer, but don’t even realize there’s such a question.

In fact the conversion rate between them is about 20. A wealth tax of 1% is equivalent to an income tax of 20%.

To convert between wealth and income tax rates, you have to divide by the rate of return on capital. The conversion rate of 20 comes from assuming that the risk-free rate of return is 5%. Historically that’s an optimistic assumption. 4% might be more realistic. But 5% will do. [833]

If we run through an example it will be clear how this works. Suppose you have $100, you’re getting a 5% rate of return on this capital, and there’s a 20% income tax. The 5% rate of return means at the end of one year your $100 has made you another $5. But you have to pay 20% of that, or $1, in income tax, so your after-tax income is $4. At the end of the year, after paying taxes, you have $100 + $4 = $104.

Now suppose instead of a 20% income tax, there’s a 1% wealth tax. At the end of the year your $100 has made you another $5, as before. But that year you had to pay 1% of your $100, or $1, in wealth tax. So at the end of the year you have $99 + $5 = $104.

Each 1% of wealth tax is equivalent to 20% of income tax.

It’s clear that politicians don’t get this from the way they talk about a “mere 1%” wealth tax. None of them would speak of adding a “mere 20%” to the income tax rate, even though that’s mathematically the same thing. [834]

Politicians understand that an additional 20% income tax would be a lot. And indeed a US state that added 20% to its top income tax rate would have extraordinarily high taxes.

Currently the country with the highest marginal income tax rate is Denmark, at 60.5%. The top US federal tax rate is 37%, and the median state income tax rate is Oklahoma’s, which is 4.75%. So in the median case, a state adding an additional 20% in income tax would have a total marginal tax rate of 37% + 4.75% + 20%, or 61.75%. [835]

In the median case, US state politicians talking about adding a “mere 1%” wealth tax are talking about causing the residents of their state to have the highest taxes in the world. That’s not the sort of decision you make lightly.

That’s why I think few politicians currently understand how to convert between wealth and income taxes. You can tell from the way they talk about the subject that they don’t understand the momentousness of what they’re proposing. But I’m optimistic that we can teach them. The answer’s not hard to understand, once you realize the question exists.

Thanks to Trevor Blackwell, Jessica Livingston, Carolynn Levy, Jon Levy, Alex Tabarrok, and Harj Taggar for reading drafts of this.

------------------------------------------------------------------------

[1] . Viaweb at first had two parts: the editor, written in Lisp, which people used to build their sites, and the ordering system, written in C, which handled orders. The first version was mostly Lisp, because the ordering system was small. Later we added two more modules, an image generator written in C, and a back-office manager written mostly in Perl. In January 2003, Yahoo released a new version of the editor written in C++ and Perl. It’s hard to say whether the program is no longer written in Lisp, though, because to translate this program into C++ they literally had to write a Lisp interpreter: the source files of all the page-generating templates are still, as far as I know, Lisp code. (See Greenspun’s Tenth Rule.)

[2] . Robert Morris says that I didn’t need to be secretive, because even if our competitors had known we were using Lisp, they wouldn’t have understood why: “If they were that smart they’d already be programming in Lisp.”

[3] . All languages are equally powerful in the sense of being Turing equivalent, but that’s not the sense of the word programmers care about. (No one wants to program a Turing machine.) The kind of power programmers care about may not be formally definable, but one way to explain it would be to say that it refers to features you could only get in the less powerful language by writing an interpreter for the more powerful language in it. If language A has an operator for removing spaces from strings and language B doesn’t, that probably doesn’t make A more powerful, because you can probably write a subroutine to do it in B. But if A supports, say, recursion, and B doesn’t, that’s not likely to be something you can fix by writing library functions.

[4] . Note to nerds: or possibly a lattice, narrowing toward the top; it’s not the shape that matters here but the idea that there is at least a partial order.

[5] . It is a bit misleading to treat macros as a separate feature. In practice their usefulness is greatly enhanced by other Lisp features like lexical closures and rest parameters.

[6] . As a result, comparisons of programming languages either take the form of religious wars or undergraduate textbooks so determinedly neutral that they’re really works of anthropology. People who value their peace, or want tenure, avoid the topic. But the question is only half a religious one; there is something there worth studying, especially if you want to design new languages. More Technical Details Japanese Translation Turkish Translation Uzbek Translation Orbitz Uses Lisp Too How To Become A Hacker A Scheme Story Italian Translation * * * You’ll find this essay and 14 others in Hackers & Painters.

[7] . Macros very close to the modern idea were proposed by Timothy Hart in 1964, two years after Lisp 1.5 was released. What was missing, initially, were ways to avoid variable capture and multiple evaluation; Hart’s examples are subject to both.

[8] . In When the Air Hits Your Brain, neurosurgeon Frank Vertosick recounts a conversation in which his chief resident, Gary, talks about the difference between surgeons and internists (“fleas”): > Gary and I ordered a large pizza and found an open booth. The chief lit a > cigarette. “Look at those goddamn fleas, jabbering about some disease > they’ll see once in their lifetimes. That’s the trouble with fleas, they > only like the bizarre stuff. They hate their bread and butter cases. That’s > the difference between us and the fucking fleas. See, we love big juicy > lumbar disc herniations, but they hate hypertension….” It’s hard to think of a lumbar disc herniation as juicy (except literally). And yet I think I know what they mean. I’ve often had a juicy bug to track down. Someone who’s not a programmer would find it hard to imagine that there could be pleasure in a bug. Surely it’s better if everything just works. In one way, it is. And yet there is undeniably a grim satisfaction in hunting down certain sorts of bugs. Postscript Version Arc Five Questions about Language Design How to Become a Hacker Japanese Translation * * *

[9] . Realizing that much of the money is in the services, companies building lightweight clients have usually tried to combine the hardware with an online service. This approach has not worked well, partly because you need two different kinds of companies to build consumer electronics and to run an online service, and partly because users hate the idea. Giving away the razor and making money on the blades may work for Gillette, but a razor is much smaller commitment than a Web terminal. Cell phone handset makers are satisfied to sell hardware without trying to capture the service revenue as well. That should probably be the model for Internet clients too. If someone just sold a nice-looking little box with a Web browser that you could use to connect through any ISP, every technophobe in the country would buy one.

[10] . Security always depends more on not screwing up than any design decision, but the nature of server-based software will make developers pay more attention to not screwing up. Compromising a server could cause such damage that ASPs (that want to stay in business) are likely to be careful about security.

[11] . In 1995, when we started Viaweb, Java applets were supposed to be the technology everyone was going to use to develop server-based applications. Applets seemed to us an old-fashioned idea. Download programs to run on the client? Simpler just to go all the way and run the programs on the server. We wasted little time on applets, but countless other startups must have been lured into this tar pit. Few can have escaped alive, or Microsoft could not have gotten away with dropping Java in the most recent version of Explorer.

[12] . This point is due to Trevor Blackwell, who adds “the cost of writing software goes up more than linearly with its size. Perhaps this is mainly due to fixing old bugs, and the cost can be more linear if all bugs are found quickly.”

[13] . The hardest kind of bug to find may be a variant of compound bug where one bug happens to compensate for another. When you fix one bug, the other becomes visible. But it will seem as if the fix is at fault, since that was the last thing you changed.

[14] . Within Viaweb we once had a contest to describe the worst thing about our software. Two customer support people tied for first prize with entries I still shiver to recall. We fixed both problems immediately.

[15] . Robert Morris wrote the ordering system, which shoppers used to place orders. Trevor Blackwell wrote the image generator and the manager, which merchants used to retrieve orders, view statistics, and configure domain names etc. I wrote the editor, which merchants used to build their sites. The ordering system and image generator were written in C and C++, the manager mostly in Perl, and the editor in Lisp.

[16] . Price discrimination is so pervasive (how often have you heard a retailer claim that their buying power meant lower prices for you?) that I was surprised to find it was outlawed in the U.S. by the Robinson-Patman Act of 1936. This law does not appear to be vigorously enforced.

[17] . In No Logo, Naomi Klein says that clothing brands favored by “urban youth” do not try too hard to prevent shoplifting because in their target market the shoplifters are also the fashion leaders.

[18] . Companies often wonder what to outsource and what not to. One possible answer: outsource any job that’s not directly exposed to competitive pressure, because outsourcing it will thereby expose it to competitive pressure.

[19] . The two guys were Dan Bricklin and Bob Frankston. Dan wrote a prototype in Basic in a couple days, then over the course of the next year they worked together (mostly at night) to make a more powerful version written in 6502 machine language. Dan was at Harvard Business School at the time and Bob nominally had a day job writing software. “There was no great risk in doing a business,” Bob wrote, “If it failed it failed. No big deal.”

[20] . It’s not quite as easy as I make it sound. It took a painfully long time for word of mouth to get going, and we did not start to get a lot of press coverage until we hired a PR firm (admittedly the best in the business) for $16,000 per month. However, it was true that the only significant channel was our own Web site.

[21] . If the Mac was so great, why did it lose? Cost, again. Microsoft concentrated on the software business, and unleashed a swarm of cheap component suppliers on Apple hardware. It did not help, either, that suits took over during a critical period.

[22] . One thing that would help Web-based applications, and help keep the next generation of software from being overshadowed by Microsoft, would be a good open-source browser. Mozilla is open-source but seems to have suffered from having been corporate software for so long. A small, fast browser that was actively maintained would be a great thing in itself, and would probably also encourage companies to build little Web appliances. Among other things, a proper open-source browser would cause HTTP and HTML to continue to evolve (as e.g. Perl has). It would help Web-based applications greatly to be able to distinguish between selecting a link and following it; all you’d need to do this would be a trivial enhancement of HTTP, to allow multiple urls in a request. Cascading menus would also be good. If you want to change the world, write a new Mosaic. Think it’s too late? In 1998 a lot of people thought it was too late to launch a new search engine, but Google proved them wrong. There is always room for something new if the current options suck enough. Make sure it works on all the free OSes first– new things start with their users.

[23] . Trevor Blackwell, who probably knows more about this from personal experience than anyone, writes: “I would go farther in saying that because server-based software is so hard on the programmers, it causes a fundamental economic shift away from large companies. It requires the kind of intensity and dedication from programmers that they will only be willing to provide when it’s their own company. Software companies can hire skilled people to work in a not-too-demanding environment, and can hire unskilled people to endure hardships, but they can’t hire highly skilled people to bust their asses. Since capital is no longer needed, big companies have little to bring to the table.”

[24] . In the original version of this essay, I advised avoiding Javascript. That was a good plan in 2001, but Javascript now works.

[25] . :i| s := s+i.

[26] . Paul Graham. A Plan for Spam.'' August 2002. http://paulgraham.com/spam.html. Probabilities in this algorithm are calculated using a degenerate case of Bayes' Rule. There are two simplifying assumptions: that the probabilities of features (i.e. words) are independent, and that we know nothing about the prior probability of an email being spam. The first assumption is widespread in text classification. Algorithms that use it are callednaive Bayesian.’’ The second assumption I made because the proportion of spam in my incoming mail fluctuated so much from day to day (indeed, from hour to hour) that the overall prior ratio seemed worthless as a predictor. If you assume that P(spam) and P(nonspam) are both .5, they cancel out and you can remove them from the formula. If you were doing Bayesian filtering in a situation where the ratio of spam to nonspam was consistently very high or (especially) very low, you could probably improve filter performance by incorporating prior probabilities. To do this right you’d have to track ratios by time of day, because spam and legitimate mail volume both have distinct daily patterns.

[27] . Patrick Pantel and Dekang Lin. ``SpamCop– A Spam Classification & Organization Program.’’ Proceedings of AAAI-98 Workshop on Learning for Text Categorization.

[28] . Mehran Sahami, Susan Dumais, David Heckerman and Eric Horvitz. ``A Bayesian Approach to Filtering Junk E-Mail.’’ Proceedings of AAAI-98 Workshop on Learning for Text Categorization.

[29] . At the time I had zero false positives out of about 4,000 legitimate emails. If the next legitimate email was a false positive, this would give us .03%. These false positive rates are untrustworthy, as I explain later. I quote a number here only to emphasize that whatever the false positive rate is, it is less than 1.16%.

[30] . Bill Yerazunis. ``Sparse Binary Polynomial Hash Message Filtering and The CRM114 Discriminator.’’ Proceedings of 2003 Spam Conference.

[31] . In ``A Plan for Spam’’ I used thresholds of .99 and .01. It seems justifiable to use thresholds proportionate to the size of the corpora. Since I now have on the order of 10,000 of each type of mail, I use .9999 and .0001.

[32] . There is a flaw here I should probably fix. Currently, when Subject*foo'' degenerates to justfoo’‘, what that means is you’re getting the stats for occurrences of foo'' in the body or header lines other than those I mark. What I should do is keep track of statistics forfoo’’ overall as well as specific versions, and degenerate from Subject*foo'' not tofoo’’ but to Anywhere*foo''. Ditto for case: I should degenerate from uppercase to any-case, not lowercase. It would probably be a win to do this with prices too, e.g. to degenerate from$129.99'' to ``$–9.99’‘, $--.99'', and$–’’. You could also degenerate from words to their stems, but this would probably only improve filtering rates early on when you had small corpora.

[33] . Steven Hauser. ``Statistical Spam Filter Works for Me.’’ http://www.sofbot.com.

[34] . False positives are not all equal, and we should remember this when comparing techniques for stopping spam. Whereas many of the false positives caused by filters will be near-spams that you wouldn’t mind missing, false positives caused by blacklists, for example, will be just mail from people who chose the wrong ISP. In both cases you catch mail that’s near spam, but for blacklists nearness is physical, and for filters it’s textual.

[35] . If spammers get good enough at obscuring tokens for this to be a problem, we can respond by simply removing whitespace, periods, commas, etc. and using a dictionary to pick the words out of the resulting sequence. And of course finding words this way that weren’t visible in the original text would in itself be evidence of spam. Picking out the words won’t be trivial. It will require more than just reconstructing word boundaries; spammers both add (xHot nPorn cSite'') and omit (P#rn’’) letters. Vision research may be useful here, since human vision is the limit that such tricks will approach.

[36] . In general, spams are more repetitive than regular email. They want to pound that message home. I currently don’t allow duplicates in the top 15 tokens, because you could get a false positive if the sender happens to use some bad word multiple times. (In my current filter, ``dick’’ has a spam probabilty of .9999, but it’s also a name.) It seems we should at least notice duplication though, so I may try allowing up to two of each token, as Brian Burton does in SpamProbe.

[37] . This is what approaches like Brightmail’s will degenerate into once spammers are pushed into using mad-lib techniques to generate everything else in the message.

[38] . It’s sometimes argued that we should be working on filtering at the network level, because it is more efficient. What people usually mean when they say this is: we currently filter at the network level, and we don’t want to start over from scratch. But you can’t dictate the problem to fit your solution. Historically, scarce-resource arguments have been the losing side in debates about software design. People only tend to use them to justify choices (inaction in particular) made for other reasons.

[39] . The greatest damage that photography has done to painting may be the fact that it killed the best day job. Most of the great painters in history supported themselves by painting portraits.

[40] . I’ve been told that Microsoft discourages employees from contributing to open-source projects, even in their spare time. But so many of the best hackers work on open-source projects now that the main effect of this policy may be to ensure that they won’t be able to hire any first-rate programmers.

[41] . What you learn about programming in college is much like what you learn about books or clothes or dating: what bad taste you had in high school.

[42] . Here’s an example of applied empathy. At Viaweb, if we couldn’t decide between two alternatives, we’d ask, what would our competitors hate most? At one point a competitor added a feature to their software that was basically useless, but since it was one of few they had that we didn’t, they made much of it in the trade press. We could have tried to explain that the feature was useless, but we decided it would annoy our competitor more if we just implemented it ourselves, so we hacked together our own version that afternoon.

[43] . Except text editors and compilers. Hackers don’t need empathy to design these, because they are themselves typical users.

[44] . Well, almost. They overshot the available RAM somewhat, causing much inconvenient disk swapping, but this could be fixed within a few months by buying an additional disk drive.

[45] . The way to make programs easy to read is not to stuff them with comments. I would take Abelson and Sussman’s quote a step further. Programming languages should be designed to express algorithms, and only incidentally to tell computers how to execute them. A good programming language ought to be better for explaining software than English. You should only need comments when there is some kind of kludge you need to warn readers about, just as on a road there are only arrows on parts with unexpectedly sharp curves.

[46] . Auto-retrieving filters will have to follow redirects, and should in some cases (e.g. a page that just says “click here”) follow more than one level of links. Make sure too that the http requests are indistinguishable from those of popular Web browsers, including the order and referrer. If the response doesn’t come back within x amount of time, default to some fairly high spam probability. Instead of making n constant, it might be a good idea to make it a function of the number of spams that have been seen mentioning the site. This would add a further level of protection against abuse and accidents.

[47] . The original version of this article used the term “whitelist” instead of “blacklist”. Though they were to work like blacklists, I preferred to call them whitelists because it might make them less vulnerable to legal attack. This just seems to have confused readers, though. There should probably be multiple blacklists. A single point of failure would be vulnerable both to attack and abuse.

[48] . One valuable thing you tend to get only in startups is uninterruptability. Different kinds of work have different time quanta. Someone proofreading a manuscript could probably be interrupted every fifteen minutes with little loss of productivity. But the time quantum for hacking is very long: it might take an hour just to load a problem into your head. So the cost of having someone from personnel call you about a form you forgot to fill out can be huge. This is why hackers give you such a baleful stare as they turn from their screen to answer your question. Inside their heads a giant house of cards is tottering. The mere possibility of being interrupted deters hackers from starting hard projects. This is why they tend to work late at night, and why it’s next to impossible to write great software in a cubicle (except late at night). One great advantage of startups is that they don’t yet have any of the people who interrupt you. There is no personnel department, and thus no form nor anyone to call you about it.

[49] . Faced with the idea that people working for startups might be 20 or 30 times as productive as those working for large companies, executives at large companies will naturally wonder, how could I get the people working for me to do that? The answer is simple: pay them to. Internally most companies are run like Communist states. If you believe in free markets, why not turn your company into one? Hypothesis: A company will be maximally profitable when each employee is paid in proportion to the wealth they generate.

[50] . Until recently even governments sometimes didn’t grasp the distinction between money and wealth. Adam Smith (Wealth of Nations , v:i) mentions several that tried to preserve their “wealth” by forbidding the export of gold or silver. But having more of the medium of exchange would not make a country richer; if you have more money chasing the same amount of material wealth, the only result is higher prices.

[51] . There are many senses of the word “wealth,” not all of them material. I’m not trying to make a deep philosophical point here about which is the true kind. I’m writing about one specific, rather technical sense of the word “wealth.” What people will give you money for. This is an interesting sort of wealth to study, because it is the kind that prevents you from starving. And what people will give you money for depends on them, not you. When you’re starting a business, it’s easy to slide into thinking that customers want what you do. During the Internet Bubble I talked to a woman who, because she liked the outdoors, was starting an “outdoor portal.” You know what kind of business you should start if you like the outdoors? One to recover data from crashed hard disks. What’s the connection? None at all. Which is precisely my point. If you want to create wealth (in the narrow technical sense of not starving) then you should be especially skeptical about any plan that centers on things you like doing. That is where your idea of what’s valuable is least likely to coincide with other people’s.

[52] . In the average car restoration you probably do make everyone else microscopically poorer, by doing a small amount of damage to the environment. While environmental costs should be taken into account, they don’t make wealth a zero-sum game. For example, if you repair a machine that’s broken because a part has come unscrewed, you create wealth with no environmental cost. [5b] This essay was written before Firefox.

[53] . Many people feel confused and depressed in their early twenties. Life seemed so much more fun in college. Well, of course it was. Don’t be fooled by the surface similarities. You’ve gone from guest to servant. It’s possible to have fun in this new world. Among other things, you now get to go behind the doors that say “authorized personnel only.” But the change is a shock at first, and all the worse if you’re not consciously aware of it.

[54] . When VCs asked us how long it would take another startup to duplicate our software, we used to reply that they probably wouldn’t be able to at all. I think this made us seem naive, or liars.

[55] . Few technologies have one clear inventor. So as a rule, if you know the “inventor” of something (the telephone, the assembly line, the airplane, the light bulb, the transistor) it is because their company made money from it, and the company’s PR people worked hard to spread the story. If you don’t know who invented something (the automobile, the television, the computer, the jet engine, the laser), it’s because other companies made all the money.

[56] . This is a good plan for life in general. If you have two choices, choose the harder. If you’re trying to decide whether to go out running or sit home and watch TV, go running. Probably the reason this trick works so well is that when you have two choices and one is harder, the only reason you’re even considering the other is laziness. You know in the back of your mind what’s the right thing to do, and this trick merely forces you to acknowledge it.

[57] . It is probably no accident that the middle class first appeared in northern Italy and the low countries, where there were no strong central governments. These two regions were the richest of their time and became the twin centers from which Renaissance civilization radiated. If they no longer play that role, it is because other places, like the United States, have been truer to the principles they discovered.

[58] . It may indeed be a sufficient condition. But if so, why didn’t the Industrial Revolution happen earlier? Two possible (and not incompatible) answers: (a) It did. The Industrial Revolution was one in a series. (b) Because in medieval towns, monopolies and guild regulations initially slowed the development of new means of production. Comment on this essay. Russian Translation Arabic Translation Spanish Translation * * * You’ll find this essay and 14 others in Hackers & Painters.

[59] . Part of the reason this subject is so contentious is that some of those most vocal on the subject of wealth–university students, heirs, professors, politicians, and journalists–have the least experience creating it. (This phenomenon will be familiar to anyone who has overheard conversations about sports in a bar.) Students are mostly still on the parental dole, and have not stopped to think about where that money comes from. Heirs will be on the parental dole for life. Professors and politicians live within socialist eddies of the economy, at one remove from the creation of wealth, and are paid a flat rate regardless of how hard they work. And journalists as part of their professional code segregate themselves from the revenue-collecting half of the businesses they work for (the ad sales department). Many of these people never come face to face with the fact that the money they receive represents wealth–wealth that, except in the case of journalists, someone else created earlier. They live in a world in which income is doled out by a central authority according to some abstract notion of fairness (or randomly, in the case of heirs), rather than given by other people in return for something they wanted, so it may seem to them unfair that things don’t work the same in the rest of the economy. (Some professors do create a great deal of wealth for society. But the money they’re paid isn’t a quid pro quo. It’s more in the nature of an investment.)

[60] . When one reads about the origins of the Fabian Society, it sounds like something cooked up by the high-minded Edwardian child-heroes of Edith Nesbit’s The Wouldbegoods.

[61] . According to a study by the Corporate Library, the median total compensation, including salary, bonus, stock grants, and the exercise of stock options, of S&P; 500 CEOs in 2002 was $3.65 million. According to Sports Illustrated , the average NBA player’s salary during the 2002-03 season was $4.54 million, and the average major league baseball player’s salary at the start of the 2003 season was $2.56 million. According to the Bureau of Labor Statistics, the mean annual wage in the US in 2002 was $35,560.

[62] . In the early empire the price of an ordinary adult slave seems to have been about 2,000 sestertii (e.g. Horace, Sat. ii.7.43). A servant girl cost 600 (Martial vi.66), while Columella (iii.3.8) says that a skilled vine- dresser was worth 8,000. A doctor, P. Decimus Eros Merula, paid 50,000 sestertii for his freedom (Dessau, Inscriptiones 7812). Seneca (Ep. xxvii.7) reports that one Calvisius Sabinus paid 100,000 sestertii apiece for slaves learned in the Greek classics. Pliny (Hist. Nat. vii.39) says that the highest price paid for a slave up to his time was 700,000 sestertii, for the linguist (and presumably teacher) Daphnis, but that this had since been exceeded by actors buying their own freedom. Classical Athens saw a similar variation in prices. An ordinary laborer was worth about 125 to 150 drachmae. Xenophon (Mem. ii.5) mentions prices ranging from 50 to 6,000 drachmae (for the manager of a silver mine). For more on the economics of ancient slavery see: Jones, A. H. M., “Slavery in the Ancient World,” Economic History Review , 2:9 (1956), 185-199, reprinted in Finley, M. I. (ed.), Slavery in Classical Antiquity , Heffer, 1964.

[63] . Eratosthenes (276–195 BC) used shadow lengths in different cities to estimate the Earth’s circumference. He was off by only about 2%.

[64] . No, and Windows, respectively.

[65] . One of the biggest divergences between the Daddy Model and reality is the valuation of hard work. In the Daddy Model, hard work is in itself deserving. In reality, wealth is measured by what one delivers, not how much effort it costs. If I paint someone’s house, the owner shouldn’t pay me extra for doing it with a toothbrush. It will seem to someone still implicitly operating on the Daddy Model that it is unfair when someone works hard and doesn’t get paid much. To help clarify the matter, get rid of everyone else and put our worker on a desert island, hunting and gathering fruit. If he’s bad at it he’ll work very hard and not end up with much food. Is this unfair? Who is being unfair to him?

[66] . Part of the reason for the tenacity of the Daddy Model may be the dual meaning of “distribution.” When economists talk about “distribution of income,” they mean statistical distribution. But when you use the phrase frequently, you can’t help associating it with the other sense of the word (as in e.g. “distribution of alms”), and thereby subconsciously seeing wealth as something that flows from some central tap. The word “regressive” as applied to tax rates has a similar effect, at least on me; how can anything regressive be good?

[67] . “From the beginning of the reign Thomas Lord Roos was an assiduous courtier of the young Henry VIII and was soon to reap the rewards. In 1525 he was made a Knight of the Garter and given the Earldom of Rutland. In the thirties his support of the breach with Rome, his zeal in crushing the Pilgrimage of Grace, and his readiness to vote the death-penalty in the succession of spectacular treason trials that punctuated Henry’s erratic matrimonial progress made him an obvious candidate for grants of monastic property.” Stone, Lawrence, Family and Fortune: Studies in Aristocratic Finance in the Sixteenth and Seventeenth Centuries , Oxford University Press, 1973, p. 166.

[68] . There is archaeological evidence for large settlements earlier, but it’s hard to say what was happening in them. Hodges, Richard and David Whitehouse, Mohammed, Charlemagne and the Origins of Europe , Cornell University Press, 1983.

[69] . William Cecil and his son Robert were each in turn the most powerful minister of the crown, and both used their position to amass fortunes among the largest of their times. Robert in particular took bribery to the point of treason. “As Secretary of State and the leading advisor to King James on foreign policy, [he] was a special recipient of favour, being offered large bribes by the Dutch not to make peace with Spain, and large bribes by Spain to make peace.” (Stone, op. cit. , p. 17.)

[70] . Though Balzac made a lot of money from writing, he was notoriously improvident and was troubled by debts all his life.

[71] . A Timex will gain or lose about .5 seconds per day. The most accurate mechanical watch, the Patek Philippe 10 Day Tourbillon, is rated at -1.5 to +2 seconds. Its retail price is about $220,000.

[72] . If asked to choose which was more expensive, a well-preserved 1989 Lincoln Town Car ten-passenger limousine ($5,000) or a 2004 Mercedes S600 sedan ($122,000), the average Edwardian might well guess wrong.

[73] . To say anything meaningful about income trends, you have to talk about real income, or income as measured in what it can buy. But the usual way of calculating real income ignores much of the growth in wealth over time, because it depends on a consumer price index created by bolting end to end a series of numbers that are only locally accurate, and that don’t include the prices of new inventions until they become so common that their prices stabilize. So while we might think it was very much better to live in a world with antibiotics or air travel or an electric power grid than without, real income statistics calculated in the usual way will prove to us that we are only slightly richer for having these things. Another approach would be to ask, if you were going back to the year x in a time machine, how much would you have to spend on trade goods to make your fortune? For example, if you were going back to 1970 it would certainly be less than $500, because the processing power you can get for $500 today would have been worth at least $150 million in 1970. The function goes asymptotic fairly quickly, because for times over a hundred years or so you could get all you needed in present-day trash. In 1800 an empty plastic drink bottle with a screw top would have seemed a miracle of workmanship.

[74] . Some will say this amounts to the same thing, because the rich have better opportunities for education. That’s a valid point. It is still possible, to a degree, to buy your kids’ way into top colleges by sending them to private schools that in effect hack the college admissions process. According to a 2002 report by the National Center for Education Statistics, about 1.7% of American kids attend private, non-sectarian schools. At Princeton, 36% of the class of 2007 came from such schools. (Interestingly, the number at Harvard is significantly lower, about 28%.) Obviously this is a huge loophole. It does at least seem to be closing, not widening. Perhaps the designers of admissions processes should take a lesson from the example of computer security, and instead of just assuming that their system can’t be hacked, measure the degree to which it is. Spanish Translation * * *

[75] . In fairness, I have to say that IBM makes decent hardware. I wrote this on an IBM laptop.

[76] . They did turn out to be doomed. They shut down a few months later.

[77] . I think this is what people mean when they talk about the “meaning of life.” On the face of it, this seems an odd idea. Life isn’t an expression; how could it have meaning? But it can have a quality that feels a lot like meaning. In a project like a compiler, you have to solve a lot of problems, but the problems all fall into a pattern, as in a signal. Whereas when the problems you have to solve are random, they seem like noise.

[78] . Einstein at one point worked designing refrigerators. (He had equity.)

[79] . It’s hard to say exactly what constitutes research in the computer world, but as a first approximation, it’s software that doesn’t have users. I don’t think it’s publication that makes the best hackers want to work in research departments. I think it’s mainly not having to have a three hour meeting with a product manager about problems integrating the Korean version of Word 13.27 with the talking paperclip.

[80] . Something similar has been happening for a long time in the construction industry. When you had a house built a couple hundred years ago, the local builders built everything in it. But increasingly what builders do is assemble components designed and manufactured by someone else. This has, like the arrival of desktop publishing, given people the freedom to experiment in disastrous ways, but it is certainly more efficient.

[81] . Google is much more dangerous to Microsoft than Netscape was. Probably more dangerous than any other company has ever been. Not least because they’re determined to fight. On their job listing page, they say that one of their “core values’’ is”Don’t be evil.’’ From a company selling soybean oil or mining equipment, such a statement would merely be eccentric. But I think all of us in the computer world recognize who that is a declaration of war on.

[82] . I’m thinking of Oresme (c. 1323-82). But it’s hard to pick a date, because there was a sudden drop-off in scholarship just as Europeans finished assimilating classical science. The cause may have been the plague of 1347; the trend in scientific progress matches the population curve.

[83] . Parker, William R. “Where Do College English Departments Come From?” College English 28 (1966-67), pp. 339-351. Reprinted in Gray, Donald J. (ed). The Department of English at Indiana University Bloomington 1868-1970. Indiana University Publications. Daniels, Robert V. The University of Vermont: The First Two Hundred Years. University of Vermont, 1991. Mueller, Friedrich M. Letter to the Pall Mall Gazette. 1886/87. Reprinted in Bacon, Alan (ed). The Nineteenth-Century History of English Studies. Ashgate, 1998.

[84] . I’m compressing the story a bit. At first literature took a back seat to philology, which (a) seemed more serious and (b) was popular in Germany, where many of the leading scholars of that generation had been trained. In some cases the writing teachers were transformed in situ into English professors. Francis James Child, who had been Boylston Professor of Rhetoric at Harvard since 1851, became in 1876 the university’s first professor of English.

[85] . Parker, op. cit. , p. 25.

[86] . The undergraduate curriculum or trivium (whence “trivial”) consisted of Latin grammar, rhetoric, and logic. Candidates for masters’ degrees went on to study the quadrivium of arithmetic, geometry, music, and astronomy. Together these were the seven liberal arts. The study of rhetoric was inherited directly from Rome, where it was considered the most important subject. It would not be far from the truth to say that education in the classical world meant training landowners’ sons to speak well enough to defend their interests in political and legal disputes.

[87] . Trevor Blackwell points out that this isn’t strictly true, because the outside edges of curves erode faster.

[88] . Actually it’s hard to say now. As Jeremy Siegel points out, if the value of a stock is its future earnings, you can’t tell if it was overvalued till you see what the earnings turn out to be. While certain famous Internet stocks were almost certainly overvalued in 1999, it is still hard to say for sure whether, e.g., the Nasdaq index was. Siegel, Jeremy J. “What Is an Asset Price Bubble? An Operational Definition.” European Financial Management, 9:1, 2003.

[89] . The number of users comes from a 6/03 Nielsen study quoted on Google’s site. (You’d think they’d have something more recent.) The revenue estimate is based on revenues of $1.35 billion for the first half of 2004, as reported in their IPO filing.

[90] . As Clinton himself discovered to his surprise when, in one of his first acts as president, he tried to shift the military leftward. After a bruising fight he escaped with a face-saving compromise.

[91] . True, Gore won the popular vote. But politicians know the electoral vote decides the election, so that’s what they campaign for. If Bush had been campaigning for the popular vote he would presumably have got more of it. (Thanks to judgmentalist for this point.)

[92] . Source: Nielsen Media Research. Of the remaining 13%, 11 didn’t have TV because they couldn’t afford it. I’d argue that the missing 11% were probably also the 11% most susceptible to charisma.

[93] . One implication of this theory is that parties shouldn’t be too quick to reject candidates with skeletons in their closets. Charismatic candidates will tend to have more skeletons than squeaky clean dullards, but in practice that doesn’t seem to lose elections. The current Bush, for example, probably did more drugs in his twenties than any preceding president, and yet managed to get elected with a base of evangelical Christians. All you have to do is say you’ve reformed, and stonewall about the details.

[94] . Japanese cities are ugly too, but for different reasons. Japan is prone to earthquakes, so buildings are traditionally seen as temporary; there is no grand tradition of city planning like the one Europeans inherited from Rome. The other cause is the notoriously corrupt relationship between the government and construction companies.

[95] . A doctor friend warns that even this can give an inaccurate picture. “Who knew how much time it would take up, how little autonomy one would have for endless years of training, and how unbelievably annoying it is to carry a beeper?”

[96] . His best bet would probably be to become dictator and intimidate the NBA into letting him play. So far the closest anyone has come is Secretary of Labor.

[97] . A day job is one you take to pay the bills so you can do what you really want, like play in a band, or invent relativity. Treating high school as a day job might actually make it easier for some students to get good grades. If you treat your classes as a game, you won’t be demoralized if they seem pointless. However bad your classes, you need to get good grades in them to get into a decent college. And that is worth doing, because universities are where a lot of the clumps of smart people are these days.

[98] . The second biggest regret was caring so much about unimportant things. And especially about what other people thought of them. I think what they really mean, in the latter case, is caring what random people thought of them. Adults care just as much what other people think, but they get to be more selective about the other people. I have about thirty friends whose opinions I care about, and the opinion of the rest of the world barely affects me. The problem in high school is that your peers are chosen for you by accidents of age and geography, rather than by you based on respect for their judgement.

[99] . The key to wasting time is distraction. Without distractions it’s too obvious to your brain that you’re not doing anything with it, and you start to feel uncomfortable. If you want to measure how dependent you’ve become on distractions, try this experiment: set aside a chunk of time on a weekend and sit alone and think. You can have a notebook to write your thoughts down in, but nothing else: no friends, TV, music, phone, IM, email, Web, games, books, newspapers, or magazines. Within an hour most people will feel a strong craving for distraction.

[100] . I don’t mean to imply that the only function of prep schools is to trick admissions officers. They also generally provide a better education. But try this thought experiment: suppose prep schools supplied the same superior education but had a tiny (.001) negative effect on college admissions. How many parents would still send their kids to them? It might also be argued that kids who went to prep schools, because they’ve learned more, are better college candidates. But this seems empirically false. What you learn in even the best high school is rounding error compared to what you learn in college. Public school kids arrive at college with a slight disadvantage, but they start to pull ahead in the sophomore year. (I’m not saying public school kids are smarter than preppies, just that they are within any given college. That follows necessarily if you agree prep schools improve kids’ admissions prospects.)

[101] . Why does society foul you? Indifference, mainly. There are simply no outside forces pushing high school to be good. The air traffic control system works because planes would crash otherwise. Businesses have to deliver because otherwise competitors would take their customers. But no planes crash if your school sucks, and it has no competitors. High school isn’t evil; it’s random; but random is pretty bad.

[102] . And then of course there is money. It’s not a big factor in high school, because you can’t do much that anyone wants. But a lot of great things were created mainly to make money. Samuel Johnson said “no man but a blockhead ever wrote except for money.” (Many hope he was exaggerating.)

[103] . Even college textbooks are bad. When you get to college, you’ll find that (with a few stellar exceptions) the textbooks are not written by the leading scholars in the field they describe. Writing college textbooks is unpleasant work, done mostly by people who need the money. It’s unpleasant because the publishers exert so much control, and there are few things worse than close supervision by someone who doesn’t understand what you’re doing. This phenomenon is apparently even worse in the production of high school textbooks.

[104] . Your teachers are always telling you to behave like adults. I wonder if they’d like it if you did. You may be loud and disorganized, but you’re very docile compared to adults. If you actually started acting like adults, it would be just as if a bunch of adults had been transposed into your bodies. Imagine the reaction of an FBI agent or taxi driver or reporter to being told they had to ask permission to go the bathroom, and only one person could go at a time. To say nothing of the things you’re taught. If a bunch of actual adults suddenly found themselves trapped in high school, the first thing they’d do is form a union and renegotiate all the rules with the administration.

[105] . Google’s revenues are about two billion a year, but half comes from ads on other sites.

[106] . One advantage startups have over established companies is that there are no discrimination laws about starting businesses. For example, I would be reluctant to start a startup with a woman who had small children, or was likely to have them soon. But you’re not allowed to ask prospective employees if they plan to have kids soon. Believe it or not, under current US law, you’re not even allowed to discriminate on the basis of intelligence. Whereas when you’re starting a company, you can discriminate on any basis you want about who you start it with.

[107] . Learning to hack is a lot cheaper than business school, because you can do it mostly on your own. For the price of a Linux box, a copy of K&R;, and a few hours of advice from your neighbor’s fifteen year old son, you’ll be well on your way.

[108] . Corollary: Avoid starting a startup to sell things to the biggest company of all, the government. Yes, there are lots of opportunities to sell them technology. But let someone else start those startups.

[109] . A friend who started a company in Germany told me they do care about the paperwork there, and that there’s more of it. Which helps explain why there are not more startups in Germany.

[110] . At the seed stage our valuation was in principle $100,000, because Julian got 10% of the company. But this is a very misleading number, because the money was the least important of the things Julian gave us.

[111] . The same goes for companies that seem to want to acquire you. There will be a few that are only pretending to in order to pick your brains. But you can never tell for sure which these are, so the best approach is to seem entirely open, but to fail to mention a few critical technical secrets.

[112] . I was as bad an employee as this place was a company. I apologize to anyone who had to work with me there.

[113] . You could probably write a book about how to succeed in business by doing everything in exactly the opposite way from the DMV.

[114] . After Greylock booted founder Philip Greenspun out of ArsDigita, he wrote a hilarious but also very informative essay about it.

[115] . Since most VCs aren’t tech guys, the technology side of their due diligence tends to be like a body cavity search by someone with a faulty knowledge of human anatomy. After a while we were quite sore from VCs attempting to probe our nonexistent database orifice. No, we don’t use Oracle. We just store the data in files. Our secret is to use an OS that doesn’t lose our data. Which OS? FreeBSD. Why do you use that instead of Windows NT? Because it’s better and it doesn’t cost anything. What, you’re using a freeware OS? How many times that conversation was repeated. Then when we got to Yahoo, we found they used FreeBSD and stored their data in files too. Chinese Translation Japanese Translation * * *

[116] . No one seems to have minded, which shows how unimportant the Arpanet (which became the Internet) was as late as 1984.

[117] . This is why, when I became an employer, I didn’t care about GPAs. In fact, we actively sought out people who’d failed out of school. We once put up posters around Harvard saying “Did you just get kicked out for doing badly in your classes because you spent all your time working on some project of your own? Come work for us!” We managed to find a kid who had been, and he was a great hacker. When Harvard kicks undergrads out for a year, they have to get jobs. The idea is to show them how awful the real world is, so they’ll understand how lucky they are to be in college. This plan backfired with the guy who came to work for us, because he had more fun than he’d had in school, and made more that year from stock options than any of his professors did in salary. So instead of crawling back repentant at the end of the year, he took another year off and went to Europe. He did eventually graduate at about 26.

[118] . Eric Raymond says the best metaphors for hackers are in set theory, combinatorics, and graph theory. Trevor Blackwell reminds you to take math classes intended for math majors. “‘Math for engineers’ classes sucked mightily. In fact any ‘x for engineers’ sucks, where x includes math, law, writing and visual design.”

[119] . Other highly recommended books: What is Mathematics? , by Courant and Robbins; Geometry and the Imagination by Hilbert and Cohn-Vossen. And for those interested in graphic design, Byrne’s Euclid.

[120] . If you wanted to have the perfect life, the thing to do would be to go to grad school, secretly write your dissertation in the first year or two, and then just enjoy yourself for the next three years, dribbling out a chapter at a time. This prospect will make grad students’ mouths water, but I know of no one who’s had the discipline to pull it off.

[121] . One professor friend says that 15-20% of the grad students they admit each year are “long shots.” But what he means by long shots are people whose applications are perfect in every way, except that no one on the admissions committee knows the professors who wrote the recommendations. So if you want to get into grad school in the sciences, you need to go to college somewhere with real research professors. Otherwise you’ll seem a risky bet to admissions committees, no matter how good you are. Which implies a surprising but apparently inevitable consequence: little liberal arts colleges are doomed. Most smart high school kids at least consider going into the sciences, even if they ultimately choose not to. Why go to a college that limits their options?

[122] . These horrible stickers are much like the intrusive ads popular on pre- Google search engines. They say to the customer: you are unimportant. We care about Intel and Microsoft, not you.

[123] . Y Combinator is (we hope) visited mostly by hackers. The proportions of OSes are: Windows 66.4%, Macintosh 18.8%, Linux 11.4%, and FreeBSD 1.5%. The Mac number is a big change from what it would have been five years ago. Italian Translation Russian Translation Chinese Translation * * *

[124] . SFP applicants: please don’t assume that not being accepted means we think your idea is bad. Because we want to keep the number of startups small this first summer, we’re going to have to turn down some good proposals too.

[125] . Dealers try to give each customer the impression that the stuff they’re showing him is something special that only a few people have seen, when in fact it may have been sitting in their racks for years while they tried to unload it on buyer after buyer.

[126] . On the other hand, he was skeptical about Viaweb too. I have a precise measure of that, because at one point in the first couple months we made a bet: if he ever made a million dollars out of Viaweb, he’d get his ear pierced. We didn’t let him off, either.

[127] . I wrote a program to generate all the combinations of “Web” plus a three letter word. I learned from this that most three letter words are bad: Webpig, Webdog, Webfat, Webzit, Webfug. But one of them was Webvia; I swapped them to make Viaweb.

[128] . It’s much easier to sell services than a product, just as it’s easier to make a living playing at weddings than by selling recordings. But the margins are greater on products. So during the Bubble a lot of companies used consulting to generate revenues they could attribute to the sale of products, because it made a better story for an IPO.

[129] . Trevor Blackwell presents the following recipe for a startup: “Watch people who have money to spend, see what they’re wasting their time on, cook up a solution, and try selling it to them. It’s surprising how small a problem can be and still provide a profitable market for a solution.”

[130] . You need to offer especially large rewards to get great people to do tedious work. That’s why startups always pay equity rather than just salary.

[131] . Buy an old copy from the 1940s or 50s instead of the current edition, which has been rewritten to suit present fashions. The original edition contained a few unPC ideas, but it’s always better to read an original book, bearing in mind that it’s a book from a past era, than to read a new version sanitized for your protection.

[132] . PR has at least one beneficial feature: it favors small companies. If PR didn’t work, the only alternative would be to advertise, and only big companies can afford that.

[133] . Advertisers pay less for ads in free publications, because they assume readers ignore something they get for free. This is why so many trade publications nominally have a cover price and yet give away free subscriptions with such abandon.

[134] . Different sections of the Times vary so much in their standards that they’re practically different papers. Whoever fed the style section reporter this story about suits coming back would have been sent packing by the regular news reporters.

[135] . The most striking example I know of this type is the “fact” that the Internet worm of 1988 infected 6000 computers. I was there when it was cooked up, and this was the recipe: someone guessed that there were about 60,000 computers attached to the Internet, and that the worm might have infected ten percent of them. Actually no one knows how many computers the worm infected, because the remedy was to reboot them, and this destroyed all traces. But people like numbers. And so this one is now replicated all over the Internet, like a little worm of its own.

[136] . Not all were necessarily supplied by the PR firm. Reporters sometimes call a few additional sources on their own, like someone adding a few fresh vegetables to a can of soup.

[137] . The average B-17 pilot in World War II was in his early twenties. (Thanks to Tad Marko for pointing this out.)

[138] . If a company tried to pay employees this way, they’d be called unfair. And yet when they buy some startups and not others, no one thinks of calling that unfair.

[139] . The 1/10 success rate for startups is a bit of an urban legend. It’s suspiciously neat. My guess is the odds are slightly worse.

[140] . Survey by Forrester Research reported in the cover story of Business Week, 31 Jan 2005. Apparently someone believed you have to replace the actual server in order to switch the operating system.

[141] . It derives from the late Latin tripalium , a torture device so called because it consisted of three stakes. I don’t know how the stakes were used. “Travel” has the same root.

[142] . It would be much bigger news, in that sense, if the president faced unscripted questions by giving a press conference.

[143] . One measure of the incompetence of newspapers is that so many still make you register to read stories. I have yet to find a blog that tried that.

[144] . They accepted the article, but I took so long to send them the final version that by the time I did the section of the magazine they’d accepted it for had disappeared in a reorganization.

[145] . The word “boss” is derived from the Dutch baas , meaning “master.”

[146] . Success here is defined from the initial investors’ point of view: either an IPO, or an acquisition for more than the valuation at the last round of funding. The conventional 1 in 10 success rate is suspiciously neat, but conversations with VCs suggest it’s roughly correct for startups overall. Top VC firms expect to do better.

[147] . I’m not claiming founders sit down and calculate the expected after-tax return from a startup. They’re motivated by examples of other people who did it. And those examples do reflect after-tax returns.

[148] . Conjecture: The variation in wealth in a (non-corrupt) country or organization will be inversely proportional to the prevalence of systems of seniority. So if you suppress variation in wealth, seniority will become correspondingly more important. So far, I know of no counterexamples, though in very corrupt countries you may get both simultaneously. (Thanks to Daniel Sobral for pointing this out.)

[149] . In a country with a truly feudal economy, you might be able to redistribute wealth successfully, because there are no startups to kill.

[150] . The speed at which startups develop new techology is the other reason they pay so well. As I explained in “How to Make Wealth”, what you do in a startup is compress a lifetime’s worth of work into a few years. It seems as dumb to discourage that as to discourage risk-taking.

[151] . By heavy-duty security I mean efforts to protect against truly determined attackers. The image shows us, the 2005 summer founders, and Smartleaf co-founders Mark Nitzberg and Olin Shivers at the 30-foot table Kate Courteau designed for us. Photo by Alex Lewin.

[152] . This phenomenon may account for a number of discrepancies currently blamed on various forbidden isms. Never attribute to malice what can be explained by math.

[153] . A lot of classic abstract expressionism is doodling of this type: artists trained to paint from life using the same gestures but without using them to represent anything. This explains why such paintings are (slightly) more interesting than random marks would be.

[154] . Bill Yerazunis had solved the problem, but he got there by another path. He made a general-purpose file classifier so good that it also worked for spam. One Specific Idea Romanian Translation Japanese Translation Traditional Chinese Translation Russian Translation Arabic Translation * * *

[155] . The aim of such regulations is to protect widows and orphans from crooked investment schemes; people with a million dollars in liquid assets are assumed to be able to protect themselves. The unintended consequence is that the investments that generate the highest returns, like hedge funds, are available only to the rich.

[156] . Consulting is where product companies go to die. IBM is the most famous example. So starting as a consulting company is like starting out in the grave and trying to work your way up into the world of the living.

[157] . If “near you” doesn’t mean the Bay Area, Boston, or Seattle, consider moving. It’s not a coincidence you haven’t heard of many startups from Philadelphia.

[158] . Investors are often compared to sheep. And they are like sheep, but that’s a rational response to their situation. Sheep act the way they do for a reason. If all the other sheep head for a certain field, it’s probably good grazing. And when a wolf appears, is he going to eat a sheep in the middle of the flock, or one near the edge?

[159] . This was partly confidence, and partly simple ignorance. We didn’t know ourselves which VC firms were the impressive ones. We thought software was all that mattered. But that turned out to be the right direction to be naive in: it’s much better to overestimate than underestimate the importance of making a good product.

[160] . I’ve omitted one source: government grants. I don’t think these are even worth thinking about for the average startup. Governments may mean well when they set up grant programs to encourage startups, but what they give with one hand they take away with the other: the process of applying is inevitably so arduous, and the restrictions on what you can do with the money so burdensome, that it would be easier to take a job to get the money. You should be especially suspicious of grants whose purpose is some kind of social engineering– e.g. to encourage more startups to be started in Mississippi. Free money to start a startup in a place where few succeed is hardly free. Some government agencies run venture funding groups, which make investments rather than giving grants. For example, the CIA runs a venture fund called In- Q-Tel that is modelled on private sector funds and apparently generates good returns. They would probably be worth approaching–if you don’t mind taking money from the CIA.

[161] . Options have largely been replaced with restricted stock, which amounts to the same thing. Instead of earning the right to buy stock, the employee gets the stock up front, and earns the right not to have to give it back. The shares set aside for this purpose are still called the “option pool.”

[162] . First-rate technical people do not generally hire themselves out to do due diligence for VCs. So the most difficult part for startup founders is often responding politely to the inane questions of the “expert” they send to look you over.

[163] . VCs regularly wipe out angels by issuing arbitrary amounts of new stock. They seem to have a standard piece of casuistry for this situation: that the angels are no longer working to help the company, and so don’t deserve to keep their stock. This of course reflects a willful misunderstanding of what investment means; like any investor, the angel is being compensated for risks he took earlier. By a similar logic, one could argue that the VCs should be deprived of their shares when the company goes public.

[164] . One new thing the company might encounter is a down round , or a funding round at valuation lower than the previous round. Down rounds are bad news; it is generally the common stock holders who take the hit. Some of the most fearsome provisions in VC deal terms have to do with down rounds–like “full ratchet anti-dilution,” which is as frightening as it sounds. Founders are tempted to ignore these clauses, because they think the company will either be a big success or a complete bust. VCs know otherwise: it’s not uncommon for startups to have moments of adversity before they ultimately succeed. So it’s worth negotiating anti-dilution provisions, even though you don’t think you need to, and VCs will try to make you feel that you’re being gratuitously troublesome.

[165] . From the conference site, June 2004: “While the first wave of the Web was closely tied to the browser, the second wave extends applications across the web and enables a new generation of services and business opportunities.” To the extent this means anything, it seems to be about web-based applications.

[166] . Disclosure: Reddit was funded by Y Combinator. But although I started using it out of loyalty to the home team, I’ve become a genuine addict. While we’re at it, I’m also an investor in !MSFT, having sold all my shares earlier this year.

[167] . I’m not against editing. I spend more time editing than writing, and I have a group of picky friends who proofread almost everything I write. What I dislike is editing done after the fact by someone else.

[168] . Obvious is an understatement. Users had been climbing in through the window for years before Apple finally moved the door.

[169] . Hint: the way to create a web-based alternative to Office may not be to write every component yourself, but to establish a protocol for web-based apps to share a virtual home directory spread across multiple servers. Or it may be to write it all yourself.

[170] . In Jessica Livingston’s Founders at Work.

[171] . Microsoft didn’t sue their customers directly, but they seem to have done all they could to help SCO sue them.

[172] . Currently we do the opposite: when we make kids do boring work, like arithmetic drills, instead of admitting frankly that it’s boring, we try to disguise it with superficial decorations.

[173] . One father told me about a related phenomenon: he found himself concealing from his family how much he liked his work. When he wanted to go to work on a saturday, he found it easier to say that it was because he “had to” for some reason, rather than admitting he preferred to work than stay home with them.

[174] . Something similar happens with suburbs. Parents move to suburbs to raise their kids in a safe environment, but suburbs are so dull and artificial that by the time they’re fifteen the kids are convinced the whole world is boring.

[175] . I’m not saying friends should be the only audience for your work. The more people you can help, the better. But friends should be your compass.

[176] . Donald Hall said young would-be poets were mistaken to be so obsessed with being published. But you can imagine what it would do for a 24 year old to get a poem published in The New Yorker. Now to people he meets at parties he’s a real poet. Actually he’s no better or worse than he was before, but to a clueless audience like that, the approval of an official authority makes all the difference. So it’s a harder problem than Hall realizes. The reason the young care so much about prestige is that the people they want to impress are not very discerning.

[177] . This is isomorphic to the principle that you should prevent your beliefs about how things are from being contaminated by how you wish they were. Most people let them mix pretty promiscuously. The continuing popularity of religion is the most visible index of that.

[178] . A more accurate metaphor would be to say that the graph of jobs is not very well connected.

[179] . You have to be careful here, because a great discovery often seems obvious in retrospect. One-click ordering, however, is not such a discovery.

[180] . “Turn the other cheek” skirts the issue; the critical question is not how to deal with slaps, but sword thrusts.

[181] . Applying for a patent is now very slow, but it might actually be bad if that got fixed. At the moment the time it takes to get a patent is conveniently just longer than the time it takes a startup to succeed or fail.

[182] . Instead of the canonical “could you build this?” maybe the corp dev guys should be asking “will you build this?” or even “why haven’t you already built this?”

[183] . Design ability is so hard to measure that you can’t even trust the design world’s internal standards. You can’t assume that someone with a degree in design is any good at design, or that an eminent designer is any better than his peers. If that worked, any company could build products as good as Apple’s just by hiring sufficiently qualified designers.

[184] . If anyone wanted to try, we’d be interested to hear from them. I suspect it’s one of those things that’s not as hard as everyone assumes.

[185] . Patent trolls can’t even claim, like speculators, that they “create” liquidity.

[186] . If big companies don’t want to wait for the government to take action, there is a way to fight back themselves. For a long time I thought there wasn’t, because there was nothing to grab onto. But there is one resource patent trolls need: lawyers. Big technology companies between them generate a lot of legal business. If they agreed among themselves never to do business with any firm employing anyone who had worked for a patent troll, either as an employee or as outside counsel, they could probably starve the trolls of the lawyers they need.

[187] . Startups can die from releasing something full of bugs, and not fixing them fast enough, but I don’t know of any that died from releasing something stable but minimal very early, then promptly improving it.

[188] . I know this is why I haven’t released Arc. The moment I do, I’ll have people nagging me for features.

[189] . A web site is different from a book or movie or desktop application in this respect. Users judge a site not as a single snapshot, but as an animation with multiple frames. Of the two, I’d say the rate of improvement is more important to users than where you currently are.

[190] . It should not always tell this to users, however. For example, MySpace is basically a replacement mall for mallrats. But it was wiser for them, initially, to pretend that the site was about bands.

[191] . Similarly, don’t make users register to try your site. Maybe what you have is so valuable that visitors should gladly register to get at it. But they’ve been trained to expect the opposite. Most of the things they’ve tried on the web have sucked– and probably especially those that made them register.

[192] . VCs have rational reasons for behaving this way. They don’t make their money (if they make money) off their median investments. In a typical fund, half the companies fail, most of the rest generate mediocre returns, and one or two “make the fund” by succeeding spectacularly. So if they miss just a few of the most promising opportunities, it could hose the whole fund.

[193] . The attitude of a running back doesn’t translate to soccer. Though it looks great when a forward dribbles past multiple defenders, a player who persists in trying such things will do worse in the long term than one who passes.

[194] . The reason Y Combinator never negotiates valuations is that we’re not professional negotiators, and don’t want to turn into them.

[195] . There are two ways to do work you love: (a) to make money, then work on what you love, or (b) to get a job where you get paid to work on stuff you love. In practice the first phases of both consist mostly of unedifying schleps, and in (b) the second phase is less secure.

[196] . It’s interesting to consider how low this number could be made. I suspect five hundred would be enough, even if they could bring no assets with them. Probably just thirty, if I could pick them, would be enough to turn Buffalo into a significant startup hub.

[197] . Bureaucrats manage to allocate research funding moderately well, but only because (like an in-house VC fund) they outsource most of the work of selection. A professor at a famous university who is highly regarded by his peers will get funding, pretty much regardless of the proposal. That wouldn’t work for startups, whose founders aren’t sponsored by organizations, and are often unknowns.

[198] . You’d have to do it all at once, or at least a whole department at a time, because people would be more likely to come if they knew their friends were. And you should probably start from scratch, rather than trying to upgrade an existing university, or much energy would be lost in friction.

[199] . Hypothesis: Any plan in which multiple independent buildings are gutted or demolished to be “redeveloped” as a single project is a net loss of personality for the city, with the exception of the conversion of buildings not previously public, like warehouses.

[200] . A few startups get started in New York, but less than a tenth as many per capita as in Boston, and mostly in less nerdy fields like finance and media.

[201] . Some blue counties are false positives (reflecting the remaining power of Democractic party machines), but there are no false negatives. You can safely write off all the red counties.

[202] . Some “urban renewal” experts took a shot at destroying Boston’s in the 1960s, leaving the area around city hall a bleak wasteland, but most neighborhoods successfully resisted them.

[203] . On the verge of the Industrial Revolution, England was already the richest country in the world. As far as such things can be compared, per capita income in England in 1750 was higher than India’s in 1960. Deane, Phyllis, The First Industrial Revolution , Cambridge University Press, 1965.

[204] . This has already happened once in China, during the Ming Dynasty, when the country turned its back on industrialization at the command of the court. One of Europe’s advantages was that it had no government powerful enough to do that.

[205] . Of course, Feynman and Diogenes were from adjacent traditions, but Confucius, though more polite, was no more willing to be told what to think.

[206] . For similar reasons it might be a lost cause to try to establish a silicon valley in Israel. Instead of no Jews moving there, only Jews would move there, and I don’t think you could build a silicon valley out of just Jews any more than you could out of just Japanese. (This is not a remark about the qualities of these groups, just their sizes. Japanese are only about 2% of the world population, and Jews about .2%.)

[207] . According to the World Bank, the initial capital requirement for German companies is 47.6% of the per capita income. Doh. World Bank, Doing Business in 2006 , http://doingbusiness.org

[208] . For most of the twentieth century, Europeans looked back on the summer of 1914 as if they’d been living in a dream world. It seems more accurate (or at least, as accurate) to call the years after 1914 a nightmare than to call those before a dream. A lot of the optimism Europeans consider distinctly American is simply what they too were feeling in 1914.

[209] . The point where things start to go wrong seems to be about 50%. Above that people get serious about tax avoidance. The reason is that the payoff for avoiding tax grows hyperexponentially (x/1-x for 0 < x < 1). If your income tax rate is 10%, moving to Monaco would only give you 11% more income, which wouldn’t even cover the extra cost. If it’s 90%, you’d get ten times as much income. And at 98%, as it was briefly in Britain in the 70s, moving to Monaco would give you fifty times as much income. It seems quite likely that European governments of the 70s never drew this curve.

[210] . The facts about Apple’s early history are from an interview with Steve Wozniak in Jessica Livingston’s Founders at Work.

[211] . As usual the popular image is several decades behind reality. Now the misunderstood artist is not a chain-smoking drunk who pours his soul into big, messy canvases that philistines see and say “that’s not art” because it isn’t a picture of anything. The philistines have now been trained that anything hung on a wall is art. Now the misunderstood artist is a coffee-drinking vegan cartoonist whose work they see and say “that’s not art” because it looks like stuff they’ve seen in the Sunday paper.

[212] . In fact this would do fairly well as a definition of politics: what determines rank in the absence of objective tests.

[213] . In high school you’re led to believe your whole future depends on where you go to college, but it turns out only to buy you a couple years. By your mid-twenties the people worth impressing already judge you more by what you’ve done than where you went to school.

[214] . Managers are presumably wondering, how can I make this miracle happen? How can I make the people working for me do more with less? Unfortunately the constraint probably has to be self-imposed. If you’re expected to do more with less, then you’re being starved, not eating virtuously.

[215] . Without the prospect of publication, the closest most people come to writing essays is to write in a journal. I find I never get as deeply into subjects as I do in proper essays. As the name implies, you don’t go back and rewrite journal entries over and over for two weeks.

[216] . Even the desire to protect one’s children seems weaker, judging from things people have historically done to their kids rather than risk their community’s disapproval. (I assume we still do things that will be regarded in the future as barbaric, but historical abuses are easier for us to see.)

[217] . Worrying that Y Combinator makes founders move for 3 months also suggests one underestimates how hard it is to start a startup. You’re going to have to put up with much greater inconveniences than that.

[218] . Most employee agreements say that any idea relating to the company’s present or potential future business belongs to them. Often as not the second clause could include any possible startup, and anyone doing due diligence for an investor or acquirer will assume the worst. To be safe either (a) don’t use code written while you were still employed in your previous job, or (b) get your employer to renounce, in writing, any claim to the code you write for your side project. Many will consent to (b) rather than lose a prized employee. The downside is that you’ll have to tell them exactly what your project does.

[219] . Geshke and Warnock only founded Adobe because Xerox ignored them. If Xerox had used what they built, they would probably never have left PARC.

[220] . This is not a complete list of the causes of failure, just those you can control. There are also several you can’t, notably ineptitude and bad luck.

[221] . Ironically, one variant of the Facebook that might work is a facebook exclusively for college students.

[222] . Steve Jobs tried to motivate people by saying “Real artists ship.” This is a fine sentence, but unfortunately not true. Many famous works of art are unfinished. It’s true in fields that have hard deadlines, like architecture and filmmaking, but even there people tend to be tweaking stuff till it’s yanked out of their hands.

[223] . There’s probably also a second factor: startup founders tend to be at the leading edge of technology, so problems they face are probably especially valuable.

[224] . You should take more than you think you’ll need, maybe 50% to 100% more, because software takes longer to write and deals longer to close than you expect.

[225] . Since people sometimes call us VCs, I should add that we’re not. VCs invest large amounts of other people’s money. We invest small amounts of our own, like angel investors.

[226] . Not linearly of course, or it would take forever to raise five million dollars. In practice it just feels like it takes forever. Though if you include the cases where VCs don’t invest, it would literally take forever in the median case. And maybe we should, because the danger of chasing large investments is not just that they take a long time. That’s the best case. The real danger is that you’ll expend a lot of time and get nothing.

[227] . Some VCs will offer you an artificially low valuation to see if you have the balls to ask for more. It’s lame that VCs play such games, but some do. If you’re dealing with one of those you should push back on the valuation a bit.

[228] . Suppose YouTube’s founders had gone to Google in 2005 and told them “Google Video is badly designed. Give us $10 million and we’ll tell you all the mistakes you made.” They would have gotten the royal raspberry. Eighteen months later Google paid $1.6 billion for the same lesson, partly because they could then tell themselves that they were buying a phenomenon, or a community, or some vague thing like that. I don’t mean to be hard on Google. They did better than their competitors, who may have now missed the video boat entirely.

[229] . Yes, actually: dealing with the government. But phone companies are up there.

[230] . Many more than most people realize, because companies don’t advertise this. Did you know Apple originally had three founders?

[231] . I’m not dissing these people. I don’t have the determination myself. I’ve twice come close to starting startups since Viaweb, and both times I bailed because I realized that without the spur of poverty I just wasn’t willing to endure the stress of a startup.

[232] . So how do you know whether you’re in the category of people who should quit their day job, or the presumably larger one who shouldn’t? I got to the point of saying that this was hard to judge for yourself and that you should seek outside advice, before realizing that that’s what we do. We think of ourselves as investors, but viewed from the other direction Y Combinator is a service for advising people whether or not to quit their day job. We could be mistaken, and no doubt often are, but we do at least bet money on our conclusions.

[233] . This is not to say, of course, that good paintings must have faces in them, just that everyone’s visual piano has that key on it. There are situations in which you want to avoid faces, precisely because they attract so much attention. But you can see how universally faces work by their prevalence in advertising.

[234] . The other reason it’s easy to believe is that it makes people feel good. To a kid, this idea is crack. In every other respect they’re constantly being told that they have a lot to learn. But in this they’re perfect. Their opinion carries the same weight as any adult’s. You should probably question anything you believed as a kid that you’d want to believe this much.

[235] . It’s conceivable that the elegance of proofs is quantifiable, in the sense that there may be some formal measure that turns out to coincide with mathematicians’ judgements. Perhaps it would be worth trying to make a formal language for proofs in which those considered more elegant consistently came out shorter (perhaps after being macroexpanded or compiled).

[236] . Maybe it would be possible to make art that would appeal to space aliens, but I’m not going to get into that because (a) it’s too hard to answer, and (b) I’m satisfied if I can establish that good art is a meaningful idea for human audiences.

[237] . If early abstract paintings seem more interesting than later ones, it may be because the first abstract painters were trained to paint from life, and their hands thus tended to make the kind of gestures you use in representing physical things. In effect they were saying “scaramara” instead of “uebfgbsb.”

[238] . It’s a bit more complicated, because sometimes artists unconsciously use tricks by imitating art that does.

[239] . I phrased this in terms of the taste of apples because if people can see the apples, they can be fooled. When I was a kid most apples were a variety called Red Delicious that had been bred to look appealing in stores, but which didn’t taste very good.

[240] . To be fair, curators are in a difficult position. If they’re dealing with recent art, they have to include things in shows that they think are bad. That’s because the test for what gets included in shows is basically the market price, and for recent art that is largely determined by successful businessmen and their wives. So it’s not always intellectual dishonesty that makes curators and dealers use neutral-sounding language.

[241] . What happens in practice is that everyone gets really good at talking about art. As the art itself gets more random, the effort that would have gone into the work goes instead into the intellectual sounding theory behind it. “My work represents an exploration of gender and sexuality in an urban context,” etc. Different people win at that game.

[242] . There were several other reasons, including that Florence was then the richest and most sophisticated city in the world, and that they lived in a time before photography had (a) killed portraiture as a source of income and (b) made brand the dominant factor in the sale of art. Incidentally, I’m not saying that good art = fifteenth century European art. I’m not saying we should make what they made, but that we should work like they worked. There are fields now in which many people work with the same energy and honesty that fifteenth century artists did, but art is not one of them.

[243] . Gauss was supposedly asked this when he was 10. Instead of laboriously adding together the numbers like the other students, he saw that they consisted of 50 pairs that each summed to 101 (100 + 1, 99 + 2, etc), and that he could just multiply 101 by 50 to get the answer, 5050.

[244] . A variant is that intelligence is the ability to solve problems, and wisdom the judgement to know how to use those solutions. But while this is certainly an important relationship between wisdom and intelligence, it’s not the distinction between them. Wisdom is useful in solving problems too, and intelligence can help in deciding what to do with the solutions.

[245] . In judging both intelligence and wisdom we have to factor out some knowledge. People who know the combination of a safe will be better at opening it than people who don’t, but no one would say that was a test of intelligence or wisdom. But knowledge overlaps with wisdom and probably also intelligence. A knowledge of human nature is certainly part of wisdom. So where do we draw the line? Perhaps the solution is to discount knowledge that at some point has a sharp drop in utility. For example, understanding French will help you in a large number of situations, but its value drops sharply as soon as no one else involved knows French. Whereas the value of understanding vanity would decline more gradually. The knowledge whose utility drops sharply is the kind that has little relation to other knowledge. This includes mere conventions, like languages and safe combinations, and also what we’d call “random” facts, like movie stars’ birthdays, or how to distinguish 1956 from 1957 Studebakers.

[246] . People seeking some single thing called “wisdom” have been fooled by grammar. Wisdom is just knowing the right thing to do, and there are a hundred and one different qualities that help in that. Some, like selflessness, might come from meditating in an empty room, and others, like a knowledge of human nature, might come from going to drunken parties. Perhaps realizing this will help dispel the cloud of semi-sacred mystery that surrounds wisdom in so many people’s eyes. The mystery comes mostly from looking for something that doesn’t exist. And the reason there have historically been so many different schools of thought about how to achieve wisdom is that they’ve focused on different components of it. When I use the word “wisdom” in this essay, I mean no more than whatever collection of qualities helps people make the right choice in a wide variety of situations.

[247] . Even in English, our sense of the word “intelligence” is surprisingly recent. Predecessors like “understanding” seem to have had a broader meaning.

[248] . There is of course some uncertainty about how closely the remarks attributed to Confucius and Socrates resemble their actual opinions. I’m using these names as we use the name “Homer,” to mean the hypothetical people who said the things attributed to them.

[249] . Analects VII:36, Fung trans. Some translators use “calm” instead of “happy.” One source of difficulty here is that present-day English speakers have a different idea of happiness from many older societies. Every language probably has a word meaning “how one feels when things are going well,” but different cultures react differently when things go well. We react like children, with smiles and laughter. But in a more reserved society, or in one where life was tougher, the reaction might be a quiet contentment.

[250] . It may have been Andrew Wiles, but I’m not sure. If anyone remembers such an interview, I’d appreciate hearing from you.

[251] . Confucius claimed proudly that he had never invented anything–that he had simply passed on an accurate account of ancient traditions. [Analects VII:1] It’s hard for us now to appreciate how important a duty it must have been in preliterate societies to remember and pass on the group’s accumulated knowledge. Even in Confucius’s time it still seems to have been the first duty of the scholar.

[252] . The bias toward wisdom in ancient philosophy may be exaggerated by the fact that, in both Greece and China, many of the first philosophers (including Confucius and Plato) saw themselves as teachers of administrators, and so thought disproportionately about such matters. The few people who did invent things, like storytellers, must have seemed an outlying data point that could be ignored.

[253] . The only people who lost were us. The angels had convertible debt, so they had first claim on the proceeds of the auction. Y Combinator only got 38 cents on the dollar.

[254] . The best kind of organization for that might be an open source project, but those don’t involve a lot of face to face meetings. Maybe it would be worth starting one that did.

[255] . There need to be some number of big companies to acquire the startups, so the number of big companies couldn’t decrease to zero.

[256] . Thought experiment: If doctors did the same work, but as impoverished outcasts, which parents would still want their kids to be doctors?

[257] . It doesn’t take a conscious effort to make software incompatible. All you have to do is not work too hard at fixing bugs–which, if you’re a big company, you produce in copious quantities. The situation is analogous to the writing of “literary theorists.” Most don’t try to be obscure; they just don’t make an effort to be clear. It wouldn’t pay.

[258] . In part because Steve Jobs got pushed out by John Sculley in a way that’s rare among technology companies. If Apple’s board hadn’t made that blunder, they wouldn’t have had to bounce back. Portuguese Translation Simplified Chinese Translation Korean Translation * * *

[259] . I may be underestimating VCs. They may play some behind the scenes role in IPOs, which you ultimately need if you want to create a silicon valley.

[260] . A few VCs have an email address you can send your business plan to, but the number of startups that get funded this way is basically zero. You should always get a personal introduction–and to a partner, not an associate.

[261] . Several people have told us that the most valuable thing about startup school was that they got to see famous startup founders and realized they were just ordinary guys. Though we’re happy to provide this service, this is not generally the way we pitch startup school to potential speakers.

[262] . Actually this sounds to me like a VC who got buyer’s remorse, then used a technicality to get out of the deal. But it’s telling that it even seemed a plausible excuse.

[263] . This is why we can’t believe anyone would think Y Combinator was a bad deal. Does anyone really think we’re so useless that in three months we can’t improve a startup’s prospects by 7.5%?

[264] . The obvious choice for your present valuation is the post-money valuation of your last funding round. This probably undervalues the company, though, because (a) unless your last round just happened, the company is presumably worth more, and (b) the valuation of an early funding round usually reflects some other contribution by the investors.

[265] . Is what we measure worth measuring? I think so. You can get rich simply by being energetic and unscrupulous, but getting rich from a technology startup takes some amount of brains. It is just the kind of work the upper middle class values; it has about the same intellectual component as being a doctor.

[266] . Actually, someone did, once. Mitch Kapor’s wife Freada was in charge of HR at Lotus in the early years. (As he is at pains to point out, they did not become romantically involved till afterward.) At one point they worried Lotus was losing its startup edge and turning into a big company. So as an experiment she sent their recruiters the resumes of the first 40 employees, with identifying details changed. These were the people who had made Lotus into the star it was. Not one got an interview.

[267] . The US News list? Surely no one trusts that. Even if the statistics they consider are useful, how do they decide on the relative weights? The reason the US News list is meaningful is precisely because they are so intellectually dishonest in that respect. There is no external source they can use to calibrate the weighting of the statistics they use; if there were, we could just use that instead. What they must do is adjust the weights till the top schools are the usual suspects in about the right order. So in effect what the US News list tells us is what the editors think the top schools are, which is probably not far from the conventional wisdom on the matter. The amusing thing is, because some schools work hard to game the system, the editors will have to keep tweaking their algorithm to get the rankings they want.

[268] . Possible doesn’t mean easy, of course. A smart student at a party school will inevitably be something of an outcast, just as he or she would be in most high schools.

[269] . In practice formal logic is not much use, because despite some progress in the last 150 years we’re still only able to formalize a small percentage of statements. We may never do that much better, for the same reason 1980s-style “knowledge representation” could never have worked; many statements may have no representation more concise than a huge, analog brain state.

[270] . It was harder for Darwin’s contemporaries to grasp this than we can easily imagine. The story of creation in the Bible is not just a Judeo-Christian concept; it’s roughly what everyone must have believed since before people were people. The hard part of grasping evolution was to realize that species weren’t, as they seem to be, unchanging, but had instead evolved from different, simpler organisms over unimaginably long periods of time. Now we don’t have to make that leap. No one in an industrialized country encounters the idea of evolution for the first time as an adult. Everyone’s taught about it as a child, either as truth or heresy.

[271] . Greek philosophers before Plato wrote in verse. This must have affected what they said. If you try to write about the nature of the world in verse, it inevitably turns into incantation. Prose lets you be more precise, and more tentative.

[272] . Philosophy is like math’s ne’er-do-well brother. It was born when Plato and Aristotle looked at the works of their predecessors and said in effect “why can’t you be more like your brother?” Russell was still saying the same thing 2300 years later. Math is the precise half of the most abstract ideas, and philosophy the imprecise half. It’s probably inevitable that philosophy will suffer by comparison, because there’s no lower bound to its precision. Bad math is merely boring, whereas bad philosophy is nonsense. And yet there are some good ideas in the imprecise half.

[273] . Aristotle’s best work was in logic and zoology, both of which he can be said to have invented. But the most dramatic departure from his predecessors was a new, much more analytical style of thinking. He was arguably the first scientist.

[274] . Brooks, Rodney, Programming in Common Lisp , Wiley, 1985, p. 94.

[275] . Some would say we depend on Aristotle more than we realize, because his ideas were one of the ingredients in our common culture. Certainly a lot of the words we use have a connection with Aristotle, but it seems a bit much to suggest that we wouldn’t have the concept of the essence of something or the distinction between matter and form if Aristotle hadn’t written about them. One way to see how much we really depend on Aristotle would be to diff European culture with Chinese: what ideas did European culture have in 1800 that Chinese culture didn’t, in virtue of Aristotle’s contribution?

[276] . The meaning of the word “philosophy” has changed over time. In ancient times it covered a broad range of topics, comparable in scope to our “scholarship” (though without the methodological implications). Even as late as Newton’s time it included what we now call “science.” But core of the subject today is still what seemed to Aristotle the core: the attempt to discover the most general truths. Aristotle didn’t call this “metaphysics.” That name got assigned to it because the books we now call the Metaphysics came after (meta = after) the Physics in the standard edition of Aristotle’s works compiled by Andronicus of Rhodes three centuries later. What we call “metaphysics” Aristotle called “first philosophy.”

[277] . Some of Aristotle’s immediate successors may have realized this, but it’s hard to say because most of their works are lost.

[278] . Sokal, Alan, “Transgressing the Boundaries: Toward a Transformative Hermeneutics of Quantum Gravity,” Social Text 46/47, pp. 217-252. Abstract-sounding nonsense seems to be most attractive when it’s aligned with some axe the audience already has to grind. If this is so we should find it’s most popular with groups that are (or feel) weak. The powerful don’t need its reassurance.

[279] . Letter to Ottoline Morrell, December 1912. Quoted in: Monk, Ray, Ludwig Wittgenstein: The Duty of Genius , Penguin, 1991, p. 75.

[280] . A preliminary result, that all metaphysics between Aristotle and 1783 had been a waste of time, is due to I. Kant.

[281] . Wittgenstein asserted a sort of mastery to which the inhabitants of early 20th century Cambridge seem to have been peculiarly vulnerable–perhaps partly because so many had been raised religious and then stopped believing, so had a vacant space in their heads for someone to tell them what to do (others chose Marx or Cardinal Newman), and partly because a quiet, earnest place like Cambridge in that era had no natural immunity to messianic figures, just as European politics then had no natural immunity to dictators.

[282] . This is actually from the Ordinatio of Duns Scotus (ca. 1300), with “number” replaced by “gender.” Plus ca change. Wolter, Allan (trans), Duns Scotus: Philosophical Writings , Nelson, 1963, p. 92.

[283] . Frankfurt, Harry, On Bullshit , Princeton University Press, 2005.

[284] . Some introductions to philosophy now take the line that philosophy is worth studying as a process rather than for any particular truths you’ll learn. The philosophers whose works they cover would be rolling in their graves at that. They hoped they were doing more than serving as examples of how to argue: they hoped they were getting results. Most were wrong, but it doesn’t seem an impossible hope. This argument seems to me like someone in 1500 looking at the lack of results achieved by alchemy and saying its value was as a process. No, they were going about it wrong. It turns out it is possible to transmute lead into gold (though not economically at current energy prices), but the route to that knowledge was to backtrack and try another approach.

[285] . The nationalistic idea is the converse: that startups should stay in a certain city because of the country it’s in. If you really have a “one world” viewpoint, deciding to move from London to Silicon Valley is no different from deciding to move from Chicago to Silicon Valley.

[286] . An investor who merely seems like he will fund you, however, you can ignore. Seeming like they will fund you one day is the way investors say No.

[287] . I mean forum in the general sense of a place to exchange views. The original Internet forums were not web sites but Usenet newsgroups.

[288] . I’m talking here about everyday tagging. Some graffiti is quite impressive (anything becomes art if you do it well enough) but the median tag is just visual spam. Russian Translation * * *

[289] . When I talk about humans being meant or designed to live a certain way, I mean by evolution.

[290] . It’s not only the leaves who suffer. The constraint propagates up as well as down. So managers are constrained too; instead of just doing things, they have to act through subordinates.

[291] . Do not finance your startup with credit cards. Financing a startup with debt is usually a stupid move, and credit card debt stupidest of all. Credit card debt is a bad idea, period. It is a trap set by evil companies for the desperate and the foolish.

[292] . The founders we fund used to be younger (initially we encouraged undergrads to apply), and the first couple times I saw this I used to wonder if they were actually getting physically taller.

[293] . Another tip: If you want to get all that value, don’t destroy the startup after you buy it. Give the founders enough autonomy that they can grow the acquisition into what it would have become.

[294] . Fifty years ago it would have seemed shocking for a public company not to pay dividends. Now many tech companies don’t. The markets seem to have figured out how to value potential dividends. Maybe that isn’t the last step in this evolution. Maybe markets will eventually get comfortable with potential earnings. (VCs already are, and at least some of them consistently make money.) I realize this sounds like the stuff one used to hear about the “new economy” during the Bubble. Believe me, I was not drinking that kool-aid at the time. But I’m convinced there were some good ideas buried in Bubble thinking. For example, it’s ok to focus on growth instead of profits–but only if the growth is genuine. You can’t be buying users; that’s a pyramid scheme. But a company with rapid, genuine growth is valuable, and eventually markets learn how to value valuable things.

[295] . The idea of starting a company with benevolent aims is currently undervalued, because the kind of people who currently make that their explicit goal don’t usually do a very good job. It’s one of the standard career paths of trustafarians to start some vaguely benevolent business. The problem with most of them is that they either have a bogus political agenda or are feebly executed. The trustafarians’ ancestors didn’t get rich by preserving their traditional culture; maybe people in Bolivia don’t want to either. And starting an organic farm, though it’s at least straightforwardly benevolent, doesn’t help people on the scale that Google does. Most explicitly benevolent projects don’t hold themselves sufficiently accountable. They act as if having good intentions were enough to guarantee good effects.

[296] . Users dislike their new operating system so much that they’re starting petitions to save the old one. And the old one was nothing special. The hackers within Microsoft must know in their hearts that if the company really cared about users they’d just advise them to switch to OSX.

[297] . One reason I stuck with such a brutally simple word is that the lies we tell kids are probably not quite as harmless as we think. If you look at what adults told children in the past, it’s shocking how much they lied to them. Like us, they did it with the best intentions. So if we think we’re as open as one could reasonably be with children, we’re probably fooling ourselves. Odds are people in 100 years will be as shocked at some of the lies we tell as we are at some of the lies people told 100 years ago. I can’t predict which these will be, and I don’t want to write an essay that will seem dumb in 100 years. So instead of using special euphemisms for lies that seem excusable according to present fashions, I’m just going to call all our lies lies. (I have omitted one type: lies told to play games with kids’ credulity. These range from “make-believe,” which is not really a lie because it’s told with a wink, to the frightening lies told by older siblings. There’s not much to say about these: I wouldn’t want the first type to go away, and wouldn’t expect the second type to.)

[298] . Calaprice, Alice (ed.), The Quotable Einstein , Princeton University Press, 1996.

[299] . If you ask parents why kids shouldn’t swear, the less educated ones usually reply with some question-begging answer like “it’s inappropriate,” while the more educated ones come up with elaborate rationalizations. In fact the less educated parents seem closer to the truth.

[300] . As a friend with small children pointed out, it’s easy for small children to consider themselves immortal, because time seems to pass so slowly for them. To a 3 year old, a day feels like a month might to an adult. So 80 years sounds to him like 2400 years would to us.

[301] . I realize I’m going to get endless grief for classifying religion as a type of lie. Usually people skirt that issue with some equivocation implying that lies believed for a sufficiently long time by sufficiently large numbers of people are immune to the usual standards for truth. But because I can’t predict which lies future generations will consider inexcusable, I can’t safely omit any type we tell. Yes, it seems unlikely that religion will be out of fashion in 100 years, but no more unlikely than it would have seemed to someone in 1880 that schoolchildren in 1980 would be taught that masturbation was perfectly normal and not to feel guilty about it.

[302] . Unfortunately the payload can consist of bad customs as well as good ones. For example, there are certain qualities that some groups in America consider “acting white.” In fact most of them could as accurately be called “acting Japanese.” There’s nothing specifically white about such customs. They’re common to all cultures with long traditions of living in cities. So it is probably a losing bet for a group to consider behaving the opposite way as part of its identity.

[303] . In this context, “issues” basically means “things we’re going to lie to them about.” That’s why there’s a special name for these topics.

[304] . Mayle, Peter, Why Are We Getting a Divorce? , Harmony, 1988.

[305] . The ironic thing is, this is also the main reason kids lie to adults. If you freak out when people tell you alarming things, they won’t tell you them. Teenagers don’t tell their parents what happened that night they were supposed to be staying at a friend’s house for the same reason parents don’t tell 5 year olds the truth about the Thanksgiving turkey. They’d freak if they knew.

[306] . This is one of the advantages of not having the universities in your country controlled by the government. When governments decide how to allocate resources, political deal-making causes things to be spread out geographically. No central goverment would put its two best universities in the same town, unless it was the capital (which would cause other problems). But scholars seem to like to cluster together as much as people in any other field, and when given the freedom to they derive the same advantages from it.

[307] . There are still a few old professors in Palo Alto, but one by one they die and their houses are transformed by developers into McMansions and sold to VPs of Bus Dev.

[308] . How many times have you read about startup founders who continued to live inexpensively as their companies took off? Who continued to dress in jeans and t-shirts, to drive the old car they had in grad school, and so on? If you did that in New York, people would treat you like shit. If you walk into a fancy restaurant in San Francisco wearing a jeans and a t-shirt, they’re nice to you; who knows who you might be? Not in New York. One sign of a city’s potential as a technology center is the number of restaurants that still require jackets for men. According to Zagat’s there are none in San Francisco, LA, Boston, or Seattle, 4 in DC, 6 in Chicago, 8 in London, 13 in New York, and 20 in Paris. (Zagat’s lists the Ritz Carlton Dining Room in SF as requiring jackets but I couldn’t believe it, so I called to check and in fact they don’t. Apparently there’s only one restaurant left on the entire West Coast that still requires jackets: The French Laundry in Napa Valley.)

[309] . Ideas are one step upstream from economic power, so it’s conceivable that intellectual centers like Cambridge will one day have an edge over Silicon Valley like the one the Valley has over New York. This seems unlikely at the moment; if anything Boston is falling further and further behind. The only reason I even mention the possibility is that the path from ideas to startups has recently been getting smoother. It’s a lot easier now for a couple of hackers with no business experience to start a startup than it was 10 years ago. If you extrapolate another 20 years, maybe the balance of power will start to shift back. I wouldn’t bet on it, but I wouldn’t bet against it either.

[310] . If Paris is where people care most about art, why is New York the center of gravity of the art business? Because in the twentieth century, art as brand split apart from art as stuff. New York is where the richest buyers are, but all they demand from art is brand, and since you can base brand on anything with a sufficiently identifiable style, you may as well use the local stuff.

[311] . When investors can’t make up their minds, they sometimes describe it as if it were a property of the startup. “You’re too early for us,” they sometimes say. But which of them, if they were taken back in a time machine to the hour Google was founded, wouldn’t offer to invest at any valuation the founders chose? An hour old is not too early if it’s the right startup. What “you’re too early” really means is “we can’t figure out yet whether you’ll succeed.”

[312] . Investors influence one another both directly and indirectly. They influence one another directly through the “buzz” that surrounds a hot startup. But they also influence one another indirectly through the founders. When a lot of investors are interested in you, it increases your confidence in a way that makes you much more attractive to investors. No VC will admit they’re influenced by buzz. Some genuinely aren’t. But there are few who can say they’re not influenced by confidence.

[313] . One VC who read this essay wrote: “We try to avoid companies that got bootstrapped with consulting. It creates very bad behaviors/instincts that are hard to erase from a company’s culture.”

[314] . The optimal way to answer the first question is to say that it would be improper to name names, while simultaneously implying that you’re talking to a bunch of other VCs who are all about to give you term sheets. If you’re the sort of person who understands how to do that, go ahead. If not, don’t even try. Nothing annoys VCs more than clumsy efforts to manipulate them.

[315] . The disadvantage of expanding a round on the fly is that the valuation is fixed at the start, so if you get a sudden rush of interest, you may have to decide between turning some investors away and selling more of the company than you meant to. That’s a good problem to have, however.

[316] . I wouldn’t say that intelligence doesn’t matter in startups. We’re only comparing YC startups, who’ve already made it over a certain threshold.

[317] . But not all are. Though most VCs are suits at heart, the most successful ones tend not to be. Oddly enough, the best VCs tend to be the least VC-like.

[318] . One of the bizarre consequences of this model was that the usual way to make more money was to become a manager. This is one of the things startups fix.

[319] . There are a lot of reasons American car companies have been doing so much worse than Japanese car companies, but at least one of them is a cause for optimism: American graduates have more options.

[320] . It’s possible that companies will one day be able to grow big in revenues without growing big in people, but we are not very far along that trend yet.

[321] . Lecuyer, Christophe, Making Silicon Valley , MIT Press, 2006.

[322] . Miyazaki, Ichisada (Conrad Schirokauer trans.), China’s Examination Hell: The Civil Service Examinations of Imperial China, Yale University Press, 1981. Scribes in ancient Egypt took exams, but they were more the type of proficiency test any apprentice might have to pass.

[323] . When I say the raison d’etre of prep schools is to get kids into better colleges, I mean this in the narrowest sense. I’m not saying that’s all prep schools do, just that if they had zero effect on college admissions there would be far less demand for them.

[324] . Progressive tax rates will tend to damp this effect, however, by decreasing the difference between good and bad measurers.

[325] . When that happens, it tends to happen fast, like a core going critical. The threshold for participating goes down to zero, which brings in more people. And they tend to say incendiary things, which draw more and angrier counterarguments.

[326] . There may be some things it’s a net win to include in your identity. For example, being a scientist. But arguably that is more of a placeholder than an actual label–like putting NMI on a form that asks for your middle initial– because it doesn’t commit you to believing anything in particular. A scientist isn’t committed to believing in natural selection in the same way a biblical literalist is committed to rejecting it. All he’s committed to is following the evidence wherever it leads. Considering yourself a scientist is equivalent to putting a sign in a cupboard saying “this cupboard must be kept empty.” Yes, strictly speaking, you’re putting something in the cupboard, but not in the ordinary sense.

[327] . Strictly speaking it’s impossible without a time machine.

[328] . In practice it’s more like a ragged comb.

[329] . Joe thinks one of the founders of Hewlett Packard said it first, but he doesn’t remember which.

[330] . They’d be interchangeable if markets stood still. Since they don’t, working twice as fast is better than having twice as much time. Turkish Translation Spanish Translation Bulgarian Translation Japanese Translation Persian Translation * * *

[331] . I tried ranking users by both average and median comment score, and average (with the high score thrown out) seemed the more accurate predictor of high quality. Median may be the more accurate predictor of low quality though.

[332] . Another thing I learned from this experiment is that if you’re going to distinguish between people, you better be sure you do it right. This is one problem where rapid prototyping doesn’t work. Indeed, that’s the intellectually honest argument for not discriminating between various types of people. The reason not to do it is not that everyone’s the same, but that it’s bad to do wrong and hard to do right.

[333] . When I catch egregiously linkjacked posts I replace the url with that of whatever they copied. Sites that habitually linkjack get banned.

[334] . Digg is notorious for its lack of transparency. The root of the problem is not that the guys running Digg are especially sneaky, but that they use the wrong algorithm for generating their frontpage. Instead of bubbling up from the bottom as they get more votes, as on Reddit, stories start at the top and get pushed down by new arrivals. The reason for the difference is that Digg is derived from Slashdot, while Reddit is derived from Delicious/popular. Digg is Slashdot with voting instead of editors, and Reddit is Delicious/popular with voting instead of bookmarking. (You can still see fossils of their origins in their graphic design.) Digg’s algorithm is very vulnerable to gaming, because any story that makes it onto the frontpage is the new top story. Which in turn forces Digg to respond with extreme countermeasures. A lot of startups have some kind of secret about the subterfuges they had to resort to in the early days, and I suspect Digg’s is the extent to which the top stories were de facto chosen by human editors.

[335] . The dialog on Beavis and Butthead was composed largely of these, and when I read comments on really bad sites I can hear them in their voices.

[336] . I suspect most of the techniques for discouraging stupid comments have yet to be discovered. Xkcd implemented a particularly clever one in its IRC channel: don’t allow the same thing twice. Once someone has said “fail,” no one can ever say it again. This would penalize short comments especially, because they have less room to avoid collisions in. Another promising idea is the stupid filter, which is just like a probabilistic spam filter, but trained on corpora of stupid and non-stupid comments instead. You may not have to kill bad comments to solve the problem. Comments at the bottom of a long thread are rarely seen, so it may be enough to incorporate a prediction of quality in the comment sorting algorithm.

[337] . What makes most suburbs so demoralizing is that there’s no center to walk to.

[338] . What people who start these supposedly local seed firms always find is that (a) their applicants come from all over, not just the local area, and (b) the local startups also apply to the other seed firms. So what ends up happening is that the applicant pool gets partitioned by quality rather than geography.

[339] . Interestingly, the bad VCs fail by choosing startups run by people like them–people who are good presenters, but have no real substance. It’s a case of the fake leading the fake. And since everyone involved is so plausible, the LPs who invest in these funds have no idea what’s happening till they measure their returns.

[340] . Not even being a tax haven, I suspect. That makes some rich people move, but not the type who would make good angel investors in startups.

[341] . Thanks to Michael Keenan for pointing this out.

[342] . Thanks to Trevor Blackwell for this point. He adds: “I remember the eyes of phone companies gleaming in the early 90s when they talked about convergence. They thought most programming would be on demand, and they would implement it and make a lot of money. It didn’t work out. They assumed that their local network infrastructure would be critical to do video on-demand, because you couldn’t possibly stream it from a few data centers over the internet. At the time (1992) the entire cross-country Internet bandwidth wasn’t enough for one video stream. But wide-area bandwidth increased more than they expected and they were beaten by iTunes and Hulu.”

[343] . Copyright owners tend to focus on the aspect they see of piracy, which is the lost revenue. They therefore think what drives users to do it is the desire to get something for free. But iTunes shows that people will pay for stuff online, if you make it easy. A significant component of piracy is simply that it offers a better user experience.

[344] . Or a phone that is actually a computer. I’m not making any predictions about the size of the device that will replace TV, just that it will have a browser and get data via the Internet.

[345] . Emmett Shear writes: “I’d argue the long tail for sports may be even larger than the long tail for other kinds of content. Anyone can broadcast a high school football game that will be interesting to 10,000 people or so, even if the quality of production is not so good.”

[346] . Convertible debt can be either capped at a particular valuation, or can be done at a discount to whatever the valuation turns out to be when it converts. E.g. convertible debt at a discount of 30% means when it converts you get stock as if you’d invested at a 30% lower valuation. That can be useful in cases where you can’t or don’t want to figure out what the valuation should be. You leave it to the next investor. On the other hand, a lot of investors want to know exactly what they’re getting, so they will only do convertible debt with a cap.

[347] . The expensive part of creating an agreement from scratch is not writing the agreement, but bickering at several hundred dollars an hour over the details. That’s why the series AA paperwork aims at a middle ground. You can just start from the compromise you’d have reached after lots of back and forth. When you fund a startup, both your lawyers should be specialists in startups. Do not use ordinary corporate lawyers for this. Their inexperience makes them overbuild: they’ll create huge, overcomplicated agreements, and spend hours arguing over irrelevant things. In the Valley, the top startup law firms are Wilson Sonsini, Orrick, Fenwick & West, Gunderson Dettmer, and Cooley Godward. In Boston the best are Goodwin Procter, Wilmer Hale, and Foley Hoag.

[348] . Your mileage may vary.

[349] . These anti-dilution provisions also protect you against tricks like a later investor trying to steal the company by doing another round that values the company at $1. If you have a competent startup lawyer handle the deal for you, you should be protected against such tricks initially. But it could become a problem later. If a big VC firm wants to invest in the startup after you, they may try to make you take out your anti-dilution protections. And if they do the startup will be pressuring you to agree. They’ll tell you that if you don’t, you’re going to kill their deal with the VC. I recommend you solve this problem by having a gentlemen’s agreement with the founders: agree with them in advance that you’re not going to give up your anti-dilution protections. Then it’s up to them to tell VCs early on. The reason you don’t want to give them up is the following scenario. The VCs recapitalize the company, meaning they give it additional funding at a pre- money valuation of zero. This wipes out the existing shareholders, including both you and the founders. They then grant the founders lots of options, because they need them to stay around, but you get nothing. Obviously this is not a nice thing to do. It doesn’t happen often. Brand-name VCs wouldn’t recapitalize a company just to steal a few percent from an angel. But there’s a continuum here. A less upstanding, lower-tier VC might be tempted to do it to steal a big chunk of stock. I’m not saying you should always absolutely refuse to give up your anti- dilution protections. Everything is a negotiation. If you’re part of a powerful syndicate, you might be able to give up legal protections and rely on social ones. If you invest in a deal led by a big angel like Ron Conway, for example, you’re pretty well protected against being mistreated, because any VC would think twice before crossing him. This kind of protection is one of the reasons angels like to invest in syndicates.

[350] . Don’t invest so much, or at such a low valuation, that you end up with an excessively large share of a startup, unless you’re sure your money will be the last they ever need. Later stage investors won’t invest in a company if the founders don’t have enough equity left to motivate them. I talked to a VC recently who said he’d met with a company he really liked, but he turned them down because investors already owned more than half of it. Those investors probably thought they’d been pretty clever by getting such a large chunk of this desirable company, but in fact they were shooting themselves in the foot.

[351] . At any given time I know of at least 3 or 4 YC alumni who I believe will be big successes but who are running on vapor, financially, because investors don’t yet get what they’re doing. (And no, unfortunately, I can’t tell you who they are. I can’t refer a startup to an investor I don’t know.)

[352] . There are some VCs who can predict instead of reacting. Not surprisingly, these are the most successful ones.

[353] . It’s somewhat sneaky of me to put it this way, because the median VC loses money. That’s one of the most surprising things I’ve learned about VC while working on Y Combinator. Only a fraction of VCs even have positive returns. The rest exist to satisfy demand among fund managers for venture capital as an asset class. Learning this explained a lot about some of the VCs I encountered when we were working on Viaweb.

[354] . VCs also generally say they prefer great markets to great people. But what they’re really saying is they want both. They’re so selective that they only even consider great people. So when they say they care above all about big markets, they mean that’s how they choose between great people.

[355] . Founders rightly dislike the sort of investor who says he’s interested in investing but doesn’t want to lead. There are circumstances where this is an acceptable excuse, but more often than not what it means is “No, but if you turn out to be a hot deal, I want to be able to claim retroactively I said yes.” If you like a startup enough to invest in it, then invest in it. Just use the standard series AA terms and write them a check.

[356] . I think the reason the dictionaries are wrong is that the meaning of the word has shifted. No one writing a dictionary from scratch today would say that hapless meant unlucky. But a couple hundred years ago they might have. People were more at the mercy of circumstances in the past, and as a result a lot of the words we use for good and bad outcomes have origins in words about luck. When I was living in Italy, I was once trying to tell someone that I hadn’t had much success in doing something, but I couldn’t think of the Italian word for success. I spent some time trying to describe the word I meant. Finally she said “Ah! Fortuna!”

[357] . There are aspects of startups where the recipe is to be actively curious. There can be times when what you’re doing is almost pure discovery. Unfortunately these times are a small proportion of the whole. On the other hand, they are in research too.

[358] . I’d almost say to most people, but I realize (a) I have no idea what most people are like, and (b) I’m pathologically optimistic about people’s ability to change.

[359] . There are two very different types of startup: one kind that evolves naturally, and one kind that’s called into being to “commercialize” a scientific discovery. Most computer/software startups are now the first type, and most pharmaceutical startups the second. When I talk about startups in this essay, I mean type I startups. There is no difficulty making type II startups spread: all you have to do is fund medical research labs; commercializing whatever new discoveries the boffins throw off is as straightforward as building a new airport. Type II startups neither require nor produce startup culture. But that means having type II startups won’t get you type I startups. Philadelphia is a case in point: lots of type II startups, but hardly any type I. Incidentally, Google may appear to be an instance of a type II startup, but it wasn’t. Google is not pagerank commercialized. They could have used another algorithm and everything would have turned out the same. What made Google Google is that they cared about doing search well at a critical point in the evolution of the web.

[360] . Watt didn’t invent the steam engine. His critical invention was a refinement that made steam engines dramatically more efficient: the separate condenser. But that oversimplifies his role. He had such a different attitude to the problem and approached it with such energy that he transformed the field. Perhaps the most accurate way to put it would be to say that Watt reinvented the steam engine.

[361] . The biggest counterexample here is Skype. If you’re doing something that would get shut down in the US, it becomes an advantage to be located elsewhere. That’s why Kazaa took the place of Napster. And the expertise and connections the founders gained from running Kazaa helped ensure the success of Skype.

[362] . The “ramen” in “ramen profitable” refers to instant ramen, which is just about the cheapest food available. Please do not take the term literally. Living on instant ramen would be very unhealthy. Rice and beans are a better source of food. Start by investing in a rice cooker, if you don’t have one. Rice and Beans for 2n [code] olive oil or butter n yellow onions other fresh vegetables; experiment 3n cloves garlic n 12-oz cans white, kidney, or black beans n cubes Knorr beef or vegetable bouillon n teaspoons freshly ground black pepper 3n teaspoons ground cumin n cups dry rice, preferably brown [/code] Put rice in rice cooker. Add water as specified on rice package. (Default: 2 cups water per cup of rice.) Turn on rice cooker and forget about it. Chop onions and other vegetables and fry in oil, over fairly low heat, till onions are glassy. Put in chopped garlic, pepper, cumin, and a little more fat, and stir. Keep heat low. Cook another 2 or 3 minutes, then add beans (don’t drain the beans), and stir. Throw in the bouillon cube(s), cover, and cook on lowish heat for at least 10 minutes more. Stir vigilantly to avoid sticking. If you want to save money, buy beans in giant cans from discount stores. Spices are also much cheaper when bought in bulk. If there’s an Indian grocery store near you, they’ll have big bags of cumin for the same price as the little jars in supermarkets.

[363] . There’s a good chance that a shift in power from investors to founders would actually increase the size of the venture business. I think investors currently err too far on the side of being harsh to founders. If they were forced to stop, the whole venture business would work better, and you might see something like the increase in trade you always see when restrictive laws are removed. Investors are one of the biggest sources of pain for founders; if they stopped causing so much pain, it would be better to be a founder; and if it were better to be a founder, more people would do it.

[364] . It’s conceivable that a startup could grow big by transforming consulting into a form that would scale. But if they did that they’d really be a product company.

[365] . Loosely speaking. What I’m claiming with the melon seed model is more like determination is proportionate to wd^m - k|w - d|^n, where w is will and d discipline.

[366] . Which means one of the best ways to help a society generally is to create events and institutions that bring ambitious people together. It’s like pulling the control rods out of a reactor: the energy they emit encourages other ambitious people, instead of being absorbed by the normal people they’re usually surrounded with. Conversely, it’s probably a mistake to do as some European countries have done and try to ensure none of your universities is significantly better than the others.

[367] . For example, willfulness clearly has two subcomponents, stubbornness and energy. The first alone yields someone who’s stubbornly inert. The second alone yields someone flighty. As willful people get older or otherwise lose their energy, they tend to become merely stubborn.

[368] . Articles of this type are also startlingly popular on Delicious, but I think that’s because delicious/popular is driven by bookmarking, not because Delicious users are stupid. Delicious users are collectors, and a list of n things seems particularly collectible because it’s a collection itself.

[369] . Most “word problems” in school math textbooks are similarly misleading. They look superficially like the application of math to real problems, but they’re not. So if anything they reinforce the impression that math is merely a complicated but pointless collection of stuff to be memorized. Russian Translation * * *

[370] . I don’t like the word “content” and tried for a while to avoid using it, but I have to admit there’s no other word that means the right thing. “Information” is too general. Ironically, the main reason I don’t like “content” is the thesis of this essay. The word suggests an undifferentiated slurry, but economically that’s how both publishers and audiences treat it. Content is information you don’t need.

[371] . Some types of publishers would be at a disadvantage trying to enter the software business. Record labels, for example, would probably find it more natural to expand into casinos than software, because the kind of people who run them would be more at home at the mafia end of the business spectrum than the don’t-be-evil end.

[372] . I never watch movies in theaters anymore. The tipping point for me was the ads they show first.

[373] . Unfortunately, making physically nice books will only be a niche within a niche. Publishers are more likely to resort to expedients like selling autographed copies, or editions with the buyer’s picture on the cover.

[374] . I had a strange feeling of being back in high school writing this. To get a good grade you had to both write the sort of pious crap you were expected to, but also seem to be writing with conviction. The solution was a kind of method acting. It was revoltingly familiar to slip back into it.

[375] . Exercise for the reader: rephrase that thought to please the same people the first version would offend.

[376] . Come to think of it, there is one way in which I deliberately pander to readers, because it doesn’t change the number of words: I switch person. This flattering distinction seems so natural to the average reader that they probably don’t notice even when I switch in mid-sentence, though you tend to notice when it’s done as conspicuously as this.

[377] . Graduate students might understand it. In grad school you always feel you should be working on your thesis. It doesn’t end every semester like classes do.

[378] . The best way for a startup to engage with slow-moving organizations is to fork off separate processes to deal with them. It’s when they’re on the critical path that they kill you–when you depend on closing a deal to move forward. It’s worth taking extreme measures to avoid that.

[379] . This is a variant of Reid Hoffman’s principle that if you aren’t embarrassed by what you launch with, you waited too long to launch.

[380] . The question to ask about what you’ve built is not whether it’s good, but whether it’s good enough to supply the activation energy required.

[381] . Some VCs seem to understand technology because they actually do, but that’s overkill; the defining test is whether you can talk about it well enough to convince limited partners.

[382] . This is the same phenomenon you see with defense contractors or fashion brands. The dumber the customers, the more effort you expend on the process of selling things to them rather than making the things you sell.

[383] . When Google adopted “Don’t be evil,” they were still so small that no one would have expected them to be, yet.

[384] . The dictator in the 1984 ad isn’t Microsoft, incidentally; it’s IBM. IBM seemed a lot more frightening in those days, but they were friendlier to developers than Apple is now.

[385] . He couldn’t even afford a monitor. That’s why the Apple I used a TV as a monitor.

[386] . Several people I talked to mentioned how much they liked the iPhone SDK. The problem is not Apple’s products but their policies. Fortunately policies are software; Apple can change them instantly if they want to. Handy that, isn’t it?

[387] . This suggests a way to predict areas where Apple will be weak: things Steve Jobs doesn’t use. E.g. I doubt he is much into gaming.

[388] . In retrospect, we should have become direct marketers. If I were doing Viaweb again, I’d open our own online store. If we had, we’d have understood users a lot better. I’d encourage anyone starting a startup to become one of its users, however unnatural it seems.

[389] . Possible exception: It’s hard to compete directly with open source software. You can build things for programmers, but there has to be some part you can charge for.

[390] . No doubt there are already names for this type of thinking, but I call it “ambient thought.”

[391] . This was made particularly clear in our case, because neither of the funds we raised was difficult, and yet in both cases the process dragged on for months. Moving large amounts of money around is never something people treat casually. The attention required increases with the amount–maybe not linearly, but definitely monotonically.

[392] . Corollary: Avoid becoming an administrator, or your job will consist of dealing with money and disputes.

[393] . Letter to Oldenburg, quoted in Westfall, Richard, Life of Isaac Newton , p. 107.

[394] . Could you restrict technological progress to areas where you wanted it? Only in a limited way, without becoming a police state. And even then your restrictions would have undesirable side effects. “Good” and “bad” technological progress aren’t sharply differentiated, so you’d find you couldn’t slow the latter without also slowing the former. And in any case, as Prohibition and the “war on drugs” show, bans often do more harm than good.

[395] . Technology has always been accelerating. By Paleolithic standards, technology evolved at a blistering pace in the Neolithic period.

[396] . Unless we mass produce social customs. I suspect the recent resurgence of evangelical Christianity in the US is partly a reaction to drugs. In desperation people reach for the sledgehammer; if their kids won’t listen to them, maybe they’ll listen to God. But that solution has broader consequences than just getting kids to say no to drugs. You end up saying no to science as well. I worry we may be heading for a future in which only a few people plot their own itinerary through no-land, while everyone else books a package tour. Or worse still, has one booked for them by the government.

[397] . People commonly use the word “procrastination” to describe what they do on the Internet. It seems to me too mild to describe what’s happening as merely not-doing-work. We don’t call it procrastination when someone gets drunk instead of working.

[398] . Several people have told me they like the iPad because it lets them bring the Internet into situations where a laptop would be too conspicuous. In other words, it’s a hip flask. (This is true of the iPhone too, of course, but this advantage isn’t as obvious because it reads as a phone, and everyone’s used to those.)

[399] . In this essay I’m talking mainly about software startups. These points don’t apply to types of startups that are still expensive to start, e.g. in energy or biotech. Even the cheap kinds of startups will generally raise large amounts at some point, when they want to hire a lot of people. What has changed is how much they can get done before that.

[400] . It’s not the distribution of good startups that has a power law dropoff, but the distribution of potentially good startups, which is to say, good deals. There are lots of potential winners, from which a few actual winners emerge with superlinear certainty.

[401] . As I was writing this, I asked some founders who’d taken series A rounds from top VC funds whether it was worth it, and they unanimously said yes. The quality of investor is more important than the type of round, though. I’d take an angel round from good angels over a series A from a mediocre VC.

[402] . Founders also worry that taking an angel investment from a VC means they’ll look bad if the VC declines to participate in the next round. The trend of VC angel investing is so new that it’s hard to say how justified this worry is. Another danger, pointed out by Mitch Kapor, is that if VCs are only doing angel deals to generate series A deal flow, then their incentives aren’t aligned with the founders’. The founders want the valuation of the next round to be high, and the VCs want it to be low. Again, hard to say yet how much of a problem this will be.

[403] . Josh Kopelman pointed out that another way to be on fewer boards at once is to take board seats for shorter periods.

[404] . Google was in this respect as so many others the pattern for the future. It would be great for VCs if the similarity extended to returns. That’s probably too much to hope for, but the returns may be somewhat higher, as I explain later.

[405] . Doing a rolling close doesn’t mean the company is always raising money. That would be a distraction. The point of a rolling close is to make fundraising take less time, not more. With a classic fixed sized round, you don’t get any money till all the investors agree, and that often creates a situation where they all sit waiting for the others to act. A rolling close usually prevents this.

[406] . There are two (non-exclusive) causes of hot deals: the quality of the company, and domino effects among investors. The former is obviously a better predictor of success.

[407] . Some of the randomness is concealed by the fact that investment is a self fulfilling prophecy.

[408] . The shift in power to founders is exaggerated now because it’s a seller’s market. On the next downtick it will seem like I overstated the case. But on the next uptick after that, founders will seem more powerful than ever.

[409] . More generally, it will become less common for the same investor to invest in successive rounds, except when exercising an option to maintain their percentage. When the same investor invests in successive rounds, it often means the startup isn’t getting market price. They may not care; they may prefer to work with an investor they already know; but as the investment market becomes more efficient, it will become increasingly easy to get market price if they want it. Which in turn means the investment community will tend to become more stratified.

[410] . The two 10 minuteses have 3 weeks between them so founders can get cheap plane tickets, but except for that they could be adjacent.

[411] . I’m not saying option pools themselves will go away. They’re an administrative convenience. What will go away is investors requiring them.

[412] . The closest we got to targeting when I was there was when we created pets.yahoo.com in order to provoke a bidding war between 3 pet supply startups for the spot as top sponsor.

[413] . In theory you could beat the death spiral by buying good programmers instead of hiring them. You can get programmers who would never have come to you as employees by buying their startups. But so far the only companies smart enough to do this are companies smart enough not to need to.

[414] . I’ve also heard them called “Mini-VCs” and “Micro-VCs.” I don’t know which name will stick. There were a couple predecessors. Ron Conway had angel funds starting in the 1990s, and in some ways First Round Capital is closer to a super-angel than a VC fund.

[415] . It wouldn’t cut their overall returns tenfold, because investing later would probably (a) cause them to lose less on investments that failed, and (b) not allow them to get as large a percentage of startups as they do now. So it’s hard to predict precisely what would happen to their returns.

[416] . The brand of an investor derives mostly from the success of their portfolio companies. The top VCs thus have a big brand advantage over the super-angels. They could make it self-perpetuating if they used it to get all the best new startups. But I don’t think they’ll be able to. To get all the best startups, you have to do more than make them want you. You also have to want them; you have to recognize them when you see them, and that’s much harder. Super-angels will snap up stars that VCs miss. And that will cause the brand gap between the top VCs and the super-angels gradually to erode.

[417] . Though in a traditional series A round VCs put two partners on your board, there are signs now that VCs may begin to conserve board seats by switching to what used to be considered an angel-round board, consisting of two founders and one VC. Which is also to the founders’ advantage if it means they still control the company.

[418] . In a series A round, you usually have to give up more than the actual amount of stock the VCs buy, because they insist you dilute yourselves to set aside an “option pool” as well. I predict this practice will gradually disappear though.

[419] . The best thing for founders, if they can get it, is a convertible note with no valuation cap at all. In that case the money invested in the angel round just converts into stock at the valuation of the next round, no matter how large. Angels and super-angels tend not to like uncapped notes. They have no idea how much of the company they’re buying. If the company does well and the valuation of the next round is high, they may end up with only a sliver of it. So by agreeing to uncapped notes, VCs who don’t care about valuations in angel rounds can make offers that super-angels hate to match.

[420] . Obviously signalling risk is also not a problem if you’ll never need to raise more money. But startups are often mistaken about that.

[421] . I’m not saying it’s impossible to succeed in a city with few other startups, just harder. If you’re sufficiently good at generating your own morale, you can survive without external encouragement. Wufoo was based in Tampa and they succeeded. But the Wufoos are exceptionally disciplined.

[422] . Incidentally, this phenomenon is not limited to startups. Most unusual ambitions fail, unless the person who has them manages to find the right sort of community.

[423] . Starting a company is common, but starting a startup is rare. I’ve talked about the distinction between the two elsewhere, but essentially a startup is a new business designed for scale. Most new businesses are service businesses and except in rare cases those don’t scale.

[424] . As I was writing this, I had a demonstration of the density of startup people in the Valley. Jessica and I bicycled to University Ave in Palo Alto to have lunch at the fabulous Oren’s Hummus. As we walked in, we met Charlie Cheever sitting near the door. Selina Tobaccowala stopped to say hello on her way out. Then Josh Wilson came in to pick up a take out order. After lunch we went to get frozen yogurt. On the way we met Rajat Suri. When we got to the yogurt place, we found Dave Shen there, and as we walked out we ran into Yuri Sagalov. We walked with him for a block or so and we ran into Muzzammil Zaveri, and then a block later we met Aydin Senkut. This is everyday life in Palo Alto. I wasn’t trying to meet people; I was just having lunch. And I’m sure for every startup founder or investor I saw that I knew, there were 5 more I didn’t. If Ron Conway had been with us he would have met 30 people he knew.

[425] . A YC partner wrote: My feeling with the bad groups is that coming into office hours, they’ve already decided what they’re going to do and everything I say is being put through an internal process in their heads, which either desperately tries to munge what I’ve said into something that conforms with their decision or just outright dismisses it and creates a rationalization for doing so. They may not even be conscious of this process but that’s what I think is happening when you say something to bad groups and they have that glazed over look. I don’t think it’s confusion or lack of understanding per se, it’s this internal process at work. With the good groups, you can tell that everything you say is being looked at with fresh eyes and even if it’s dismissed, it’s because of some logical reason e.g. “we already tried that” or “from speaking to our users that isn’t what they’d like,” etc. Those groups never have that glazed over look.

[426] . It’s also one of the most important things VCs fail to understand about startups. Most expect founders to walk in with a clear plan for the future, and judge them based on that. Few consciously realize that in the biggest successes there is the least correlation between the initial plan and what the startup eventually becomes.

[427] . This sentence originally read “GMail is painfully slow.” Thanks to Paul Buchheit for the correction.

[428] . Roger Bannister is famous as the first person to run a mile in under 4 minutes. But his world record only lasted 46 days. Once he showed it could be done, lots of others followed. Ten years later Jim Ryun ran a 3:59 mile as a high school junior.

[429] . If you want to be the next Apple, maybe you don’t even want to start with consumer electronics. Maybe at first you make something hackers use. Or you make something popular but apparently unimportant, like a headset or router. All you need is a bridgehead.

[430] . If you want to learn more about hunter gatherers I strongly recommend Elizabeth Marshall Thomas’s The Harmless People and The Old Way.

[431] . Change in the definition of property is driven mostly by technological progress, however, and since technological progress is accelerating, so presumably will the rate of change in the definition of property. Which means it’s all the more important for societies to be able to respond gracefully to such changes, because they will come at an ever increasing rate.

[432] . As far as I know, the term “copyright colony” was first used by Myles Peterson.

[433] . The state of technology isn’t simply a function of the definition of property. They each constrain the other. But that being so, you can’t mess with the definition of property without affecting (and probably harming) the state of technology. The history of the USSR offers a vivid illustration of that.

[434] . I’m not talking here about academic talks, which are a different type of thing. While the audience at an academic talk might appreciate a joke, they will (or at least should) make a conscious effort to see what new ideas you’re presenting.

[435] . That’s the lower bound. In practice you can often do better, because talks are usually about things you’ve written or talked about before, and when you ad lib, you end up reproducing some of those sentences. Like early medieval architecture, impromptu talks are made of spolia. Which feels a bit dishonest, incidentally, because you have to deliver these sentences as if you’d just thought of them.

[436] . Robert Morris points out that there is a way in which practicing talks makes them better: reading a talk out loud can expose awkward parts. I agree and in fact I read most things I write out loud at least once for that reason.

[437] . For sufficiently small audiences, it may not be true that being part of an audience makes people dumber. The real decline seems to set in when the audience gets too big for the talk to feel like a conversation – maybe around 10 people.

[438] . I’m not saying that the big winners are all that matters, just that they’re all that matters financially for investors. Since we’re not doing YC mainly for financial reasons, the big winners aren’t all that matters to us. We’re delighted to have funded Reddit, for example. Even though we made comparatively little from it, Reddit has had a big effect on the world, and it introduced us to Steve Huffman and Alexis Ohanian, both of whom have become good friends. Nor do we push founders to try to become one of the big winners if they don’t want to. We didn’t “swing for the fences” in our own startup (Viaweb, which was acquired for $50 million), and it would feel pretty bogus to press founders to do something we didn’t do. Our rule is that it’s up to the founders. Some want to take over the world, and some just want that first few million. But we invest in so many companies that we don’t have to sweat any one outcome. In fact, we don’t have to sweat whether startups have exits at all. The biggest exits are the only ones that matter financially, and those are guaranteed in the sense that if a company becomes big enough, a market for its shares will inevitably arise. Since the remaining outcomes don’t have a significant effect on returns, it’s cool with us if the founders want to sell early for a small amount, or grow slowly and never sell (i.e. become a so- called lifestyle business), or even shut the company down. We’re sometimes disappointed when a startup we had high hopes for doesn’t do well, but this disappointment is mostly the ordinary variety that anyone feels when that happens.

[439] . Without visual cues (e.g. the horizon) you can’t distinguish between gravity and acceleration. Which means if you’re flying through clouds you can’t tell what the attitude of the aircraft is. You could feel like you’re flying straight and level while in fact you’re descending in a spiral. The solution is to ignore what your body is telling you and listen only to your instruments. But it turns out to be very hard to ignore what your body is telling you. Every pilot knows about this problem and yet it is still a leading cause of accidents.

[440] . Not all big hits follow this pattern though. The reason Google seemed a bad idea was that there were already lots of search engines and there didn’t seem to be room for another.

[441] . A startup’s success at fundraising is a function of two things: what they’re selling and how good they are at selling it. And while we can teach startups a lot about how to appeal to investors, even the most convincing pitch can’t sell an idea that investors don’t like. I was genuinely worried that Airbnb, for example, would not be able to raise money after Demo Day. I couldn’t convince Fred Wilson to fund them. They might not have raised money at all but for the coincidence that Greg McAdoo, our contact at Sequoia, was one of a handful of VCs who understood the vacation rental business, having spent much of the previous two years investigating it.

[442] . I calculated it once for the last batch before a consortium of investors started offering investment automatically to every startup we funded, summer 2010. At the time it was 94% (33 of 35 companies that tried to raise money succeeded, and one didn’t try because they were already profitable). Presumably it’s lower now because of that investment; in the old days it was raise after Demo Day or die.

[443] . Strictly speaking it’s not lots of customers you need but a big market, meaning a high product of number of customers times how much they’ll pay. But it’s dangerous to have too few customers even if they pay a lot, or the power that individual customers have over you could turn you into a de facto consulting firm. So whatever market you’re in, you’ll usually do best to err on the side of making the broadest type of product for it.

[444] . One year at Startup School David Heinemeier Hansson encouraged programmers who wanted to start businesses to use a restaurant as a model. What he meant, I believe, is that it’s fine to start software companies constrained in (a) in the same way a restaurant is constrained in (b). I agree. Most people should not try to start startups.

[445] . That sort of stepping back is one of the things we focus on at Y Combinator. It’s common for founders to have discovered something intuitively without understanding all its implications. That’s probably true of the biggest discoveries in any field.

[446] . I got it wrong in “How to Make Wealth” when I said that a startup was a small company that takes on a hard technical problem. That is the most common recipe but not the only one.

[447] . In principle companies aren’t limited by the size of the markets they serve, because they could just expand into new markets. But there seem to be limits on the ability of big companies to do that. Which means the slowdown that comes from bumping up against the limits of one’s markets is ultimately just another way in which internal limits are expressed. It may be that some of these limits could be overcome by changing the shape of the organization – specifically by sharding it.

[448] . This is, obviously, only for startups that have already launched or can launch during YC. A startup building a new database will probably not do that. On the other hand, launching something small and then using growth rate as evolutionary pressure is such a valuable technique that any company that could start this way probably should.

[449] . If the startup is taking the Facebook/Twitter route and building something they hope will be very popular but from which they don’t yet have a definite plan to make money, the growth rate has to be higher, even though it’s a proxy for revenue growth, because such companies need huge numbers of users to succeed at all. Beware too of the edge case where something spreads rapidly but the churn is high as well, so that you have good net growth till you run through all the potential users, at which point it suddenly stops.

[450] . Within YC when we say it’s ipso facto right to do whatever gets you growth, it’s implicit that this excludes trickery like buying users for more than their lifetime value, counting users as active when they’re really not, bleeding out invites at a regularly increasing rate to manufacture a perfect growth curve, etc. Even if you were able to fool investors with such tricks, you’d ultimately be hurting yourself, because you’re throwing off your own compass.

[451] . Which is why it’s such a dangerous mistake to believe that successful startups are simply the embodiment of some brilliant initial idea. What you’re looking for initially is not so much a great idea as an idea that could evolve into a great one. The danger is that promising ideas are not merely blurry versions of great ones. They’re often different in kind, because the early adopters you evolve the idea upon have different needs from the rest of the market. For example, the idea that evolves into Facebook isn’t merely a subset of Facebook; the idea that evolves into Facebook is a site for Harvard undergrads.

[452] . What if a company grew at 1.7x a year for a really long time? Could it not grow just as big as any successful startup? In principle yes, of course. If our hypothetical company making $1000 a month grew at 1% a week for 19 years, it would grow as big as a company growing at 5% a week for 4 years. But while such trajectories may be common in, say, real estate development, you don’t see them much in the technology business. In technology, companies that grow slowly tend not to grow as big.

[453] . Any expected value calculation varies from person to person depending on their utility function for money. I.e. the first million is worth more to most people than subsequent millions. How much more depends on the person. For founders who are younger or more ambitious the utility function is flatter. Which is probably part of the reason the founders of the most successful startups of all tend to be on the young side.

[454] . More precisely, this is the case in the biggest winners, which is where all the returns come from. A startup founder could pull the same trick of enriching himself at the company’s expense by selling them overpriced components. But it wouldn’t be worth it for the founders of Google to do that. Only founders of failing startups would even be tempted, but those are writeoffs from the VCs’ point of view anyway.

[455] . Acquisitions fall into two categories: those where the acquirer wants the business, and those where the acquirer just wants the employees. The latter type is sometimes called an HR acquisition. Though nominally acquisitions and sometimes on a scale that has a significant effect on the expected value calculation for potential founders, HR acquisitions are viewed by acquirers as more akin to hiring bonuses.

[456] . I once explained this to some founders who had recently arrived from Russia. They found it novel that if you threatened a company they’d pay a premium for you. “In Russia they just kill you,” they said, and they were only partly joking. Economically, the fact that established companies can’t simply eliminate new competitors may be one of the most valuable aspects of the rule of law. And so to the extent we see incumbents suppressing competitors via regulations or patent suits, we should worry, not because it’s a departure from the rule of law per se but from what the rule of law is aiming at.

[457] . This form of bad idea has been around as long as the web. It was common in the 1990s, except then people who had it used to say they were going to create a portal for x instead of a social network for x. Structurally the idea is stone soup: you post a sign saying “this is the place for people interested in x,” and all those people show up and you make money from them. What lures founders into this sort of idea are statistics about the millions of people who might be interested in each type of x. What they forget is that any given person might have 20 affinities by this standard, and no one is going to visit 20 different communities regularly.

[458] . I’m not saying, incidentally, that I know for sure a social network for pet owners is a bad idea. I know it’s a bad idea the way I know randomly generated DNA would not produce a viable organism. The set of plausible sounding startup ideas is many times larger than the set of good ones, and many of the good ones don’t even sound that plausible. So if all you know about a startup idea is that it sounds plausible, you have to assume it’s bad.

[459] . More precisely, the users’ need has to give them sufficient activation energy to start using whatever you make, which can vary a lot. For example, the activation energy for enterprise software sold through traditional channels is very high, so you’d have to be a lot better to get users to switch. Whereas the activation energy required to switch to a new search engine is low. Which in turn is why search engines are so much better than enterprise software.

[460] . This gets harder as you get older. While the space of ideas doesn’t have dangerous local maxima, the space of careers does. There are fairly high walls between most of the paths people take through life, and the older you get, the higher the walls become.

[461] . It was also obvious to us that the web was going to be a big deal. Few non-programmers grasped that in 1995, but the programmers had seen what GUIs had done for desktop computers.

[462] . Maybe it would work to have this second self keep a journal, and each night to make a brief entry listing the gaps and anomalies you’d noticed that day. Not startup ideas, just the raw gaps and anomalies.

[463] . Sam Altman points out that taking time to come up with an idea is not merely a better strategy in an absolute sense, but also like an undervalued stock in that so few founders do it. There’s comparatively little competition for the best ideas, because few founders are willing to put in the time required to notice them. Whereas there is a great deal of competition for mediocre ideas, because when people make up startup ideas, they tend to make up the same ones.

[464] . For the computer hardware and software companies, summer jobs are the first phase of the recruiting funnel. But if you’re good you can skip the first phase. If you’re good you’ll have no trouble getting hired by these companies when you graduate, regardless of how you spent your summers.

[465] . The empirical evidence suggests that if colleges want to help their students start startups, the best thing they can do is leave them alone in the right way.

[466] . I’m speaking here of IT startups; in biotech things are different.

[467] . This is an instance of a more general rule: focus on users, not competitors. The most important information about competitors is what you learn via users anyway.

[468] . In practice most successful startups have elements of both. And you can describe each strategy in terms of the other by adjusting the boundaries of what you call the market. But it’s useful to consider these two ideas separately.

[469] . I almost hesitate to raise that point though. Startups are businesses; the point of a business is to make money; and with that additional constraint, you can’t expect you’ll be able to spend all your time working on what interests you most.

[470] . The need has to be a strong one. You can retroactively describe any made- up idea as something you need. But do you really need that recipe site or local event aggregator as much as Drew Houston needed Dropbox, or Brian Chesky and Joe Gebbia needed Airbnb? Quite often at YC I find myself asking founders “Would you use this thing yourself, if you hadn’t written it?” and you’d be surprised how often the answer is no.

[471] . Paul Buchheit points out that trying to sell something bad can be a source of better ideas: “The best technique I’ve found for dealing with YC companies that have bad ideas is to tell them to go sell the product ASAP (before wasting time building it). Not only do they learn that nobody wants what they are building, they very often come back with a real idea that they discovered in the process of trying to sell the bad idea.”

[472] . Here’s a recipe that might produce the next Facebook, if you’re college students. If you have a connection to one of the more powerful sororities at your school, approach the queen bees thereof and offer to be their personal IT consultants, building anything they could imagine needing in their social lives that didn’t already exist. Anything that got built this way would be very promising, because such users are not just the most demanding but also the perfect point to spread from. I have no idea whether this would work.

[473] . And the reason it used a TV for a monitor is that Steve Wozniak started out by solving his own problems. He, like most of his peers, couldn’t afford a monitor.

[474] . I realize revenue and not fundraising is the proper test of success for a startup. The reason we quote statistics about fundraising is because those are the numbers we have. We couldn’t talk meaningfully about revenues without including the numbers from the most successful startups, and we don’t have those. We often discuss revenue growth with the earlier stage startups, because that’s how we gauge their progress, but when companies reach a certain size it gets presumptuous for a seed investor to do that. In any case, companies’ market caps do eventually become a function of revenues, and post-money valuations of funding rounds are at least guesses by pros about where those market caps will end up. The reason only 287 have valuations is that the rest have mostly raised money on convertible notes, and although convertible notes often have valuation caps, a valuation cap is merely an upper bound on a valuation.

[475] . We didn’t try to accept a particular number. We have no way of doing that even if we wanted to. We just tried to be significantly pickier.

[476] . Though you never know with bottlenecks, I’m guessing the next one will be coordinating efforts among partners.

[477] . I realize starting a company doesn’t have to mean starting a startup. There will be lots of people starting normal companies too. But that’s not relevant to an audience of investors. Geoff Ralston reports that in Silicon Valley it seemed thinkable to start a startup in the mid 1980s. It would have started there. But I know it didn’t to undergraduates on the East Coast.

[478] . This trend is one of the main causes of the increase in economic inequality in the US since the mid twentieth century. The person who would in 1950 have been the general manager of the x division of Megacorp is now the founder of the x company, and owns significant equity in it.

[479] . If Congress passes the founder visa in a non-broken form, that alone could in principle get us up to 20x, since 95% of the world’s population lives outside the US.

[480] . If idea clashes got bad enough, it could change what it means to be a startup. We currently advise startups mostly to ignore competitors. We tell them startups are competitive like running, not like soccer; you don’t have to go and steal the ball away from the other team. But if idea clashes became common enough, maybe you’d start to have to. That would be unfortunate.

[481] . Actually Emerson never mentioned mousetraps specifically. He wrote “If a man has good corn or wood, or boards, or pigs, to sell, or can make better chairs or knives, crucibles or church organs, than anybody else, you will find a broad hard-beaten road to his house, though it be in the woods.”

[482] . Thanks to Sam Altman for suggesting I make this explicit. And no, you can’t avoid doing sales by hiring someone to do it for you. You have to do sales yourself initially. Later you can hire a real salesperson to replace you.

[483] . The reason this works is that as you get bigger, your size helps you grow. Patrick Collison wrote “At some point, there was a very noticeable change in how Stripe felt. It tipped from being this boulder we had to push to being a train car that in fact had its own momentum.”

[484] . One of the more subtle ways in which YC can help founders is by calibrating their ambitions, because we know exactly how a lot of successful startups looked when they were just getting started.

[485] . If you’re building something for which you can’t easily get a small set of users to observe – e.g. enterprise software – and in a domain where you have no connections, you’ll have to rely on cold calls and introductions. But should you even be working on such an idea?

[486] . Garry Tan pointed out an interesting trap founders fall into in the beginning. They want so much to seem big that they imitate even the flaws of big companies, like indifference to individual users. This seems to them more “professional.” Actually it’s better to embrace the fact that you’re small and use whatever advantages that brings.

[487] . Your user model almost couldn’t be perfectly accurate, because users’ needs often change in response to what you build for them. Build them a microcomputer, and suddenly they need to run spreadsheets on it, because the arrival of your new microcomputer causes someone to invent the spreadsheet.

[488] . If you have to choose between the subset that will sign up quickest and those that will pay the most, it’s usually best to pick the former, because those are probably the early adopters. They’ll have a better influence on your product, and they won’t make you expend as much effort on sales. And though they have less money, you don’t need that much to maintain your target growth rate early on.

[489] . Yes, I can imagine cases where you could end up making something that was really only useful for one user. But those are usually obvious, even to inexperienced founders. So if it’s not obvious you’d be making something for a market of one, don’t worry about that danger.

[490] . There may even be an inverse correlation between launch magnitude and success. The only launches I remember are famous flops like the Segway and Google Wave. Wave is a particularly alarming example, because I think it was actually a great idea that was killed partly by its overdone launch.

[491] . Google grew big on the back of Yahoo, but that wasn’t a partnership. Yahoo was their customer.

[492] . It will also remind founders that an idea where the second component is empty – an idea where there is nothing you can do to get going, e.g. because you have no way to find users to recruit manually – is probably a bad idea, at least for those founders.

[493] . There’s no reason to believe this number is a constant. In fact it’s our explicit goal at Y Combinator to increase it, by encouraging people to start startups who otherwise wouldn’t have.

[494] . Or more precisely, investors decide whether you’re a loser or possibly a winner. If you seem like a winner, they may then, depending on how much you’re raising, have several more meetings with you to test whether that initial impression holds up. But if you seem like a loser they’re done, at least for the next year or so. And when they decide you’re a loser they usually decide in way less than the 50 minutes they may have allotted for the first meeting. Which explains the astonished stories one always hears about VC inattentiveness. How could these people make investment decisions well when they’re checking their messages during startups’ presentations? The solution to that mystery is that they’ve already made the decision.

[495] . The two are not mutually exclusive. There are people who are both genuinely formidable, and also really good at acting that way.

[496] . How can people who will go on to create giant companies not seem formidable early on? I think the main reason is that their experience so far has trained them to keep their wings folded, as it were. Family, school, and jobs encourage cooperation, not conquest. And it’s just as well they do, because even being Genghis Khan is probably 99% cooperation. But the result is that most people emerge from the tube of their upbringing in their early twenties compressed into the shape of the tube. Some find they have wings and start to spread them. But this takes a few years. In the beginning even they don’t know yet what they’re capable of.

[497] . In fact, change what you’re doing. You’re investing your own time in your startup. If you’re not convinced that what you’re working on is a sufficiently good bet, why are you even working on that?

[498] . When investors ask you a question you don’t know the answer to, the best response is neither to bluff nor give up, but instead to explain how you’d figure out the answer. If you can work out a preliminary answer on the spot, so much the better, but explain that’s what you’re doing.

[499] . At YC we try to ensure startups are ready to raise money on Demo Day by encouraging them to ignore investors and instead focus on their companies till about a week before. That way most reach the stage where they’re sufficiently convincing well before Demo Day. But not all do, so we also give any startup that wants to the option of deferring to a later Demo Day.

[500] . Founders are often surprised by how much harder it is to raise the next round. There is a qualitative difference in investors’ attitudes. It’s like the difference between being judged as a kid and as an adult. The next time you raise money, it’s not enough to be promising. You have to be delivering results. So although it works well to show growth graphs at either stage, investors treat them differently. At three months, a growth graph is mostly evidence that the founders are effective. At two years, it has to be evidence of a promising market and a company tuned to exploit it.

[501] . By this I mean that if the present day equivalent of the 3 month old Microsoft presented at a Demo Day, there would be investors who turned them down. Microsoft itself didn’t raise outside money, and indeed the venture business barely existed when they got started in 1975.

[502] . The best investors rarely care who else is investing, but mediocre investors almost all do. So you can use this question as a test of investor quality.

[503] . To use this technique, you’ll have to find out why investors who rejected you did so, or at least what they claim was the reason. That may require asking, because investors don’t always volunteer a lot of detail. Make it clear when you ask that you’re not trying to dispute their decision – just that if there is some weakness in your plans, you need to know about it. You won’t always get a real reason out of them, but you should at least try.

[504] . Dropbox wasn’t rejected by all the East Coast VCs. There was one firm that wanted to invest but tried to lowball them.

[505] . Alfred Lin points out that it’s doubly important for the explanation of a startup to be clear and concise, because it has to convince at one remove: it has to work not just on the partner you talk to, but when that partner re- tells it to colleagues. We consciously optimize for this at YC. When we work with founders create a Demo Day pitch, the last step is to imagine how an investor would sell it to colleagues.

[506] . An accountant might say that a company that has raised a million dollars is no richer if it’s convertible debt, but in practice money raised as convertible debt is little different from money raised in an equity round.

[507] . Founders are often surprised by this, but investors can get very emotional. Or rather indignant; that’s the main emotion I’ve observed; but it is very common, to the point where it sometimes causes investors to act against their own interests. I know of one investor who invested in a startup at a $15 million valuation cap. Earlier he’d had an opportunity to invest at a $5 million cap, but he refused because a friend who invested earlier had been able to invest at a $3 million cap.

[508] . If an investor pushes you hard to tell them about your conversations with other investors, is this someone you want as an investor?

[509] . The worst explosions happen when unpromising-seeming startups encounter mediocre investors. Good investors don’t lead startups on; their reputations are too valuable. And startups that seem promising can usually get enough money from good investors that they don’t have to talk to mediocre ones. It is the unpromising-seeming startups that have to resort to raising money from mediocre investors. And it’s particularly damaging when these investors flake, because unpromising-seeming startups are usually more desperate for money. (Not all unpromising-seeming startups do badly. Some are merely ugly ducklings in the sense that they violate current startup fashions.)

[510] . One YC founder told me: > I think in general we’ve done ok at fundraising, but I managed to screw up > twice at the exact same thing – trying to focus on building the company and > fundraising at the same time.

[511] . There is one subtle danger you have to watch out for here, which I warn about later: beware of getting too high a valuation from an eager investor, lest that set an impossibly high target when raising additional money.

[512] . If they really need a meeting, then they’re not ready to invest, regardless of what they say. They’re still deciding, which means you’re being asked to come in and convince them. Which is fundraising.

[513] . Associates at VC firms regularly cold email startups. Naive founders think “Wow, a VC is interested in us!” But an associate is not a VC. They have no decision-making power. And while they may introduce startups they like to partners at their firm, the partners discriminate against deals that come to them this way. I don’t know of a single VC investment that began with an associate cold-emailing a startup. If you want to approach a specific firm, get an intro to a partner from someone they respect. It’s ok to talk to an associate if you get an intro to a VC firm or they see you at a Demo Day and they begin by having an associate vet you. That’s not a promising lead and should therefore get low priority, but it’s not as completely worthless as a cold email. Because the title “associate” has gotten a bad reputation, a few VC firms have started to give their associates the title “partner,” which can make things very confusing. If you’re a YC startup you can ask us who’s who; otherwise you may have to do some research online. There may be a special title for actual partners. If someone speaks for the firm in the press or a blog on the firm’s site, they’re probably a real partner. If they’re on boards of directors they’re probably a real partner. There are titles between “associate” and “partner,” including “principal” and “venture partner.” The meanings of these titles vary too much to generalize.

[514] . For similar reasons, avoid casual conversations with potential acquirers. They can lead to distractions even more dangerous than fundraising. Don’t even take a meeting with a potential acquirer unless you want to sell your company right now.

[515] . Joshua Reeves specifically suggests asking each investor to intro you to two more investors. Don’t ask investors who say no for introductions to other investors. That will in many cases be an anti-recommendation.

[516] . This is not always as deliberate as its sounds. A lot of the delays and disconnects between founders and investors are induced by the customs of the venture business, which have evolved the way they have because they suit investors’ interests.

[517] . One YC founder who read a draft of this essay wrote: > This is the most important section. I think it might bear stating even more > clearly. “Investors will deliberately affect more interest than they have to > preserve optionality. If an investor seems very interested in you, they > still probably won’t invest. The solution for this is to assume the worst – > that an investor is just feigning interest – until you get a definite > commitment.”

[518] . Though you should probably pack investor meetings as closely as you can, Jeff Byun mentions one reason not to: if you pack investor meetings too closely, you’ll have less time for your pitch to evolve. Some founders deliberately schedule a handful of lame investors first, to get the bugs out of their pitch.

[519] . There is not an efficient market in this respect. Some of the most useless investors are also the highest maintenance.

[520] . Incidentally, this paragraph is sales 101. If you want to see it in action, go talk to a car dealer.

[521] . I know one very smooth founder who used to end investor meetings with “So, can I count you in?” delivered as if it were “Can you pass the salt?” Unless you’re very smooth (if you’re not sure…), do not do this yourself. There is nothing more unconvincing, for an investor, than a nerdy founder trying to deliver the lines meant for a smooth one. Investors are fine with funding nerds. So if you’re a nerd, just try to be a good nerd, rather than doing a bad imitation of a smooth salesman.

[522] . Ian Hogarth suggests a good way to tell how serious potential investors are: the resources they expend on you after the first meeting. An investor who’s seriously interested will already be working to help you even before they’ve committed.

[523] . In principle you might have to think about so-called “signalling risk.” If a prestigious VC makes a small seed investment in you, what if they don’t want to invest the next time you raise money? Other investors might assume that the VC knows you well, since they’re an existing investor, and if they don’t want to invest in your next round, that must mean you suck. The reason I say “in principle” is that in practice signalling hasn’t been much of a problem so far. It rarely arises, and in the few cases where it does, the startup in question usually is doing badly and is doomed anyway. If you have the luxury of choosing among seed investors, you can play it safe by excluding VC firms. But it isn’t critical to.

[524] . Sometimes a competitor will deliberately threaten you with a lawsuit just as you start fundraising, because they know you’ll have to disclose the threat to potential investors and they hope this will make it harder for you to raise money. If this happens it will probably frighten you more than investors. Experienced investors know about this trick, and know the actual lawsuits rarely happen. So if you’re attacked in this way, be forthright with investors. They’ll be more alarmed if you seem evasive than if you tell them everything.

[525] . A related trick is to claim that they’ll only invest contingently on other investors doing so because otherwise you’d be “undercapitalized.” This is almost always bullshit. They can’t estimate your minimum capital needs that precisely.

[526] . You won’t hire all those 20 people at once, and you’ll probably have some revenues before 18 months are out. But those too are acceptable or at least accepted additions to the margin for error.

[527] . Type A fundraising is so much better that it might even be worth doing something different if it gets you there sooner. One YC founder told me that if he were a first-time founder again he’d “leave ideas that are up-front capital intensive to founders with established reputations.”

[528] . I don’t know whether this happens because they’re innumerate, or because they believe they have zero ability to predict startup outcomes (in which case this behavior at least wouldn’t be irrational). In either case the implications are similar.

[529] . If you’re a YC startup and you have an investor who for some reason insists that you decide the price, any YC partner can estimate a market price for you.

[530] . You should respond in kind when investors behave upstandingly too. When an investor makes you a clean offer with no deadline, you have a moral obligation to respond promptly.

[531] . Tell the investors talking to you about an A round about the smaller investments you raise as you raise them. You owe them such updates on your cap table, and this is also a good way to pressure them to act. They won’t like you raising other money and may pressure you to stop, but they can’t legitimately ask you to commit to them till they also commit to you. If they want you to stop raising money, the way to do it is to give you a series A termsheet with a no-shop clause. You can relent a little if the potential series A investor has a great reputation and they’re clearly working fast to get you a termsheet, particularly if a third party like YC is involved to ensure there are no misunderstandings. But be careful.

[532] . The company is Weebly, which made it to profitability on a seed investment of $650k. They did try to raise a series A in the fall of 2008 but (no doubt partly because it was the fall of 2008) the terms they were offered were so bad that they decided to skip raising an A round.

[533] . Another advantage of having one founder take fundraising meetings is that you never have to negotiate in real time, which is something inexperienced founders should avoid. One YC founder told me: > Investors are professional negotiators and can negotiate on the spot very > easily. If only one founder is in the room, you can say “I need to circle > back with my co-founder” before making any commitments. I used to do this > all the time.

[534] . You’ll be lucky if fundraising feels pleasant enough to become addictive. More often you have to worry about the other extreme – becoming demoralized when investors reject you. As one (very successful) YC founder wrote after reading a draft of this: > It’s hard to mentally deal with the sheer scale of rejection in fundraising > and if you are not in the right mindset you will fail. Users may love you > but these supposedly smart investors may not understand you at all. At this > point for me, rejection still rankles but I’ve come to accept that investors > are just not super thoughtful for the most part and you need to play the > game according to certain somewhat depressing rules (many of which you are > listing) in order to win.

[535] . The actual sentence in the King James Bible is “Pride goeth before destruction, and an haughty spirit before a fall.”

[536] . Some founders listen more than others, and this tends to be a predictor of success. One of the things I remember about the Airbnbs during YC is how intently they listened.

[537] . In fact, this is one of the reasons startups are possible. If big companies weren’t plagued by internal inefficiencies, they’d be proportionately more effective, leaving less room for startups.

[538] . In a startup you have to spend a lot of time on schleps, but this sort of work is merely unglamorous, not bogus.

[539] . What should you do if your true calling is gaming the system? Management consulting.

[540] . The company may not be incorporated, but if you start to get significant numbers of users, you’ve started it, whether you realize it yet or not.

[541] . It shouldn’t be that surprising that colleges can’t teach students how to be good startup founders, because they can’t teach them how to be good employees either. The way universities “teach” students how to be employees is to hand off the task to companies via internship programs. But you couldn’t do the equivalent thing for startups, because by definition if the students did well they would never come back.

[542] . Charles Darwin was 22 when he received an invitation to travel aboard the HMS Beagle as a naturalist. It was only because he was otherwise unoccupied, to a degree that alarmed his family, that he could accept it. And yet if he hadn’t we probably would not know his name.

[543] . Parents can sometimes be especially conservative in this department. There are some whose definition of important problems includes only those on the critical path to med school.

[544] . I did manage to think of a heuristic for detecting whether you have a taste for interesting ideas: whether you find known boring ideas intolerable. Could you endure studying literary theory, or working in middle management at a large company?

[545] . In fact, if your goal is to start a startup, you can stick even more closely to the ideal of a liberal education than past generations have. Back when students focused mainly on getting a job after college, they thought at least a little about how the courses they took might look to an employer. And perhaps even worse, they might shy away from taking a difficult class lest they get a low grade, which would harm their all-important GPA. Good news: users don’t care what your GPA was. And I’ve never heard of investors caring either. Y Combinator certainly never asks what classes you took in college or what grades you got in them.

[546] . I’m not saying all founders who take big acquisition offers are driven only by money, but rather that those who don’t aren’t. Plus one can have benevolent motives for being driven by money – for example, to take care of one’s family, or to be free to work on projects that improve the world.

[547] . It’s unlikely that every successful startup improves the world. But their founders, like parents, truly believe they do. Successful founders are in love with their companies. And while this sort of love is as blind as the love people have for one another, it is genuine.

[548] . Peter Thiel would point out that successful founders still get rich from controlling monopolies, just monopolies they create rather than ones they capture. And while this is largely true, it means a big change in the sort of person who wins.

[549] . To be fair, the Romans didn’t mean to kill Archimedes. The Roman commander specifically ordered that he be spared. But he got killed in the chaos anyway. In sufficiently disordered times, even thinking requires control of scarce resources, because living at all is a scarce resource.

[550] . There are a handful of companies that can’t reasonably expect to make money for the first year or two, because what they’re building takes so long. For these companies substitute “progress” for “revenue growth.” You’re not one of these companies unless your initial investors agreed in advance that you were. And frankly even these companies wish they weren’t, because the illiquidity of “progress” puts them at the mercy of investors.

[551] . There’s a variant of the fatal pinch where your existing investors help you along by promising to invest more. Or rather, where you read them as promising to invest more, while they think they’re just mentioning the possibility. The way to solve this problem, if you have 8 months of runway or less, is to try to get the money right now. Then you’ll either get the money, in which case (immediate) problem solved, or at least prevent your investors from helping you to remain in denial about your fundraising prospects.

[552] . Obviously, if you have significant expenses other than salaries that you can eliminate, do it now.

[553] . Unless of course the source of the problem is that you’re paying yourselves high salaries. If by cutting the founders’ salaries to the minimum you need, you can make it to profitability, you should. But it’s a bad sign if you needed to read this to realize that.

[554] . My usual trick is to talk about aspects of the present that most people haven’t noticed yet.

[555] . Especially if they become well enough known that people start to identify them with you. You have to be extra skeptical about things you want to believe, and once a hypothesis starts to be identified with you, it will almost certainly start to be in that category.

[556] . In practice “sufficiently expert” doesn’t require one to be recognized as an expert–which is a trailing indicator in any case. In many fields a year of focused work plus caring a lot would be enough.

[557] . Though they are public and persist indefinitely, comments on e.g. forums and places like Twitter seem empirically to work like casual conversation. The threshold may be whether what you write has a title.

[558] . How much better is a great programmer than an ordinary one? So much better that you can’t even measure the difference directly. A great programmer doesn’t merely do the same work faster. A great programmer will invent things an ordinary programmer would never even think of. This doesn’t mean a great programmer is infinitely more valuable, because any invention has a finite market value. But it’s easy to imagine cases where a great programmer might invent things worth 100x or even 1000x an average programmer’s salary.

[559] . There are a handful of consulting firms that rent out big pools of foreign programmers they bring in on H1-B visas. By all means crack down on these. It should be easy to write legislation that distinguishes them, because they are so different from technology companies. But it is dishonest of the anti- immigration people to claim that companies like Google and Facebook are driven by the same motives. An influx of inexpensive but mediocre programmers is the last thing they’d want; it would destroy them.

[560] . Though this essay talks about programmers, the group of people we need to import is broader, ranging from designers to programmers to electrical engineers. The best one could do as a general term might be “digital talent.” It seemed better to make the argument a little too narrow than to confuse everyone with a neologism.

[561] . I’m not saying you should never sell. I’m saying you should be clear in your own mind about whether you want to sell or not, and not be led by manipulation or wishful thinking into trying to sell earlier than you otherwise would have.

[562] . In a startup, as in most competitive sports, the task at hand almost does this for you; you’re too busy to feel tired. But when you lose that protection, e.g. at the final whistle, the fatigue hits you like a wave. To talk to corp dev is to let yourself feel it mid-game.

[563] . To be fair, the apparent misdeeds of corp dev people are magnified by the fact that they function as the face of a large organization that often doesn’t know its own mind. Acquirers can be surprisingly indecisive about acquisitions, and their flakiness is indistinguishable from dishonesty by the time it filters down to you.

[564] . I’m not saying that if you sort investors by benevolence you’ve also sorted them by returns, but rather that if you do a scatterplot with benevolence on the x axis and returns on the y, you’d see a clear upward trend.

[565] . Y Combinator in particular, because it aggregates data from so many startups, has a pretty comprehensive view of investor behavior.

[566] . Incidentally, this thought experiment works for nationality and religion too.

[567] . The liking you have for a name that has become part of your identity manifests itself not directly, which would be easy to discount, but as a collection of specious beliefs about its intrinsic qualities. (This too is true of nationality and religion as well.)

[568] . Sometimes founders know it’s a problem that they don’t have the .com of their name, but delusion strikes a step later in the belief that they’ll be able to buy it despite having no evidence it’s for sale. Don’t believe a domain is for sale unless the owner has already told you an asking price.

[569] . Many think successful startup founders are driven by money. In fact the secret weapon of the most successful founders is that they aren’t. If they were, they’d have taken one of the acquisition offers that every fast-growing startup gets on the way up. What drives the most successful founders is the same thing that drives most people who make things: the company is their project.

[570] . In fact since 2 ≈ 1.05 ^ 15, the un-rapacious founder is always 15 weeks behind the rapacious one.

[571] . The other reason it might help to be good at squeezing money out of customers is that startups usually lose money at first, and making more per customer makes it easier to get to profitability before your initial funding runs out. But while it is very common for startups to die from running through their initial funding and then being unable to raise more, the underlying cause is usually slow growth or excessive spending rather than insufficient effort to extract money from existing customers.

[572] . Steep usage growth will also interest investors. Revenue will ultimately be a constant multiple of usage, so x% usage growth predicts x% revenue growth. But in practice investors discount merely predicted revenue, so if you’re measuring usage you need a higher growth rate to impress investors.

[573] . Startups that don’t raise money are saved from hiring too fast because they can’t afford to. But that doesn’t mean you should avoid raising money in order to avoid this problem, any more than that total abstinence is the only way to avoid becoming an alcoholic.

[574] . I would not be surprised if VCs’ tendency to push founders to overhire is not even in their own interest. They don’t know how many of the companies that get killed by overspending might have done well if they’d survived. My guess is a significant number.

[575] . After reading a draft, Sam Altman wrote: “I think you should make the hiring point more strongly. I think it’s roughly correct to say that YC’s most successful companies have never been the fastest to hire, and one of the marks of a great founder is being able to resist this urge.” Paul Buchheit adds: “A related problem that I see a lot is premature scaling–founders take a small business that isn’t really working (bad unit economics, typically) and then scale it up because they want impressive growth numbers. This is similar to over-hiring in that it makes the business much harder to fix once it’s big, plus they are bleeding cash really fast.”

[576] . This technique wouldn’t work if the selection process looked for different things from different types of applicants–for example, if an employer hired men based on their ability but women based on their appearance.

[577] . As Paul Buchheit points out, First Round excluded their most successful investment, Uber, from the study. And while it makes sense to exclude outliers from some types of studies, studies of returns from startup investing, which is all about hitting outliers, are not one of them.

[578] . Harj Taggar reminded me that while Jessica didn’t ask many questions, they tended to be important ones: “She was always good at sniffing out any red flags about the team or their determination and disarmingly asking the right question, which usually revealed more than the founders realized.”

[579] . Or more precisely, while she likes getting attention in the sense of getting credit for what she has done, she doesn’t like getting attention in the sense of being watched in real time. Unfortunately, not just for her but for a lot of people, how much you get of the former depends a lot on how much you get of the latter. Incidentally, if you saw Jessica at a public event, you would never guess she hates attention, because (a) she is very polite and (b) when she’s nervous, she expresses it by smiling more.

[580] . The existence of people like Jessica is not just something the mainstream media needs to learn to acknowledge, but something feminists need to learn to acknowledge as well. There are successful women who don’t like to fight. Which means if the public conversation about women consists of fighting, their voices will be silenced. There’s a sort of Gresham’s Law of conversations. If a conversation reaches a certain level of incivility, the more thoughtful people start to leave. No one understands female founders better than Jessica. But it’s unlikely anyone will ever hear her speak candidly about the topic. She ventured a toe in that water a while ago, and the reaction was so violent that she decided “never again.”

[581] . Lester Thurow, writing in 1975, said the wage differentials prevailing at the end of World War II had become so embedded that they “were regarded as ‘just’ even after the egalitarian pressures of World War II had disappeared. Basically, the same differentials exist to this day, thirty years later.” But Goldin and Margo think market forces in the postwar period also helped preserve the wartime compression of wages – specifically increased demand for unskilled workers, and oversupply of educated ones. (Oddly enough, the American custom of having employers pay for health insurance derives from efforts by businesses to circumvent NWLB wage controls in order to attract workers.)

[582] . As always, tax rates don’t tell the whole story. There were lots of exemptions, especially for individuals. And in World War II the tax codes were so new that the government had little acquired immunity to tax avoidance. If the rich paid high taxes during the war it was more because they wanted to than because they had to. After the war, federal tax receipts as a percentage of GDP were about the same as they are now. In fact, for the entire period since the war, tax receipts have stayed close to 18% of GDP, despite dramatic changes in tax rates. The lowest point occurred when marginal income tax rates were highest: 14.1% in 1950. Looking at the data, it’s hard to avoid the conclusion that tax rates have had little effect on what people actually paid.

[583] . Though in fact the decade preceding the war had been a time of unprecedented federal power, in response to the Depression. Which is not entirely a coincidence, because the Depression was one of the causes of the war. In many ways the New Deal was a sort of dress rehearsal for the measures the federal government took during wartime. The wartime versions were much more drastic and more pervasive though. As Anthony Badger wrote, “for many Americans the decisive change in their experiences came not with the New Deal but with World War II.”

[584] . I don’t know enough about the origins of the world wars to say, but it’s not inconceivable they were connected to the rise of big corporations. If that were the case, 20th century cohesion would have a single cause.

[585] . More precisely, there was a bimodal economy consisting, in Galbraith’s words, of “the world of the technically dynamic, massively capitalized and highly organized corporations on the one hand and the hundreds of thousands of small and traditional proprietors on the other.” Money, prestige, and power were concentrated in the former, and there was near zero crossover.

[586] . I wonder how much of the decline in families eating together was due to the decline in families watching TV together afterward.

[587] . I know when this happened because it was the season Dallas premiered. Everyone else was talking about what was happening on Dallas, and I had no idea what they meant.

[588] . I didn’t realize it till I started doing research for this essay, but the meretriciousness of the products I grew up with is a well-known byproduct of oligopoly. When companies can’t compete on price, they compete on tailfins.

[589] . Monroeville Mall was at the time of its completion in 1969 the largest in the country. In the late 1970s the movie Dawn of the Dead was shot there. Apparently the mall was not just the location of the movie, but its inspiration; the crowds of shoppers drifting through this huge mall reminded George Romero of zombies. My first job was scooping ice cream in the Baskin- Robbins.

[590] . Labor unions were exempted from antitrust laws by the Clayton Antitrust Act in 1914 on the grounds that a person’s work is not “a commodity or article of commerce.” I wonder if that means service companies are also exempt.

[591] . The relationships between unions and unionized companies can even be symbiotic, because unions will exert political pressure to protect their hosts. According to Michael Lind, when politicians tried to attack the A&P; supermarket chain because it was putting local grocery stores out of business, “A&P; successfully defended itself by allowing the unionization of its workforce in 1938, thereby gaining organized labor as a constituency.” I’ve seen this phenomenon myself: hotel unions are responsible for more of the political pressure against Airbnb than hotel companies.

[592] . Galbraith was clearly puzzled that corporate executives would work so hard to make money for other people (the shareholders) instead of themselves. He devoted much of The New Industrial State to trying to figure this out. His theory was that professionalism had replaced money as a motive, and that modern corporate executives were, like (good) scientists, motivated less by financial rewards than by the desire to do good work and thereby earn the respect of their peers. There is something in this, though I think lack of movement between companies combined with self-interest explains much of observed behavior.

[593] . Galbraith (p. 94) says a 1952 study of the 800 highest paid executives at 300 big corporations found that three quarters of them had been with their company for more than 20 years.

[594] . It seems likely that in the first third of the 20th century executive salaries were low partly because companies then were more dependent on banks, who would have disapproved if executives got too much. This was certainly true in the beginning. The first big company CEOs were J. P. Morgan’s hired hands. Companies didn’t start to finance themselves with retained earnings till the 1920s. Till then they had to pay out their earnings in dividends, and so depended on banks for capital for expansion. Bankers continued to sit on corporate boards till the Glass-Steagall act in 1933. By mid-century big companies funded 3/4 of their growth from earnings. But the early years of bank dependence, reinforced by the financial controls of World War II, must have had a big effect on social conventions about executive salaries. So it may be that the lack of movement between companies was as much the effect of low salaries as the cause. Incidentally, the switch in the 1920s to financing growth with retained earnings was one cause of the 1929 crash. The banks now had to find someone else to lend to, so they made more margin loans.

[595] . Even now it’s hard to get them to. One of the things I find hardest to get into the heads of would-be startup founders is how important it is to do certain kinds of menial work early in the life of a company. Doing things that don’t scale is to how Henry Ford got started as a high-fiber diet is to the traditional peasant’s diet: they had no choice but to do the right thing, while we have to make a conscious effort.

[596] . Founders weren’t celebrated in the press when I was a kid. “Our founder” meant a photograph of a severe-looking man with a walrus mustache and a wing collar who had died decades ago. The thing to be when I was a kid was an executive. If you weren’t around then it’s hard to grasp the cachet that term had. The fancy version of everything was called the “executive” model.

[597] . The wave of hostile takeovers in the 1980s was enabled by a combination of circumstances: court decisions striking down state anti-takeover laws, starting with the Supreme Court’s 1982 decision in Edgar v. MITE Corp.; the Reagan administration’s comparatively sympathetic attitude toward takeovers; the Depository Institutions Act of 1982, which allowed banks and savings and loans to buy corporate bonds; a new SEC rule issued in 1982 (rule 415) that made it possible to bring corporate bonds to market faster; the creation of the junk bond business by Michael Milken; a vogue for conglomerates in the preceding period that caused many companies to be combined that never should have been; a decade of inflation that left many public companies trading below the value of their assets; and not least, the increasing complacency of managements.

[598] . Foster, Richard. “Creative Destruction Whips through Corporate America.” Innosight, February 2012.

[599] . CEOs of big companies may be overpaid. I don’t know enough about big companies to say. But it is certainly not impossible for a CEO to make 200x as much difference to a company’s revenues as the average employee. Look at what Steve Jobs did for Apple when he came back as CEO. It would have been a good deal for the board to give him 95% of the company. Apple’s market cap the day Steve came back in July 1997 was 1.73 billion. 5% of Apple now (January 2016) would be worth about 30 billion. And it would not be if Steve hadn’t come back; Apple probably wouldn’t even exist anymore. Merely including Steve in the sample might be enough to answer the question of whether public company CEOs in the aggregate are overpaid. And that is not as facile a trick as it might seem, because the broader your holdings, the more the aggregate is what you care about.

[600] . The late 1960s were famous for social upheaval. But that was more rebellion (which can happen in any era if people are provoked sufficiently) than fragmentation. You’re not seeing fragmentation unless you see people breaking off to both left and right.

[601] . Globally the trend has been in the other direction. While the US is becoming more fragmented, the world as a whole is becoming less fragmented, and mostly in good ways.

[602] . There were a handful of ways to make a fortune in the mid 20th century. The main one was drilling for oil, which was open to newcomers because it was not something big companies could dominate through economies of scale. How did individuals accumulate large fortunes in an era of such high taxes? Giant tax loopholes defended by two of the most powerful men in Congress, Sam Rayburn and Lyndon Johnson. But becoming a Texas oilman was not in 1950 something one could aspire to the way starting a startup or going to work on Wall Street were in 2000, because (a) there was a strong local component and (b) success depended so much on luck.

[603] . The Baumol Effect induced by startups is very visible in Silicon Valley. Google will pay people millions of dollars a year to keep them from leaving to start or join startups.

[604] . I’m not claiming variation in productivity is the only cause of economic inequality in the US. But it’s a significant cause, and it will become as big a cause as it needs to, in the sense that if you ban other ways to get rich, people who want to get rich will use this route instead.

[605] . Stiglitz, Joseph. The Price of Inequality. Norton, 2012. p. 32.

[606] . Particularly since economic inequality is a matter of outliers, and outliers are disproportionately likely to have gotten where they are by ways that have little do with the sort of things economists usually think about, like wages and productivity, but rather by, say, ending up on the wrong side of the “War on Drugs.”

[607] . Determination is the most important factor in deciding between success and failure, which in startups tend to be sharply differentiated. But it takes more than determination to create one of the hugely successful startups. Though most founders start out excited about the idea of getting rich, purely mercenary founders will usually take one of the big acquisition offers most successful startups get on the way up. The founders who go on to the next stage tend to be driven by a sense of mission. They have the same attachment to their companies that an artist or writer has to their work. But it is very hard to predict at the outset which founders will do that. It’s not simply a function of their initial attitude. Starting a company changes people.

[608] . After reading a draft of this essay, Richard Florida told me how he had once talked to a group of Europeans “who said they wanted to make Europe more entrepreneurial and more like Silicon Valley. I said by definition this will give you more inequality. They thought I was insane – they could not process it.”

[609] . Economic inequality has been decreasing globally. But this is mainly due to the erosion of the kleptocracies that formerly dominated all the poorer countries. Once the playing field is leveler politically, we’ll see economic inequality start to rise again. The US is the bellwether. The situation we face here, the rest of the world will sooner or later.

[610] . Some people still get rich by buying politicians. My point is that it’s no longer a precondition.

[611] . As well as problems that have economic inequality as a symptom, there are those that have it as a cause. But in most if not all, economic inequality is not the primary cause. There is usually some injustice that is allowing economic inequality to turn into other forms of inequality, and that injustice is what we need to fix. For example, the police in the US treat the poor worse than the rich. But the solution is not to make people richer. It’s to make the police treat people more equitably. Otherwise they’ll continue to maltreat people who are weak in other ways.

[612] . Some who read this essay will say that I’m clueless or even being deliberately misleading by focusing so much on the richer end of economic inequality – that economic inequality is really about poverty. But that is exactly the point I’m making, though sloppier language than I’d use to make it. The real problem is poverty, not economic inequality. And if you conflate them you’re aiming at the wrong target. Others will say I’m clueless or being misleading by focusing on people who get rich by creating wealth – that startups aren’t the problem, but corrupt practices in finance, healthcare, and so on. Once again, that is exactly my point. The problem is not economic inequality, but those specific abuses. It’s a strange task to write an essay about why something isn’t the problem, but that’s the situation you find yourself in when so many people mistakenly think it is.

[613] . Particularly since many causes of poverty are only partially driven by people trying to make money from them. For example, America’s abnormally high incarceration rate is a major cause of poverty. But although for-profit prison companies and prison guard unions both spend a lot lobbying for harsh sentencing laws, they are not the original source of them.

[614] . Incidentally, tax loopholes are definitely not a product of some power shift due to recent increases in economic inequality. The golden age of economic equality in the mid 20th century was also the golden age of tax avoidance. Indeed, it was so widespread and so effective that I’m skeptical whether economic inequality was really so low then as we think. In a period when people are trying to hide wealth from the government, it will tend to be hidden from statistics too. One sign of the potential magnitude of the problem is the discrepancy between government receipts as a percentage of GDP, which have remained more or less constant during the entire period from the end of World War II to the present, and tax rates, which have varied dramatically.

[615] . At first I didn’t like it that the word that came to mind was one that had other meanings. But then I realized the other meanings are fairly closely related. Bullshit in the sense of things you waste your time on is a lot like intellectual bullshit.

[616] . I chose this example deliberately as a note to self. I get attacked a lot online. People tell the craziest lies about me. And I have so far done a pretty mediocre job of suppressing the natural human inclination to say “Hey, that’s not true!”

[617] . I realize of course that if people’s personalities vary in any two ways, you can use them as axes and call the resulting four quadrants personality types. So what I’m really claiming is that the axes are orthogonal and that there’s significant variation in both.

[618] . The aggressively conventional-minded aren’t responsible for all the trouble in the world. Another big source of trouble is the sort of charismatic leader who gains power by appealing to them. They become much more dangerous when such leaders emerge.

[619] . I never worried about writing things that offended the conventional-minded when I was running Y Combinator. If YC were a cookie company, I’d have faced a difficult moral choice. Conventional-minded people eat cookies too. But they don’t start successful startups. So if I deterred them from applying to YC, the only effect was to save us work reading applications.

[620] . There has been progress in one area: the punishments for talking about banned ideas are less severe than in the past. There’s little danger of being killed, at least in richer countries. The aggressively conventional-minded are mostly satisfied with getting people fired.

[621] . Many professors are independent-minded — especially in math, the hard sciences, and engineering, where you have to be to succeed. But students are more representative of the general population, and thus mostly conventional- minded. So when professors and students are in conflict, it’s not just a conflict between generations but also between different types of people.

[622] . In practice, eventually some of this 8% would come in the form of dividends, which are taxed as income at issue, so this model actually represents the most optimistic case for the founder. * * *

[623] . This assumption may be too conservative. There is some evidence that historically the Bay Area has attracted a different sort of person than, say, New York City.

[624] . One of their great favorites is Theranos. But the most conspicuous feature of Theranos’s cap table is the absence of Silicon Valley firms. Journalists were fooled by Theranos, but Silicon Valley investors weren’t.

[625] . I made two mistakes about teachers when I was younger. I cared more about professors’ research than their reputations as teachers, and I was also wrong about what it meant to be a good teacher. I thought it simply meant to be good at explaining things.

[626] . Patrick Collison points out that you can go past treating something as a hack in the sense of a prototype and onward to the sense of the word that means something closer to a practical joke: > I think there may be something related to being a hack that can be powerful > — the idea of making the tenuousness and implausibility a feature. “Yes, > it’s a bit ridiculous, right? I’m just trying to see how far such a naive > approach can get.” YC seemed to me to have this characteristic.

[627] . Much of the advantage of switching from physical to digital media is not the software per se but that it lets you start something new with little upfront commitment.

[628] . John Carmack adds: > The value of a medium without a vast gulf between the early work and the > final work is exemplified in game mods. The original Quake game was a golden > age for mods, because everything was very flexible, but so crude due to > technical limitations, that quick hacks to try out a gameplay idea weren’t > all that far from the official game. Many careers were born from that, but > as the commercial game quality improved over the years, it became almost a > full time job to make a successful mod that would be appreciated by the > community. This was dramatically reversed with Minecraft and later Roblox, > where the entire esthetic of the experience was so explicitly crude that > innovative gameplay concepts became the overriding value. These “crude” game > mods by single authors are now often bigger deals than massive professional > teams’ work.

[629] . Lisa Randall suggests that we > treat new things as experiments. That way there’s no such thing as failing, > since you learn something no matter what. You treat it like an experiment in > the sense that if it really rules something out, you give up and move on, > but if there’s some way to vary it to make it work better, go ahead and do > that

[630] . Michael Nielsen points out that the internet has made this easier, because you can see programmers’ first commits, musicians’ first videos, and so on.

[631] . One convenient consequence of the fact that no one identifies as conventional-minded is that you can say what you like about conventional- minded people without getting in too much trouble. When I wrote “The Four Quadrants of Conformism” I expected a firestorm of rage from the aggressively conventional-minded, but in fact it was quite muted. They sensed that there was something about the essay that they disliked intensely, but they had a hard time finding a specific passage to pin it on.

[632] . When I ask myself what in my life is like high school, the answer is Twitter. It’s not just full of conventional-minded people, as anything its size will inevitably be, but subject to violent storms of conventional- mindedness that remind me of descriptions of Jupiter. But while it probably is a net loss to spend time there, it has at least made me think more about the distinction between independent- and conventional-mindedness, which I probably wouldn’t have done otherwise.

[633] . The decrease in independent-mindedness in growing startups is still an open problem, but there may be solutions. Founders can delay the problem by making a conscious effort only to hire independent-minded people. Which of course also has the ancillary benefit that they have better ideas. Another possible solution is to create policies that somehow disrupt the force of conformism, much as control rods slow chain reactions, so that the conventional-minded aren’t as dangerous. The physical separation of Lockheed’s Skunk Works may have had this as a side benefit. Recent examples suggest employee forums like Slack may not be an unmitigated good. The most radical solution would be to grow revenues without growing the company. You think hiring that junior PR person will be cheap, compared to a programmer, but what will be the effect on the average level of independent- mindedness in your company? (The growth in staff relative to faculty seems to have had a similar effect on universities.) Perhaps the rule about outsourcing work that’s not your “core competency” should be augmented by one about outsourcing work done by people who’d ruin your culture as employees. Some investment firms already seem to be able to grow revenues without growing the number of employees. Automation plus the ever increasing articulation of the “tech stack” suggest this may one day be possible for product companies.

[634] . There are intellectual fashions in every field, but their influence varies. One of the reasons politics, for example, tends to be boring is that it’s so extremely subject to them. The threshold for having opinions about politics is much lower than the one for having opinions about set theory. So while there are some ideas in politics, in practice they tend to be swamped by waves of intellectual fashion.

[635] . The conventional-minded are often fooled by the strength of their opinions into believing that they’re independent-minded. But strong convictions are not a sign of independent-mindedness. Rather the opposite.

[636] . Fastidiousness about truth doesn’t imply that an independent-minded person won’t be dishonest, but that he won’t be deluded. It’s sort of like the definition of a gentleman as someone who is never unintentionally rude.

[637] . You see this especially among political extremists. They think themselves nonconformists, but actually they’re niche conformists. Their opinions may be different from the average person’s, but they are often more influenced by their peers’ opinions than the average person’s are.

[638] . If we broaden the concept of fastidiousness about truth so that it excludes pandering, bogusness, and pomposity as well as falsehood in the strict sense, our model of independent-mindedness can expand further into the arts.

[639] . This correlation is far from perfect, though. Gödel and Dirac don’t seem to have been very strong in the humor department. But someone who is both “neurotypical” and humorless is very likely to be conventional-minded.

[640] . Exception: gossip. Almost everyone is curious about gossip.

[641] . The YC partners have so much practice doing this that they sometimes see paths that the founders themselves haven’t seen yet. The partners don’t try to seem skeptical, as buyers in transactions often do to increase their leverage. Although the founders feel their job is to convince the partners of the potential of their idea, these roles are not infrequently reversed, and the founders leave the interview feeling their idea has more potential than they realized.

[642] . In practice, 7 minutes would be enough. You rarely change your mind at minute 8. But 10 minutes is socially convenient.

[643] . I myself took the first sufficiently large acquisition offer in my first startup, so I don’t blame founders for doing this. There’s nothing wrong with starting a startup to make money. You need to make money somehow, and for some people startups are the most efficient way to do it. I’m just saying that these are not the startups that get really big.

[644] . Not these days, anyway. There were some big ones during the Internet Bubble, and indeed some big IPOs.

[645] . It’s interesting how many different ways there are not to be earnest: to be cleverly cynical, to be superficially brilliant, to be conspicuously virtuous, to be cool, to be sophisticated, to be orthodox, to be a snob, to bully, to pander, to be on the make. This pattern suggests that earnestness is not one end of a continuum, but a target one can fall short of in multiple dimensions. Another thing I notice about this list is that it sounds like a list of the ways people behave on Twitter. Whatever else social media is, it’s a vivid catalogue of ways not to be earnest.

[646] . People’s motives are as mixed in Silicon Valley as anywhere else. Even the founders motivated mostly by money tend to be at least somewhat interested in the problem they’re solving, and even the founders most interested in the problem they’re solving also like the idea of getting rich. But there’s great variation in the relative proportions of different founders’ motivations. And when I talk about “wrong” motives, I don’t mean morally wrong. There’s nothing morally wrong with starting a startup to make money. I just mean that those startups don’t do as well.

[647] . The most powerful motivator for most people is probably family. But there are some for whom intellectual curiosity comes first. In his (wonderful) autobiography, Paul Halmos says explicitly that for a mathematician, math must come before anything else, including family. Which at least implies that it did for him.

[648] . Interestingly, just as the word “nerd” implies earnestness even when used as a metaphor, the word “politics” implies the opposite. It’s not only in actual politics that earnestness seems to be a handicap, but also in office politics and academic politics.

[649] . It’s a bigger social error to seem naive in most European countries than it is in America, and this may be one of subtler reasons startups are less common there. Founder culture is completely at odds with sophisticated cynicism. The most earnest part of Europe is Scandinavia, and not surprisingly this is also the region with the highest number of successful startups per capita.

[650] . Much of business is schleps, and probably always will be. But even being a professor is largely schleps. It would be interesting to collect statistics about the schlep ratios of different jobs, but I suspect they’d rarely be less than 30%.

[651] . My experience skipped a step in the evolution of computers: time-sharing machines with interactive OSes. I went straight from batch processing to microcomputers, which made microcomputers seem all the more exciting.

[652] . Italian words for abstract concepts can nearly always be predicted from their English cognates (except for occasional traps like polluzione). It’s the everyday words that differ. So if you string together a lot of abstract concepts with a few simple verbs, you can make a little Italian go a long way.

[653] . I lived at Piazza San Felice 4, so my walk to the Accademia went straight down the spine of old Florence: past the Pitti, across the bridge, past Orsanmichele, between the Duomo and the Baptistery, and then up Via Ricasoli to Piazza San Marco. I saw Florence at street level in every possible condition, from empty dark winter evenings to sweltering summer days when the streets were packed with tourists.

[654] . You can of course paint people like still lives if you want to, and they’re willing. That sort of portrait is arguably the apex of still life painting, though the long sitting does tend to produce pained expressions in the sitters.

[655] . Interleaf was one of many companies that had smart people and built impressive technology, and yet got crushed by Moore’s Law. In the 1990s the exponential growth in the power of commodity (i.e. Intel) processors rolled up high-end, special-purpose hardware and software companies like a bulldozer.

[656] . The signature style seekers at RISD weren’t specifically mercenary. In the art world, money and coolness are tightly coupled. Anything expensive comes to be seen as cool, and anything seen as cool will soon become equally expensive.

[657] . Technically the apartment wasn’t rent-controlled but rent-stabilized, but this is a refinement only New Yorkers would know or care about. The point is that it was really cheap, less than half market price.

[658] . Most software you can launch as soon as it’s done. But when the software is an online store builder and you’re hosting the stores, if you don’t have any users yet, that fact will be painfully obvious. So before we could launch publicly we had to launch privately, in the sense of recruiting an initial set of users and making sure they had decent-looking stores.

[659] . We’d had a code editor in Viaweb for users to define their own page styles. They didn’t know it, but they were editing Lisp expressions underneath. But this wasn’t an app editor, because the code ran when the merchants’ sites were generated, not when shoppers visited them.

[660] . This was the first instance of what is now a familiar experience, and so was what happened next, when I read the comments and found they were full of angry people. How could I claim that Lisp was better than other languages? Weren’t they all Turing complete? People who see the responses to essays I write sometimes tell me how sorry they feel for me, but I’m not exaggerating when I reply that it has always been like this, since the very beginning. It comes with the territory. An essay must tell readers things they don’t already know, and some people dislike being told such things.

[661] . People put plenty of stuff on the internet in the 90s of course, but putting something online is not the same as publishing it online. Publishing online means you treat the online version as the (or at least a) primary version.

[662] . There is a general lesson here that our experience with Y Combinator also teaches: Customs continue to constrain you long after the restrictions that caused them have disappeared. Customary VC practice had once, like the customs about publishing essays, been based on real constraints. Startups had once been much more expensive to start, and proportionally rare. Now they could be cheap and common, but the VCs’ customs still reflected the old world, just as customs about writing essays still reflected the constraints of the print era. Which in turn implies that people who are independent-minded (i.e. less influenced by custom) will have an advantage in fields affected by rapid change (where customs are more likely to be obsolete). Here’s an interesting point, though: you can’t always predict which fields will be affected by rapid change. Obviously software and venture capital will be, but who would have predicted that essay writing would be?

[663] . Y Combinator was not the original name. At first we were called Cambridge Seed. But we didn’t want a regional name, in case someone copied us in Silicon Valley, so we renamed ourselves after one of the coolest tricks in the lambda calculus, the Y combinator. I picked orange as our color partly because it’s the warmest, and partly because no VC used it. In 2005 all the VCs used staid colors like maroon, navy blue, and forest green, because they were trying to appeal to LPs, not founders. The YC logo itself is an inside joke: the Viaweb logo had been a white V on a red circle, so I made the YC logo a white Y on an orange square.

[664] . YC did become a fund for a couple years starting in 2009, because it was getting so big I could no longer afford to fund it personally. But after Heroku got bought we had enough money to go back to being self-funded.

[665] . I’ve never liked the term “deal flow,” because it implies that the number of new startups at any given time is fixed. This is not only false, but it’s the purpose of YC to falsify it, by causing startups to be founded that would not otherwise have existed.

[666] . She reports that they were all different shapes and sizes, because there was a run on air conditioners and she had to get whatever she could, but that they were all heavier than she could carry now.

[667] . Another problem with HN was a bizarre edge case that occurs when you both write essays and run a forum. When you run a forum, you’re assumed to see if not every conversation, at least every conversation involving you. And when you write essays, people post highly imaginative misinterpretations of them on forums. Individually these two phenomena are tedious but bearable, but the combination is disastrous. You actually have to respond to the misinterpretations, because the assumption that you’re present in the conversation means that not responding to any sufficiently upvoted misinterpretation reads as a tacit admission that it’s correct. But that in turn encourages more; anyone who wants to pick a fight with you senses that now is their chance.

[668] . The worst thing about leaving YC was not working with Jessica anymore. We’d been working on YC almost the whole time we’d known each other, and we’d neither tried nor wanted to separate it from our personal lives, so leaving was like pulling up a deeply rooted tree.

[669] . One way to get more precise about the concept of invented vs discovered is to talk about space aliens. Any sufficiently advanced alien civilization would certainly know about the Pythagorean theorem, for example. I believe, though with less certainty, that they would also know about the Lisp in McCarthy’s 1960 paper. But if so there’s no reason to suppose that this is the limit of the language that might be known to them. Presumably aliens need numbers and errors and I/O too. So it seems likely there exists at least one path out of McCarthy’s Lisp along which discoveredness is preserved.

[670] . Unfortunately restricted donations tend to generate more publicity than unrestricted ones. “X donates money to build a school in Africa” is not only more interesting than “X donates money to Y nonprofit to spend as Y chooses,” but also focuses more attention on X.

[671] . Investment firms grew rapidly after a regulatory change by the Labor Department in 1978 allowed pension funds to invest in them, but the effects of this growth were not yet visible in the top 100 fortunes in 1982.

[672] . George Mitchell deserves mention as an exception. Though really driven and good at making deals, he was also the first to figure out how to use fracking to get natural gas out of shale.

[673] . When I say people are starting more companies, I mean the type of company meant to grow very big. There has actually been a decrease in the last couple decades in the overall number of new companies. But the vast majority of companies are small retail and service businesses. So what the statistics about the decreasing number of new businesses mean is that people are starting fewer shoe stores and barber shops. People sometimes get confused when they see a graph labelled “startups” that’s going down, because there are two senses of the word “startup”: (1) the founding of a company, and (2) a particular type of company designed to grow big fast. The statistics mean startup in sense (1), not sense (2).

[674] . Rockoff, Hugh. “Great Fortunes of the Gilded Age.” NBER Working Paper 14555, 2008.

[675] . Lind, Michael. Land of Promise. HarperCollins, 2012. It’s also likely that the high tax rates in the mid 20th century deterred people from starting their own companies. Starting one’s own company is risky, and when risk isn’t rewarded, people opt for safety instead. But it wasn’t simply cause and effect. The oligopolies and high tax rates of the mid 20th century were all of a piece. Lower taxes are not just a cause of entrepreneurship, but an effect as well: the people getting rich in the mid 20th century from real estate and oil exploration lobbied for and got huge tax loopholes that made their effective tax rate much lower, and presumably if it had been more common to grow big companies by building new technology, the people doing that would have lobbied for their own loopholes as well.

[676] . That’s why the people who did get rich in the mid 20th century so often got rich from oil exploration or real estate. Those were the two big areas of the economy that weren’t susceptible to consolidation.

[677] . The pure tech companies used to be called “high technology” startups. But now that startups can punch through the middle of the ice crust, we don’t need a separate name for the edges, and the term “high-tech” has a decidedly retro sound.

[678] . Higher valuations mean you either sell less stock to get a given amount of money, or get more money for a given amount of stock. The typical startup does some of each. Obviously you end up richer if you keep more stock, but you should also end up richer if you raise more money, because (a) it should make the company more successful, and (b) you should be able to last longer before the next round, or not even need one. Notice all those shoulds though. In practice a lot of money slips through them. It might seem that the huge rounds raised by startups nowadays contradict the claim that it has become cheaper to start one. But there’s no contradiction here; the startups that raise the most are the ones doing it by choice, in order to grow faster, not the ones doing it because they need the money to survive. There’s nothing like not needing money to make people offer it to you. You would think, after having been on the side of labor in its fight with capital for almost two centuries, that the far left would be happy that labor has finally prevailed. But none of them seem to be. You can almost hear them saying “No, no, not that way.”

[679] . IBM was created in 1911 by merging three companies, the most important of which was Herman Hollerith’s Tabulating Machine Company, founded in 1896. In 1941 its revenues were $60 million. Hewlett-Packard’s revenues in 1964 were $125 million. Microsoft’s revenues in 1988 were $590 million.

[680] . This domain expertise could be in another field. Indeed, such crossovers tend to be particularly promising.

[681] . I’m not claiming this principle extends much beyond math, engineering, and the hard sciences. In politics, for example, crazy-sounding ideas generally are as bad as they sound. Though arguably this is not an exception, because the people who propose them are not in fact domain experts; politicians are domain experts in political tactics, like how to get elected and how to get legislation passed, but not in the world that policy acts upon. Perhaps no one could be.

[682] . This sense of “paradigm” was defined by Thomas Kuhn in his Structure of Scientific Revolutions , but I also recommend his Copernican Revolution , where you can see him at work developing the idea.

[683] . This is one reason people with a touch of Asperger’s may have an advantage in discovering new ideas. They’re always flying on instruments.

[684] . Hall, Rupert. From Galileo to Newton. Collins, 1963. This book is particularly good at getting into contemporaries’ heads.

[685] . To be a nerd is to be socially awkward, and there are two distinct ways to do that: to be playing the same game as everyone else, but badly, and to be playing a different game. The smart nerds are the latter type.

[686] . The same qualities that make fierce nerds so effective can also make them very annoying. Fierce nerds would do well to remember this, and (a) try to keep a lid on it, and (b) seek out organizations and types of work where getting the right answer matters more than preserving social harmony. In practice that means small groups working on hard problems. Which fortunately is the most fun kind of environment anyway.

[687] . If success neutralizes bitterness, why are there some people who are at least moderately successful and yet still quite bitter? Because people’s potential bitterness varies depending on how naturally bitter their personality is, and how ambitious they are: someone who’s naturally very bitter will still have a lot left after success neutralizes some of it, and someone who’s very ambitious will need proportionally more success to satisfy that ambition. So the worst-case scenario is someone who’s both naturally bitter and extremely ambitious, and yet only moderately successful.

[688] . “Hobby” is a curious word. Now it means work that isn’t real work – work that one is not to be judged by – but originally it just meant an obsession in a fairly general sense (even a political opinion, for example) that one metaphorically rode as a child rides a hobby-horse. It’s hard to say if its recent, narrower meaning is a change for the better or the worse. For sure there are lots of false positives – lots of projects that end up being important but are dismissed initially as mere hobbies. But on the other hand, the concept provides valuable cover for projects in the early, ugly duckling phase.

[689] . Tiger parents, as parents so often do, are fighting the last war. Grades mattered more in the old days when the route to success was to acquire credentials while ascending some predefined ladder. But it’s just as well that their tactics are focused on grades. How awful it would be if they invaded the territory of projects, and thereby gave their kids a distaste for this kind of work by forcing them to do it. Grades are already a grim, fake world, and aren’t harmed much by parental interference, but working on one’s own projects is a more delicate, private thing that could be damaged very easily.

[690] . The complicated, gradual edge between working on one’s own projects and collaborating with others is one reason there is so much disagreement about the idea of the “lone genius.” In practice people collaborate (or not) in all kinds of different ways, but the idea of the lone genius is definitely not a myth. There’s a core of truth to it that goes with a certain way of working.

[691] . Collaboration is powerful too. The optimal organization would combine collaboration and ownership in such a way as to do the least damage to each. Interestingly, companies and university departments approach this ideal from opposite directions: companies insist on collaboration, and occasionally also manage both to recruit skaters and allow them to skate, and university departments insist on the ability to do independent research (which is by custom treated as skating, whether it is or not), and the people they hire collaborate as much as they choose.

[692] . If a company could design its software in such a way that the best newly arrived programmers always got a clean sheet, it could have a kind of eternal youth. That might not be impossible. If you had a software backbone defining a game with sufficiently clear rules, individual programmers could write their own players.

[693] . In “The Bus Ticket Theory of Genius” I said the three ingredients in great work were natural ability, determination, and interest. That’s the formula in the preceding stage; determination and interest yield practice and effort.

[694] . I mean this at a resolution of days, not hours. You’ll often get somewhere while not working in the sense that the solution to a problem comes to you while taking a shower, or even in your sleep, but only because you were working hard on it the day before. It’s good to go on vacation occasionally, but when I go on vacation, I like to learn new things. I wouldn’t like just sitting on a beach.

[695] . The thing kids do in school that’s most like the real version is sports. Admittedly because many sports originated as games played in schools. But in this one area, at least, kids are doing exactly what adults do. In the average American high school, you have a choice of pretending to do something serious, or seriously doing something pretend. Arguably the latter is no worse.

[696] . Knowing what you want to work on doesn’t mean you’ll be able to. Most people have to spend a lot of their time working on things they don’t want to, especially early on. But if you know what you want to do, you at least know what direction to nudge your life in.

[697] . The lower time limits for intense work suggest a solution to the problem of having less time to work after you have kids: switch to harder problems. In effect I did that, though not deliberately.

[698] . Some cultures have a tradition of performative hard work. I don’t love this idea, because (a) it makes a parody of something important and (b) it causes people to wear themselves out doing things that don’t matter. I don’t know enough to say for sure whether it’s net good or bad, but my guess is bad.

[699] . One of the reasons people work so hard on startups is that startups can fail, and when they do, that failure tends to be both decisive and conspicuous.

[700] . It’s ok to work on something to make a lot of money. You need to solve the money problem somehow, and there’s nothing wrong with doing that efficiently by trying to make a lot at once. I suppose it would even be ok to be interested in money for its own sake; whatever floats your boat. Just so long as you’re conscious of your motivations. The thing to avoid is unconsciously letting the need for money warp your ideas about what kind of work you find most interesting.

[701] . Many people face this question on a smaller scale with individual projects. But it’s easier both to recognize and to accept a dead end in a single project than to abandon some type of work entirely. The more determined you are, the harder it gets. Like a Spanish Flu victim, you’re fighting your own immune system: Instead of giving up, you tell yourself, I should just try harder. And who can say you’re not right?

[702] . What wins in conversation depends on who with. It ranges from mere aggressiveness at the bottom, through quick-wittedness in the middle, to something closer to actual intelligence at the top, though probably always with some component of quick-wittedness.

[703] . Just as intelligence isn’t the only ingredient in having new ideas, having new ideas isn’t the only thing intelligence is useful for. It’s also useful, for example, in diagnosing problems and figuring out how to fix them. Both overlap with having new ideas, but both have an end that doesn’t. Those ways of using intelligence are much more common than having new ideas. And in such cases intelligence is even harder to distinguish from its consequences.

[704] . Some would attribute the difference between intelligence and having new ideas to “creativity,” but this doesn’t seem a very useful term. As well as being pretty vague, it’s shifted half a frame sideways from what we care about: it’s neither separable from intelligence, nor responsible for all the difference between intelligence and having new ideas.

[705] . Curiously enough, this essay is an example. It started out as an essay about writing ability. But when I came to the distinction between intelligence and having new ideas, that seemed so much more important that I turned the original essay inside out, making that the topic and my original topic one of the points in it. As in many other fields, that level of reworking is easier to contemplate once you’ve had a lot of practice.

[706] . Machinery and circuits are formal languages.

[707] . I thought of this sentence as I was walking down the street in Palo Alto.

[708] . There are two senses of talking to someone: a strict sense in which the conversation is verbal, and a more general sense in which it can take any form, including writing. In the limit case (e.g. Seneca’s letters), conversation in the latter sense becomes essay writing. It can be very useful to talk (in either sense) with other people as you’re writing something. But a verbal conversation will never be more exacting than when you’re talking about something you’re writing.

[709] . Or more accurately, biographies of Newton, since Westfall wrote two: a long version called Never at Rest , and a shorter one called The Life of Isaac Newton. Both are great. The short version moves faster, but the long one is full of interesting and often very funny details. This passage is the same in both.

[710] . Another more subtle but equally damning bit of evidence is that claims of x-ism are never qualified. You never hear anyone say that a statement is “probably x-ist” or “almost certainly y-ist.” If claims of x-ism were actually claims about truth, you’d expect to see “probably” in front of “x-ist” as often as you see it in front of “fallacious.”

[711] . The rules must be strict, but they need not be demanding. So the most effective type of rules are those about superficial matters, like doctrinal minutiae, or the precise words adherents must use. Such rules can be made extremely complicated, and yet don’t repel potential converts by requiring significant sacrifice. The superficial demands of orthodoxy make it an inexpensive substitute for virtue. And that in turn is one of the reasons orthodoxy is so attractive to bad people. You could be a horrible person, and yet as long as you’re orthodox, you’re better than everyone who isn’t.

[712] . Arguably there were two. The first had died down somewhat by 2000, but was followed by a second in the 2010s, probably caused by social media.

[713] . Fortunately most of those trying to suppress ideas today still respect Enlightenment principles enough to pay lip service to them. They know they’re not supposed to ban ideas per se, so they have to recast the ideas as causing “harm,” which sounds like something that can be banned. The more extreme try to claim speech itself is violence, or even that silence is. But strange as it may sound, such gymnastics are a good sign. We’ll know we’re really in trouble when they stop bothering to invent pretenses for banning ideas – when, like the medieval church, they say “Damn right we’re banning ideas, and in fact here’s a list of them.”

[714] . People only have the luxury of ignoring the medical consensus about vaccines because vaccines have worked so well. If we didn’t have any vaccines at all, the mortality rate would be so high that most current anti-vaxxers would be begging for them. And the situation with freedom of expression is similar. It’s only because they live in a world created by the Enlightenment that kids from the suburbs can play at banning ideas.

[715] . This is why I’ve never liked it when people refer to YC as a “bootcamp.” It’s intense like a bootcamp, but the opposite in structure. Instead of everyone doing the same thing, they’re each talking to YC partners to figure out what their specific startup needs.

[716] . When I say the summer 2012 batch was broken, I mean it felt to the partners that something was wrong. Things weren’t yet so broken that the startups had a worse experience. In fact that batch did unusually well.

[717] . This situation reminds me of the research showing that people are much better at answering questions than they are at judging how accurate their answers are. The two phenomena feel very similar.

[718] . The Airbnbs were particularly good at listening – partly because they were flexible and disciplined, but also because they’d had such a rough time during the preceding year. They were ready to listen.

[719] . The optimal unit of decisiveness depends on how long it takes to get results, and that depends on the type of problem you’re solving. When you’re negotiating with investors, it could be a couple days, whereas if you’re building hardware it could be months.

[720] . I didn’t know when I was 9 that matter might behave randomly, but I don’t think it affects the problem much. Randomness destroys the ghost in the machine as effectively as determinism.

[721] . If you don’t like using an expression, you can make the same point using higher-order desires: There is some n such that you don’t control your nth- order desires.

[722] . Audiobooks can give you examples of good writing, but having them read to you doesn’t teach you as much about writing as reading them yourself.

[723] . By “good at reading” I don’t mean good at the mechanics of reading. You don’t have to be good at extracting words from the page so much as extracting meaning from the words. Japanese Translation Chinese Translation Italian Translation French Translation * * *

[724] . I don’t think you could give a precise definition of what counts as great work. Doing great work means doing something important so well that you expand people’s ideas of what’s possible. But there’s no threshold for importance. It’s a matter of degree, and often hard to judge at the time anyway. So I’d rather people focused on developing their interests rather than worrying about whether they’re important or not. Just try to do something amazing, and leave it to future generations to say if you succeeded.

[725] . A lot of standup comedy is based on noticing anomalies in everyday life. “Did you ever notice…?” New ideas come from doing this about nontrivial things. Which may help explain why people’s reaction to a new idea is often the first half of laughing: Ha!

[726] . That second qualifier is critical. If you’re excited about something most authorities discount, but you can’t give a more precise explanation than “they don’t get it,” then you’re starting to drift into the territory of cranks.

[727] . Finding something to work on is not simply a matter of finding a match between the current version of you and a list of known problems. You’ll often have to coevolve with the problem. That’s why it can sometimes be so hard to figure out what to work on. The search space is huge. It’s the cartesian product of all possible types of work, both known and yet to be discovered, and all possible future versions of you. There’s no way you could search this whole space, so you have to rely on heuristics to generate promising paths through it and hope the best matches will be clustered. Which they will not always be; different types of work have been collected together as much by accidents of history as by the intrinsic similarities between them.

[728] . There are many reasons curious people are more likely to do great work, but one of the more subtle is that, by casting a wide net, they’re more likely to find the right thing to work on in the first place.

[729] . It can also be dangerous to make things for an audience you feel is less sophisticated than you, if that causes you to talk down to them. You can make a lot of money doing that, if you do it in a sufficiently cynical way, but it’s not the route to great work. Not that anyone using this m.o. would care.

[730] . This idea I learned from Hardy’s A Mathematician’s Apology , which I recommend to anyone ambitious to do great work, in any field.

[731] . Just as we overestimate what we can do in a day and underestimate what we can do over several years, we overestimate the damage done by procrastinating for a day and underestimate the damage done by procrastinating for several years.

[732] . You can’t usually get paid for doing exactly what you want, especially early on. There are two options: get paid for doing work close to what you want and hope to push it closer, or get paid for doing something else entirely and do your own projects on the side. Both can work, but both have drawbacks: in the first approach your work is compromised by default, and in the second you have to fight to get time to do it.

[733] . If you set your life up right, it will deliver the focus-relax cycle automatically. The perfect setup is an office you work in and that you walk to and from.

[734] . There may be some very unworldly people who do great work without consciously trying to. If you want to expand this rule to cover that case, it becomes: Don’t try to be anything except the best.

[735] . This gets more complicated in work like acting, where the goal is to adopt a fake persona. But even here it’s possible to be affected. Perhaps the rule in such fields should be to avoid unintentional affectation.

[736] . It’s safe to have beliefs that you treat as unquestionable if and only if they’re also unfalsifiable. For example, it’s safe to have the principle that everyone should be treated equally under the law, because a sentence with a “should” in it isn’t really a statement about the world and is therefore hard to disprove. And if there’s no evidence that could disprove one of your principles, there can’t be any facts you’d need to ignore in order to preserve it.

[737] . Affectation is easier to cure than intellectual dishonesty. Affectation is often a shortcoming of the young that burns off in time, while intellectual dishonesty is more of a character flaw.

[738] . Obviously you don’t have to be working at the exact moment you have the idea, but you’ll probably have been working fairly recently.

[739] . Some say psychoactive drugs have a similar effect. I’m skeptical, but also almost totally ignorant of their effects.

[740] . For example you might give the nth most important topic (m-1)/m^n of your attention, for some m > 1. You couldn’t allocate your attention so precisely, of course, but this at least gives an idea of a reasonable distribution.

[741] . The principles defining a religion have to be mistaken. Otherwise anyone might adopt them, and there would be nothing to distinguish the adherents of the religion from everyone else.

[742] . It might be a good exercise to try writing down a list of questions you wondered about in your youth. You might find you’re now in a position to do something about some of them.

[743] . The connection between originality and uncertainty causes a strange phenomenon: because the conventional-minded are more certain than the independent-minded, this tends to give them the upper hand in disputes, even though they’re generally stupider. > The best lack all conviction, while the worst > Are full of passionate intensity.

[744] . Derived from Linus Pauling’s “If you want to have good ideas, you must have many ideas.”

[745] . Attacking a project as a “toy” is similar to attacking a statement as “inappropriate.” It means that no more substantial criticism can be made to stick.

[746] . One way to tell whether you’re wasting time is to ask if you’re producing or consuming. Writing computer games is less likely to be a waste of time than playing them, and playing games where you create something is less likely to be a waste of time than playing games where you don’t.

[747] . Another related advantage is that if you haven’t said anything publicly yet, you won’t be biased toward evidence that supports your earlier conclusions. With sufficient integrity you could achieve eternal youth in this respect, but few manage to. For most people, having previously published opinions has an effect similar to ideology, just in quantity 1.

[748] . In the early 1630s Daniel Mytens made a painting of Henrietta Maria handing a laurel wreath to Charles I. Van Dyck then painted his own version to show how much better he was.

[749] . I’m being deliberately vague about what a place is. As of this writing, being in the same physical place has advantages that are hard to duplicate, but that could change.

[750] . This is false when the work the other people have to do is very constrained, as with SETI@home or Bitcoin. It may be possible to expand the area in which it’s false by defining similarly restricted protocols with more freedom of action in the nodes.

[751] . Corollary: Building something that enables people to go around intermediaries and engage directly with their audience is probably a good idea.

[752] . It may be helpful always to walk or run the same route, because that frees attention for thinking. It feels that way to me, and there is some historical evidence for it.

[753] . Evolution itself is probably the most pervasive example of superlinear returns for performance. But this is hard for us to empathize with because we’re not the recipients; we’re the returns.

[754] . Knowledge did of course have a practical effect before the Industrial Revolution. The development of agriculture changed human life completely. But this kind of change was the result of broad, gradual improvements in technique, not the discoveries of a few exceptionally learned people.

[755] . It’s not mathematically correct to describe a step function as superlinear, but a step function starting from zero works like a superlinear function when it describes the reward curve for effort by a rational actor. If it starts at zero then the part before the step is below any linearly increasing return, and the part after the step must be above the necessary return at that point or no one would bother.

[756] . Seeking competition could be a good heuristic in the sense that some people find it motivating. It’s also somewhat of a guide to promising problems, because it’s a sign that other people find them promising. But it’s a very imperfect sign: often there’s a clamoring crowd chasing some problem, and they all end up being trumped by someone quietly working on another one.

[757] . Not always, though. You have to be careful with this rule. When something is popular despite being mediocre, there’s often a hidden reason why. Perhaps monopoly or regulation make it hard to compete. Perhaps customers have bad taste or have broken procedures for deciding what to buy. There are huge swathes of mediocre things that exist for such reasons.

[758] . In my twenties I wanted to be an artist and even went to art school to study painting. Mostly because I liked art, but a nontrivial part of my motivation came from the fact that artists seemed least at the mercy of organizations.

[759] . In principle everyone is getting superlinear returns. Learning compounds, and everyone learns in the course of their life. But in practice few push this kind of everyday learning to the point where the return curve gets really steep.

[760] . It’s unclear exactly what advocates of “equity” mean by it. They seem to disagree among themselves. But whatever they mean is probably at odds with a world in which institutions have less power to control outcomes, and a handful of outliers do much better than everyone else. It may seem like bad luck for this concept that it arose at just the moment when the world was shifting in the opposite direction, but I don’t think this was a coincidence. I think one reason it arose now is because its adherents feel threatened by rapidly increasing variation in performance.

[761] . Corollary: Parents who pressure their kids to work on something prestigious, like medicine, even though they have no interest in it, will be hosing them even more than they have in the past.

[762] . The original version of this paragraph was the first draft of “How to Do Great Work.” As soon as I wrote it I realized it was a more important topic than superlinear returns, so I paused the present essay to expand this paragraph into its own. Practically nothing remains of the original version, because after I finished “How to Do Great Work” I rewrote it based on that.

[763] . Before the Industrial Revolution, people who got rich usually did it like emperors: capturing some resource made them more powerful and enabled them to capture more. Now it can be done like a scientist, by discovering or building something uniquely valuable. Most people who get rich use a mix of the old and the new ways, but in the most advanced economies the ratio has shifted dramatically toward discovery just in the last half century.

[764] . It’s not surprising that conventional-minded people would dislike inequality if independent-mindedness is one of the biggest drivers of it. But it’s not simply that they don’t want anyone to have what they can’t. The conventional-minded literally can’t imagine what it’s like to have novel ideas. So the whole phenomenon of great variation in performance seems unnatural to them, and when they encounter it they assume it must be due to cheating or to some malign external influence.

[765] . There might be some resistance to this conclusion on the grounds that some of these discoveries could only be understood by a small number of readers. But you get into all sorts of difficulties if you want to disqualify essays on this account. How do you decide where the cutoff should be? If a virus kills off everyone except a handful of people sequestered at Los Alamos, could an essay that had been disqualified now be eligible? Etc. Darwin’s 1844 essay was derived from an earlier version written in 1839. Extracts from it were published in 1858.

[766] . When you find yourself very curious about an apparently minor question, that’s an exciting sign. Evolution has designed you to pay attention to things that matter. So when you’re very curious about something random, that could mean you’ve unconsciously noticed it’s less random than it seems.

[767] . Corollary: If you’re not intellectually honest, your writing won’t just be biased, but also boring, because you’ll miss all the ideas you’d have discovered if you pushed for the truth.

[768] . Sometimes this process begins before you start writing. Sometimes you’ve already figured out the first few things you want to say. Schoolchildren are often taught they should decide everything they want to say, and write this down as an outline before they start writing the essay itself. Maybe that’s a good way to get them started – or not, I don’t know – but it’s antithetical to the spirit of essay writing. The more detailed your outline, the less your ideas can benefit from the sort of discovery that essays are for.

[769] . The problem with this type of “greedy” algorithm is that you can end up on a local maximum. If the most valuable question is preceded by a boring one, you’ll overlook it. But I can’t imagine a better strategy. There’s no lookahead except by writing. So use a greedy algorithm and a lot of time.

[770] . I ended up reattaching the first 5 of the 17 paragraphs, and discarding the rest.

[771] . Stephen Fry confessed to making use of this phenomenon when taking exams at Oxford. He had in his head a standard essay about some general literary topic, and he would find a way to turn the exam question toward it and then just reproduce it again. Strictly speaking it’s the graph of ideas that would be highly connected, not the space, but that usage would confuse people who don’t know graph theory, whereas people who do know it will get what I mean if I say “space”.

[772] . Too far doesn’t depend just on the distance from the original topic. It’s more like that distance divided by the value of whatever I’ve discovered in the subtree.

[773] . Or can you? I should try writing about this. Even if the chance of succeeding is small, the expected value is huge.

[774] . There was a vogue in the 20th century for saying that the purpose of art was also to teach. Some artists tried to justify their work by explaining that their goal was not to produce something good, but to challenge our preconceptions about art. And to be fair, art can teach somewhat. The ancient Greeks’ naturalistic sculptures represented a new idea, and must have been extra exciting to contemporaries on that account. But they still look good to us.

[775] . Bertrand Russell caused huge controversy in the early 20th century with his ideas about “trial marriage.” But they make boring reading now, because they prevailed. “Trial marriage” is what we call “dating.”

[776] . If you’d asked me 10 years ago, I’d have predicted that schools would continue to teach hacking the test for centuries. But now it seems plausible that students will soon be taught individually by AIs, and that exams will be replaced by ongoing, invisible micro-assessments.

[777] . The rhetorical trick in this sentence is that the “Google”s refer to different things. What I mean is: a company that has as much chance of growing as big as Google ultimately did as Larry and Sergey could have reasonably expected Google itself would at the time they started it. But I think the original version is zippier.

[778] . Making something for your friends isn’t the only source of startup ideas. It’s just the best source for young founders, who have the least knowledge of what other people want, and whose own wants are most predictive of future demand.

[779] . Strangely enough this is particularly true in countries like the US where undergraduate admissions are done badly. US admissions departments make applicants jump through a lot of arbitrary hoops that have little to do with their intellectual ability. But the more arbitrary a test, the more it becomes a test of mere determination and resourcefulness. And those are the two most important qualities in startup founders. So US admissions departments are better at selecting founders than they would be if they were better at selecting students.

[780] . I’m going to use “persistent” for the good kind of stubborn and “obstinate” for the bad kind, but I can’t claim I’m simply following current usage. Conventional opinion barely distinguishes between good and bad kinds of stubbornness, and usage is correspondingly promiscuous. I could have invented a new word for the good kind, but it seemed better just to stretch “persistent.”

[781] . There are some domains where one can succeed by being obstinate. Some political leaders have been notorious for it. But it won’t work in situations where you have to pass external tests. And indeed the political leaders who are famous for being obstinate are famous for getting power, not for using it well.

[782] . There will be some resistance to turning the rudder of a persistent person, because there’s some cost to changing direction.

[783] . The obstinate do sometimes succeed in solving hard problems. One way is through luck: like the stopped clock that’s right twice a day, they seize onto some arbitrary idea, and it turns out to be right. Another is when their obstinacy cancels out some other form of error. For example, if a leader has overcautious subordinates, their estimates of the probability of success will always be off in the same direction. So if he mindlessly says “push ahead regardless” in every borderline case, he’ll usually turn out to be right.

[784] . If you stop there, at just energy and imagination, you get the conventional caricature of an artist or poet.

[785] . Start by erring on the small side. If you’re inexperienced you’ll inevitably err on one side or the other, and if you err on the side of making the goal too broad, you won’t get anywhere. Whereas if you err on the small side you’ll at least be moving forward. Then, once you’re moving, you expand the goal.

[786] . The more diplomatic way of phrasing this statement would be to say that experienced C-level execs are often very skilled at managing up. And I don’t think anyone with knowledge of this world would dispute that.

[787] . If the practice of having such retreats became so widespread that even mature companies dominated by politics started to do it, we could quantify the senescence of companies by the average depth on the org chart of those invited.

[788] . I also have another less optimistic prediction: as soon as the concept of founder mode becomes established, people will start misusing it. Founders who are unable to delegate even things they should will use founder mode as the excuse. Or managers who aren’t founders will decide they should try to act like founders. That may even work, to some extent, but the results will be messy when it doesn’t; the modular approach does at least limit the damage a bad CEO can do.

[789] . These examples show why it’s a mistake to assume that economic inequality must be evidence of some kind of brokenness or unfairness. It’s obvious that different people have different interests, and that some interests yield far more money than others, so how can it not be obvious that some people will end up much richer than others? In a world where some people like to write enterprise software and others like to make studio pottery, economic inequality is the natural outcome.

[790] . Difficulty choosing between interests is a different matter. That’s not always due to ignorance. It’s often intrinsically difficult. I still have trouble doing it.

[791] . You can’t always take people at their word on this. Since it’s more prestigious to work on things you’re interested in than to be driven by money, people who are driven mainly by money will often claim to be more interested in their work than they actually are. One way to test such claims is by doing the following thought experiment: if their work didn’t pay well, would they take day jobs doing something else in order to do it in their spare time? Lots of mathematicians and scientists and engineers would. Historically lots have. But I don’t think as many investment bankers would. This thought experiment is also useful for distinguishing between university departments.

[792] . This was not the original meaning of “woke,” but it’s rarely used in the original sense now. Now the pejorative sense is the dominant one.

[793] . Why did 1960s radicals focus on the causes they did? One of the people who reviewed drafts of this essay explained this so well that I asked if I could quote him: > The middle-class student protestors of the New Left rejected the > socialist/Marxist left as unhip. They were interested in sexier forms of > oppression uncovered by cultural analysis (Marcuse) and abstruse “Theory”. > Labor politics became stodgy and old-fashioned. This took a couple > generations to work through. The woke ideology’s conspicuous lack of > interest in the working class is the tell-tale sign. Such fragments as are, > er, left of the old left are anti-woke, and meanwhile the actual working > class shifted to the populist right and gave us Trump. Trump and wokeness > are cousins. > > The middle-class origins of wokeness smoothed its way through the > institutions because it had no interest in “seizing the means of production” > (how quaint such phrases seem now), which would quickly have run up against > hard state and corporate power. The fact that wokeness only expressed > interest in other kinds of class (race, sex, etc) signalled compromise with > existing power: give us power within your system and we’ll bestow the > resource we control – moral rectitude – upon you. As an ideological > stalking horse for gaining control over discourse and institutions, this > succeeded where a more ambitious revolutionary program would not have.

[794] . It helped that the humanities and social sciences also included some of the biggest and easiest undergrad majors. If a political movement had to start with physics students, it could never get off the ground; there would be too few of them, and they wouldn’t have the time to spare. At the top universities these majors are not as big as they used to be, though. A 2022 survey found that only 7% of Harvard undergrads plan to major in the humanities, vs nearly 30% during the 1970s. I expect wokeness is at least part of the reason; when undergrads consider majoring in English, it’s presumably because they love the written word and not because they want to listen to lectures about racism.

[795] . The puppet-master-and-puppet character of political correctness became clearly visible when a bakery near Oberlin College was falsely accused of race discrimination in 2016. In the subsequent civil trial, lawyers for the bakery produced a text message from Oberlin Dean of Students Meredith Raimondo that read “I’d say unleash the students if I wasn’t convinced this needs to be put behind us.”

[796] . The woke sometimes claim that wokeness is simply treating people with respect. But if it were, that would be the only rule you’d have to remember, and this is comically far from being the case. My younger son likes to imitate voices, and at one point when he was about seven I had to explain which accents it was currently safe to imitate publicly and which not. It took about ten minutes, and I still hadn’t covered all the cases.

[797] . In 1986 the Supreme Court ruled that creating a hostile work environment could constitute sex discrimination, which in turn affected universities via Title IX. The court specified that the test of a hostile environment was whether it would bother a reasonable person, but since for a professor merely being the subject of a sexual harassment complaint would be a disaster whether the complainant was reasonable or not, in practice any joke or remark remotely connected with sex was now effectively forbidden. Which meant we’d now come full circle to Victorian codes of behavior, when there was a large class of things that might not be said “with ladies present.”

[798] . Much as they tried to pretend there was no conflict between diversity and quality. But you can’t simultaneously optimize for two things that aren’t identical. What diversity actually means, judging from the way the term is used, is proportional representation, and unless you’re selecting a group whose purpose is to be representative, like poll respondents, optimizing for proportional representation has to come at the expense of quality. This is not because of anything about representation; it’s the nature of optimization; optimizing for x has to come at the expense of y unless x and y are identical.

[799] . Maybe societies will eventually develop antibodies to viral outrage. Maybe we were just the first to be exposed to it, so it tore through us like an epidemic through a previously isolated population. I’m fairly confident that it would be possible to create new social media apps that were less driven by outrage, and an app of this type would have a good chance of stealing users from existing ones, because the smartest people would tend to migrate to it.

[800] . I say “mostly” because I have hopes that journalistic neutrality will return in some form. There is some market for unbiased news, and while it may be small, it’s valuable. The rich and powerful want to know what’s really going on; that’s how they became rich and powerful.

[801] . The Times made this momentous announcement very informally, in passing in the middle of an article about a Times reporter who’d been criticized for inaccuracy. It’s quite possible no senior editor even approved it. But it’s somehow appropriate that this particular universe ended with a whimper rather than a bang.

[802] . As the acronym DEI goes out of fashion, many of these bureaucrats will try to go underground by changing their titles. It looks like “belonging” will be a popular option.

[803] . If you’ve ever wondered why our legal system includes protections like the separation of prosecutor, judge, and jury, the right to examine evidence and cross-examine witnesses, and the right to be represented by legal counsel, the de facto parallel legal system established by Title IX makes that all too clear.

[804] . The invention of new improprieties is most visible in the rapid evolution of woke nomenclature. This is particularly annoying to me as a writer, because the new names are always worse. Any religious observance has to be inconvenient and slightly absurd; otherwise gentiles would do it too. So “slaves” becomes “enslaved individuals.” But web search can show us the leading edge of moral growth in real time: if you search for “individuals experiencing slavery” you will as of this writing find five legit attempts to use the phrase, and you’ll even find two for “individuals experiencing enslavement.”

[805] . Organizations that do dubious things are particularly concerned with propriety, which is how you end up with absurdities like tobacco and oil companies having higher ESG ratings than Tesla.

[806] . Elon did something else that tilted Twitter rightward though: he gave more visibility to paying users. Paying users lean right on average, because people on the far left dislike Elon and don’t want to give him money. Elon presumably knew this would happen. On the other hand, the people on the far left have only themselves to blame; they could tilt Twitter back to the left tomorrow if they wanted to.

[807] . It even, as James Lindsay and Peter Boghossian pointed out, has a concept of original sin: privilege. Which means unlike Christianity’s egalitarian version, people have varying degrees of it. An able-bodied straight white American male is born with such a load of sin that only by the most abject repentance can he be saved. Wokeness also shares something rather funny with many actual versions of Christianity: like God, the people for whose sake wokeness purports to act are often revolted by the things done in their name.

[808] . There is one exception to most of these rules: actual religious organizations. It’s reasonable for them to insist on orthodoxy. But they in turn should declare that they’re religious organizations. It’s rightly considered shady when something that appears to be an ordinary business or publication turns out to be a religious organization.

[809] . I don’t want to give the impression that it will be simple to roll back wokeness. There will be places where the fight inevitably gets messy – particularly within universities, which everyone has to share, yet which are currently the most pervaded by wokeness of any institutions.

[810] . You can however get rid of aggressively conventional-minded people within an organization, and in many if not most organizations this would be an excellent idea. Even a handful of them can do a lot of damage. I bet you’d feel a noticeable improvement going from a handful to none.

[811] . We could treat all three as the same kind of should by saying that it’s one’s duty to live well – for example by saying, as some Christians have, that it’s one’s duty to make the most of one’s God-given gifts. But this seems one of those casuistries people invented to evade the stern requirements of religion: it was permissible to spend time studying math instead of praying or performing acts of charity because otherwise you were rejecting a gift God had given you. A useful casuistry no doubt, but we don’t need it. We could also combine the first two principles, since people are part of the world. Why should our species get special treatment? I won’t try to justify this choice, but I’m skeptical that anyone who claims to think differently actually lives according to their principles.

[812] . Confucius was also excluded from public life after ending up on the losing end of a power struggle, and presumably he too would not be so famous now if it hadn’t been for this long stretch of enforced leisure.

[813] . The closest thing to an exception is when you have to go back and insert a new point into the middle of something you’ve written. This often messes up the flow, sometimes in ways you can never quite repair. But I think the ultimate source of this problem is that ideas are tree-shaped and essays are linear. You inevitably run into difficulties when you try to cram the former into the latter. Frankly it’s surprising how much you can get away with. But even so you sometimes have to resort to an endnote.

[814] . Obviously if you shake the bin hard enough the objects in it can become less tightly packed. And similarly, if you imposed some huge external constraint on your writing, like using alternating one and two syllable words, the ideas would start to suffer.

[815] . Bizarrely enough, this happened in the writing of this very paragraph. An earlier version shared several phrases in common with the preceding paragraph, and the repetition bugged me each time I reread it. When I got annoyed enough to fix it, I discovered that the repetition reflected a problem in the underlying ideas, and I fixed both simultaneously.

[816] . It’s hard to write a really good essay about an unimportant topic, though, because a really good essayist will inevitably draw the topic into deeper waters. E. B. White could write an essay about how to boil potatoes that ended up being full of timeless wisdom. In which case, of course, it wouldn’t really be about how to boil potatoes; that would just have been the starting point.

[817] . The Bretton Woods agreement didn’t fix exchange rates between currencies directly. It fixed each relative to gold. Obviously this also fixed them relative to one another.

[818] . The Golden Ellipse isn’t quite a round rect, because the sides aren’t quite flat. It’s similar in shape to the superellipses popularized by Piet Hein in the early 1960s, and in fact that may be where they got the name. But mathematically it’s not an actual superellipse. My guess is that Patek’s designer just experimented with French curves till he got something he liked. And to be fair it is a good shape.

[819] . It was ironic that Patek Philippe of all companies made this mistake, because Adrien Philippe was the inventor of the modern crown. But they must have realized what they’d done, because later Ellipses have if anything excessively prominent crowns.

[820] . The high ratio of design space to practitioners in fine art has combined with the practical importance of attribution to give people the impression that painting in a distinctively Leonardesque way is what makes Leonardo good. The most dangerous problem faced by curators, art historians, and art dealers – the one that has the worst consequences if they get the wrong answer – is attribution. So inevitably they spend a lot of time thinking and talking about the features that distinguish the work of one artist from another. But those aren’t what make artists good. What makes the line of a woman’s cheek in a Leonardo drawing good is how good it looks as the line of a cheek, not how little it looks like lines made by other artists. Because painting has such prestige, the myth that having a distinctive style (rather than painting well) is the defining quality of great artists has in turn given cover to a lot of bad design in adjacent fields. A brand that does something hideous to distinguish their products can say “Like all great works of art, ours have a distinctive style,” and people will buy it.

[821] . An ad that Patek Philippe ran in America in 1970 famously described a Patek 3548 with a gold bracelet as a “$1700 trust fund.” Was it actually a good investment? In the very best case a dealer might pay you $20k now for one in unworn condition with its original box and papers. That’s about a 4.5% rate of return, which is not absolutely terrible. But apparently the average rate of return on S&P; 500 stocks over this period was more like 10%, if you reinvested all the dividends after paying taxes on them. The average rate of return would have been over 9% if you merely bought a lump of gold that hadn’t been made into a watch. So, not surprisingly, the ad wasn’t very good investment advice.

[822] . Tania Edwards, who ran US marketing for Patek Philippe in the 90s, said that Bittel literally sketched the design of the 3919 on a piece of paper. This sounds odd to me, because the 3919 looked exactly like the existing 3520 with the addition of sub seconds (a small dial with a second hand above 6 o’clock). Why would you sketch a design almost identical to an existing watch when you could just point to the existing watch and say “that, with sub seconds.” What this story does show, though, is the degree to which people within Patek felt their ad agency was responsible for the design of the 3919.

[823] . If I had to date the turning point for mechanical watches precisely, I’d say 1986. Unit sales of Swiss watches rebounded in 1985, but revenue didn’t, which means what we’re seeing is the boom in cheap quartz Swatches. Indeed, sales of mechanical watches must have been down if revenue was flat despite the sale of all those Swatches. Whereas in 1986 revenue turns sharply upward even though unit sales only increase by a little, which implies a corresponding increase in sales of expensive mechanical watches.

[824] . There is of course another reason some people are into mechanical watches: because they’re interested in old technology. And if you are genuinely interested in mechanical watches, there’s good news. You don’t have to wear a billboard on your wrist or pay a lot to own one. Just buy golden age watches. They still keep good time, they’re much more beautiful, and they cost a fraction of what new watches cost. The key to buying a golden age watch is to find a good dealer, and the best way to recognize one is by how much they tell you about the watch. A bad dealer will just have a lot of fluff about the prestige of the brand and the sleek lines of the case. A good dealer will tell you the model number of the watch and movement, have lots of pictures, including some with the case back open, give you dimensions, disclose all damage and restoration, and tell you exactly how accurately the watch is running. Good dealers tend to be watch nerds themselves, so they’re into this kind of thing. (There are a few independent watchmakers trying earnestly to make good mechanical watches now, but their efforts show how hard it is to do good work when the current is against you.)

[825] . Oddly enough it might have helped that the 3919 was hand wound. If a watch runs for long enough, 5 seconds a day starts to add up. After three months a watch that gains 5 seconds a day will be 7 minutes fast. But with a hand wound watch you occasionally forget to wind it, and it runs down. And when you wind it again you reset it – on average to a time about 30 seconds behind the actual time. So if you forgot to wind a 3919 every two weeks or so, it would rarely have shown the wrong time.

[826] . There’s one brand still waiting to be reinflated: Universal Genève, which was one of the big players of the golden age but since 1977 has been little more than a brand name passed from acquirer to acquirer. They’re scheduled to come back to life later this year, no doubt with stories about their long tradition of watchmaking.

[827] . More precisely, a high ratio of size to accuracy meant cheap. It’s easier to make a larger movement keep good time, but between two watches of the same accuracy, the larger was usually the cheaper.

[828] . Their form did once follow function. They were originally diving watches. But they’re long since obsolete for this purpose. Present day diving watches (now called dive computers) are digital and tell you much more than the time.

[829] . Rolex was awarded an average of 16.6 patents per year in the 1950s, but only 1.7 per year in the 1960s. Pierre-Yves Donzé, The Making of a Status Symbol: A Business History of Rolex , Manchester University Press, 2025.

[830] . Rolexes also shared something more specific with SUVs: aspirational manliness. An internal 1967 report by Rolex’s ad agency J. Walter Thompson explained the idea they were trying to convey: “Because a Rolex is designed for any situation, however rough or dangerous or heroic or exalted, it implies that the man who wears it is, potentially, a hero.” Reprinted in Donzé, op cit.

[831] . This business model only works when purchase decisions are driven mainly by brand. In a normal market, if one manufacturer restricts production, customers just buy from whichever competing manufacturer offers something as good. It’s only when customers are seeking a certain brand rather than a certain level of performance that you can manipulate them by restricting its availability.

[832] . Of course the first question one has on noticing a bubble is: will it burst? The reason ordinary bubbles eventually burst is that speculators get overoptimistic, but in this case the CEO of Patek Philippe controls the “money supply” and can thus take measures to cool down an overheated market. So there are probably only two things that could cause their specific bubble to burst: if his successor is not as capable, or if the whole custom of wearing mechanical watches goes away. The latter seems the greater danger. People aren’t going to wear three things on their wrists, so all it would take is for there to be two popular devices that were worn on the wrist, and mechanical watches would start to be seen by the next cohort of young rich people as an old guy thing. It’s hard to imagine a luxury watch brand surviving that.

[833] . It’s possible to get a higher rate of return if you’re willing to risk losing your capital. But to convert between tax rates you should use the risk- free rate of return, because considered as an anti-investment, a wealth tax is absolutely risk-free: you will absolutely owe the government that money. And while you do have to put “risk-free” in scare quotes when talking about returns, the kind of risks you’re talking about now are the almost apocalyptic kind that would make tax rates a moot point.

[834] . The same conversion rate applies to capital gains. The source of the multiple is whether the money is taxed every year or just once. Indeed it’s the same math you’d use to calculate the value of any income-generating asset.

[835] . You can deduct some state tax from your federal income taxes, but there’s a cap on how much you can deduct, which means in the marginal case we simply add the two rates.
