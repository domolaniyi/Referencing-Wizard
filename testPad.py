import NlpEngine
# delete file once complete
import SearchEngine
import time
import texts
import ApiEngine
import Article
from bs4 import BeautifulSoup
import requests
import numpy

Search_Engine = SearchEngine.SearchEngine()
Api_Engine = ApiEngine.ApiEngine()
Nlp_Engine = NlpEngine.NlpEngine()
Document = Article.Article("hello","dom dom","1","10.1016/j.patcog.2022.109225","10/10/10","https://test")

# Nlp_Engine1 = NlpEngine.NlpEngine()

text = "Figures 1 and 2 are scatterplots which compare the metrics Weighted Methods Per Class (WMC) and Coupling " \
           "Between Objects (CBO). From using these metrics to analyse the 2 systems I was able make some key " \
           "findings. Firstly, I gathered the correlation coefficients for both systems. The correlation for system 2 " \
           "was 0.29 while the correlation for system 3 was 0.25. When comparing the correlations both systems do " \
           "show some correlation between CBO and WMC however this relationship is weak. From the comparison it shows " \
           "that CBO doesn’t have a strong impact on WMC and vice versa. It also shows that although a particular " \
           "class may have tight coupling this has hardly any impact on how complex the class is. These findings " \
           "aren’t particularly unusual because the complexity of a class and it’s coupling are independent. A highly " \
           "complex class doesn’t necessarily mean that it is more likely to have a high coupling and evidently from " \
           "the correlation coefficients for both systems this is true. However, although there isn’t a strong " \
           "relationship between these two metrics, from my findings both systems have points where there are strong " \
           "code smells and where refactoring can be done to decrease the smells. Firstly, Shotgun Surgery is a " \
           "strong code smell which is given off by an outlier within Figure 1. This outlier has a WMC of 26 and a " \
           "CBO of 223. The CBO for this class is extremely high to the point where if one small change is made to " \
           "one class, many other changes to other classes may also need to be made. One way this could be combated " \
           "is by using Extract Class Refactoring. This type of refactoring can drastically decrease the coupling of " \
           "a class if done correctly, this is also suggested by Tramontana who talks about how Extract " \
           "Class refactoring can be ‘used to the lower the complexity of the original class’. However, when doing " \
           "Extract Class Refactoring some considerations need to also be accounted so you don’t end up in the same " \
           "place you started. The technique shouldn’t focus on purely on how cohesive specific parts of the code is " \
           "but also how coupled it is. Alzahrani builds on this saying ‘neglecting the coupling between them " \
           "can result in classes that are highly cohesive yet tightly coupled because increasing the cohesion of the " \
           "extracted class can lead to increasing the coupling between them’. In essence, when performing this " \
           "refactoring there should be a fine line established to avoid favouring one thing over another. Similarly, " \
           "within Figure 2 there is an outlier which has a WMC of 50 and a CBO of 228. The same techniques can also " \
           "be used on this class to help reduce its CBO. "

text1 = "A commonly observed ambiguity of a class is simply a reflection of multiple methods’ implementation within an " \
           "individual class. The process of Extract Class refactoring is, therefore, used to separate the different " \
           "responsibilities of a class into different classes. A major limitation in existing approaches of the Extract " \
           "Class refactoring is based on factors that are internal to the class, i.e., structural and semantic " \
           "relationships between methods, in order to identify and separate the responsibilities of the class which are " \
           "inadequate in many cases. Thus, we propose a novel approach that exploits the clients of the class to support " \
           "the Extract Class refactoring. The importance of this approach lies in its usefulness to support existing " \
           "approaches since it involves factors external to the class, i.e., the clients. Moreover, an extensive " \
           "empirical evaluation is presented to support the proposed method through the utilization of real classes " \
           "selected from two open source systems. The result shows the potential of our proposed approach and usefulness " \
           "that leads to an improvement in the quality of the considered classes. "

text2 = "The main goal of software design is to continue slicing the code to fit the human mind. A likely reason for " \
           "that is related to the fact that human work can be improved by a focus on a limited set of data. However, " \
           "even with advanced practices to support software quality, complex codes continue to be produced, resulting in " \
           "cognitive overload for the developers. Cognitive-Driven Development (CDD) is an inspiration from cognitive " \
           "psychol- ogy that aims to support the developers in defining a cognitive complexity constraint for the source " \
           "code. The main idea behind the CDD is keeping the implementation units under this constraint, even with the " \
           "continuous expansion of software scale. This paper presents an experimental study for verifying the CDD " \
           "effects in the early stages of development compared to conventional practices. Projects adopted for hiring " \
           "developers in Java by important Brazilian software companies were chosen. 44 experienced software engineers " \
           "from the same company attended this experiment and the CDD guided part of them. The projects were evaluated " \
           "with the following metrics: CBO (Coupling between objects), WMC (Weight Method Class), RFC (Response for a " \
           "Class), LCOM (Lack of Cohesion of Methods) and LOC (Lines of Code). The result suggests that CDD can guide " \
           "the developers to achieve better quality levels for the software with lower dispersion for the values of such " \
           "metrics. "

text3 = "The goal of ECR is to extract classes from the original class that have high cohesion and low coupling between " \
        "each other. Therefore, ECR can be considered as an optimization problem in which the aim is to maximize the " \
        "cohesion of the extracted classes while minimizing the coupling between them as much as possible. To this aim, " \
        "a greedy approach is proposed to address the ECR problem. A greedy approach is an algorithmic technique that can " \
        "be used to tackle optimization problems. Although this technique is not always guaranteed to find the optimal " \
        "solution, it has been used to optimally solve a wide range of optimization problems such as Huffman coding and " \
        "fractional knapsack problems [36]. Greedy algorithms solve a problem by selecting the best (greedy) choice at " \
        "the moment that solves part of the problem and reduces its size without considering the final optimal solution " \
        "of the whole problem. Figure 1 gives a process overview of the proposed ECR approach. The details of the process " \
        "are better explained in Algorithm 1. The algorithm takes as an input the class to undergo ECR and outputs a set " \
        "of classes suggested to be extracted from the input class. The algorithm initially takes each method in the input " \
        "class and put it into a separate class and adds all resulting classes into a set S. Then the algorithm makes " \
        "a greedy choice by merging the two classes in the set S that have the highest coupling, (see Algorithm 2), " \
        "compared to the coupling between any other two classes in the set. This choice will reduce the size of the " \
        "problem (i.e., |S|) by one. The algorithm repeats the previous step until the size of the problem become 2 " \
        "which means there are only 2 classes in the set S. The algorithm stores the classes in the set S and their β(S)" \

text4 = "Most cyber-physical system (CPS) applications are safety-critical; misbehavior caused by random failures or " \
        "cyber-attacks can considerably restrict their growth. Thus, it is important to protect CPS from being " \
        "damaged in this way [1]. Current security solutions have been well-integrated into many networked systems " \
        "including the use of middle boxes, such as antivirus protection, firewall, and intrusion detection systems (" \
        "IDS). A firewall controls network traffic based on the source or destination address. It alters network " \
        "traffic according to the firewall rules. Firewalls are also limited to their knowledge of the hosts " \
        "receiving the content and the amount of state available. An IDS is a type of security tool that scans the " \
        "system for suspicious activity, monitors the network traffic, and alerts the system or network administrator " \
        "[2]. In this context, a number of frameworks and mechanisms have been suggested in recent papers. In this " \
        "paper, we have considered SQL injection attacks that target the HTTP/HTTPS protocol, which aim to pass " \
        "through the web application firewall (WAF) and obtain an unauthorized access to proprietary data. SQL " \
        "injection belongs to the injection family of web attacks, wherein an attacker inserts inputs into a system " \
        "to execute malicious statements. The victim system is usually not ready to process this input, " \
        "typically resulting in data leakage and/or granting of unauthorized access to the attacker; in this case, " \
        "the attacker can access and/or modify the data, affecting all aspects of security, including " \
        "confidentiality, integrity, and data availability [3]. In an SQL injection, the attacker inserts an SQL " \
        "statement into an exchange between a client and database server [3]. SQL (structured query language) is used " \
        "to represent queries to database management systems (DBMSs). The maliciously injected SQL statement is " \
        "designed to extract or modify data from the database server. A successful injection can result in " \
        "authentication and bypass and changes to the database by inserting, modifying, and/or deleting data, " \
        "causing data loss and/or destruction of the entire database. Furthermore, such an attack could overrun and " \
        "execute commands on the hosted operating system, typically leading to more serious consequences [4]. Thus, " \
        "SQL injection attacks present aserious threats to organizations. A variety of research has been undertaken " \
        "to address this threat, presenting various artificial intelligence (AI)techniques for detection of SQL " \
        "injection attacks using machine learning and deep learning models [5]. AI techniques to facilitate the " \
        "detection of threats are usually implemented via learning from historical data representing an attack and/or " \
        "normal data. Historical data are useful for learning, in order to recognize patterns of attacks, " \
        "understanding detected traffic, and even predicting future attacks before they occur [6]. "

text5 = "The first deepfake content published on the Internet was a celebrity pornographic video that was created by " \
        "a Reddit user (named deepfake) in 2017. The Generative Adversarial Network (GAN) was first introduced in " \
        "2014 and used for image-enhancement purposes only [4]. However, since the first published deepfake media, " \
        "it has been unavoidable for deepfake and GAN technology to be used for malicious uses. Therefore, in 2017, " \
        "GANs were used to generate new facial images for malicious uses for the first time [5]. Following that, " \
        "there has been a constant development of other deepfake-based applications such as FakeApp and FaceSwap. In " \
        "2019, Deepnude was developed and provided undressed videos of the input data [6]. The widespread strategies " \
        "used to manipulate multimedia files can be broadly categorized into the following major categories: " \
        "copy–move, splicing, deepfake, and resampling [7]. Copy–move, splicing and resampling involve repositioning " \
        "the contents of a photo, overlapping different regions of multiple photos into a new one, and manipulating " \
        "the scale and position of components of a photo. The final goal is to manipulate the user by conveying the " \
        "deception of having a larger number of components in the photograph than those that were initially present. " \
        "Deepfake media, however, leveraging powerful machine-learning (ML) techniques, have significantly improved " \
        "the manipulation of the contents. Deepfake can be considered to be a type of splicing, where a person’s " \
        "face, sound, or actions in media is swiped by a fake target [8]. A wide set of cybercrime activities are " \
        "usually associated with this type of manipulation technique, and while spreading them is easy, correcting " \
        "the records and avoiding deepfakes are harder [9]. Consequently, it is becoming harder for machine-learning " \
        "techniques to identify convolutional traces of deepfake generation algorithms, as there needs to be " \
        "frequency-specific anomaly analysis. The most basic algorithms that were being used to train models for the " \
        "task of deepfake detection such as Support Vector Machine (SVM), Convolution Neural Network (CNN), " \
        "and Recurrent Neural Network (RNN) are now being coupled with multi-attentional [10] or ensemble [11] " \
        "methods to increase the performance and address weakness of other methods. As proposed by [12], " \
        "by implementing an ensemble of standard and attention-based data-augmented detection networks, " \
        "the generalization issue of the previous approaches can be avoided. As such, it is of high importance to " \
        "identify the most suitable algorithms for the backbone layers in multi-attentional and ensembled " \
        "architectures. As generation of deepfake media only started in 2017, academic writing on the problem is " \
        "meager [13]. Most of the developed and published methods/techniques are focused on deepfake videos. The main " \
        "difference between deepfake video- and image-detection methods is that video-detection methods can leverage " \
        "spatial features [14], spatio-temporal anomalies [15] and supervised domain [16] to draw a conclusion on the " \
        "whole video by aggregating the inferred output both in time and across multiple faces. However, " \
        "deepfake image-detection techniques have access to one face image only and mostly leverage pixel- [17] and " \
        "noise-level analysis [18] to identify the traces of the manipulation method.Therefore, identifying the most " \
        "reliable methods for face-image forgery detection that relies on convolutional neural networks (CNN) as the " \
        "backbone for a binary classification task could provide valuable insight for the future direction in the " \
        "development of deepfake-detection techniques. "

text6 = "The industrial problem of wear can significantly damage the overlapping components that move by each other [" \
        "1]. There are a number of different factors that can impact the wear rate, including the metal hardness, " \
        "sliding time and applied load [2]. Moreover, a number of methods can be used to reduce wear, " \
        "such as applying lubricants to surfaces or using cast iron metal as it contains graphite pellets that can " \
        "lubricate the surfaces of moving components [3]. Many academics have carried out experimental studies to " \
        "investigate wear whilst also considering a variety of factors that have been identified in earlier studies [" \
        "4,5]. Artificial intelligence (AI) technology has been developed over the last thirty years and has become " \
        "one of the most popular ways to predict and overcome various engineering issues in different fields, " \
        "particularly in industrial applications [6], as it can resolve and predict nonlinear relationships between " \
        "the input and output parameters. Meanwhile, of all the AI machine learning approaches available, " \
        "the artificial neural network (ANN) is considered to be one of the most important and popular [7]. ANNs were " \
        "used to model and optimize various systems in the field of material science and this is primarily due to " \
        "their flexibility and ability to understand problems without needing to know the exact details of the " \
        "mathematical model. In fact, it does not even need to have information about the physical conditions. For " \
        "instance, Radosaw et al. estimated the tensile strength of ductile iron friction welded joints using hybrid " \
        "intelligence methods [8]. The primary goal of their work was to use support vector regression (SVR), " \
        "genetic algorithms (GA) and an imperialist competitive approach to maximize the welding parameters (ICA). " \
        "The findings demonstrated that the TS of 256.93 MPa was achieved using SVR plus GA algorithms with heating " \
        "force welding parameters of 40 kN, a heating time of 300 s, and an upsetting force of 10.12 kN. In addition, " \
        "the use of hybrid intelligent approaches enhanced the TS joints from 211 to 258mpa for the ZT-14 type " \
        "friction welder. Similarly, Vaira et al. used an ANN approach incorporating the Levenberg–Marquardt " \
        "algorithm to predict the tensile strength of friction stir welded (FSW) for the AA1100 aluminum alloy [9]. " \
        "Rotation speed, welding speed, shoulder diameter, and pin diameter were all applied as the ANN model’s input " \
        "parameters. The findings for the projected TS show that the ANN model is effective in predicting the tensile " \
        "stress when these input parameters are present. The mechanical characteristics of ductile cast iron were " \
        "identified by Zmak et al., utilizing ANN based on the error back-propagation training technique [10]. The " \
        "multilayer hidden layers of the ANN model had sigmoid activation functions. The 13 weights of chemical " \
        "elements in melt were the input parameters used in the ANN model. Subsequently, the output included tensile " \
        "and yield strength, hardness, and elongation. Additionally, Perzyk et al. built and trained a variety of ANN " \
        "models to predict the quality of ductile cast iron and the findings indicated that ANN models are effective " \
        "for use in melt shop on-line production control [11]. Furthermore, Anand et al. estimated the friction " \
        "welding process parameters of Incoloy 800H joints and correlated the input and output responses of the " \
        "friction welding using a hybrid ANN method incorporating the optimization algorithm [12]. It also explored " \
        "how the best strength and hardness of joints can be achieved with the shortest burn-off length. The findings " \
        "indicated that the friction welding process parameters may be accurately predicted using an ANN model " \
        "combined with a genetic algorithm. Meanwhile, the friction coefficient and wear rate were examined in Kumar " \
        "et al.’s study using an ANN model under the influence of various loads, pin heating temperature, and speed. " \
        "The findings highlighted a significant relationship between the anticipated and measured values, " \
        "with a correlation factor of 0.99447 [13]. However, a number of friction systems have employed ANN to " \
        "design, forecast, and optimize friction parameters. By combining Elman’s recurrent configuration with the " \
        "ANN approach, Xiao and Zhu established several friction characteristics. The outcomes led to an improvement " \
        "in material formulation, which was supported by evidence from research trials and experiments [14]. "


# TEST DATA - SHORT TEXT(LENGTH 250 OR LESS)

test_short_1 = "studied the relationship between refactorings and code changes to identify developers’ motivations of " \
               "applying refactorings. In contrast to other studies mainly interviewed developers to investigate " \
               "their refactoring motivations, the study by exploited the analysis of software repositories. One of " \
               "the main findings of the study suggest that, developers apply more complex refactorings during the " \
               "implementation of new features in order to improve code cohesion and conformity to  principles. " \
               "Further analysis revealed that, among the key developers’ motivations to refactor code when " \
               "implementing new features is to reduce the piled up technical debts before introducing new code. " \
               "Generally, these studies suggest that, refactoring is mostly motivated by the changes in the " \
               "requirements. However, refactoring recommendation approaches to facilitate developers in refactorings " \
               "selection during feature requests implementation are still scarce. Some few examples include the " \
               "approaches proposed recently by.  These approaches exploit past history of feature requests, " \
               "code smells, and applied refactorings to train the classifiers for predicting the need for " \
               "refactoring and recommending types of refactoring that would be required. To detect previously " \
               "applied refactorings, the approaches rely solely on refactoring detectors. "

test_short_2 = "A production system produces items according to certain specifications through the integration of " \
               "human resources, equipment, raw materials, and other resources. In this process, complex production " \
               "resources need to be allocated according to the needs of multiple stakeholders. If the allocation of " \
               "resources is unreasonable, it may lead to the waste of production resources or the overload of " \
               "workers, which results in reducing production efficiency and increasing production costs. Production " \
               "scheduling refers to allocating equipment, human resources, and operations to optimize work loads, " \
               "and it is applied as a common method to balance the production requirements and resources to maximize " \
               "productivity. Production scheduling process primarily includes modeling and solving. Although the " \
               "production scheduling method has been applied in the production field for a long time, the following " \
               "problems still exist.The production scheduling process involving multiple stakeholders and complex " \
               "cooperation results in a high communication cost. Stakeholders participate in different aspects of " \
               "the scheduling process to interact with information and material. It is difficult to describe the " \
               "real scheduling process completely if the information is only described using natural language when " \
               "modeling. In addition, there are risks of change and ambiguity in the communication between different " \
               "stakeholders, which may lead to an information delay and ambiguity. It is difficult to integrate and " \
               "interact with the production scheduling data when modeling production scheduling, owing to the lack " \
               "of a unified expression. "

test_short_3_not_used = "Due to the development of preventive and diagnostic methods, as well as the available treatments for " \
               "various medical problems, the lifespans of companion dogs have increased considerably. Increased " \
               "anxiety, confusion, sleep-wake cycle alterations, barking or howling at night, forgetting previous " \
               "training, getting lost in familiar places, and. The central nervous system (CNS) of older dogs " \
               "undergoes specific changes during the aging process. Their brains may exhibit several morphological " \
               "changes. Aging of the human brain is characterized by a progressive reduction in the volume of the " \
               "parenchyma. The pathological alterations observed, which include the accumulation of amyloid beta " \
               "peptides and formation of senile plaques. Cognitive dysfunction syndrome (CDS) is a condition that " \
               "causes behavioural changes in senior and geriatric dogs, which are not the result of medical " \
               "pathology such as infection, failure of some organs or neoplasia. CDS is a chronic, progressive " \
               "neurodegenerative condition that is characterized by changes in behaviour, memory, learning capacity, " \
               "social interaction. Most common CDS signs are characterized by disorientation, alterations in " \
               "interactions with owners, sleep-wake cycle disturbances. CDS diagnoses are based on the " \
               "identification of alterations in cognitive functions and the exclusion of other diseases that " \
               "directly or indirectly affect the thalamocortical region, such as hepatic encephalopathy, " \
               "hypothyroidism, intracranial neoplasia, or cerebrovascular accidents. "

test_short_3 = "In the current era, software productivity can be effectively improved through object-oriented " \
               "analysis and design, so as to further improve the quality of software, reduce the time required for " \
               "development, and adjust the overall complexity of the system. Because this method supports the " \
               "decomposition, abstraction, modularization and reuse of the system, it is widely used and has " \
               "achieved success in various fields. UML is a standard notation for object-oriented analysis and " \
               "design. It has been recognized and applied in a wide range of system design fields, and has been " \
               "actually used in various fields. It belongs to a modeling language and has the main characteristics " \
               "of visualization. It can describe the specific system through a series of graphical symbols, " \
               "such as class diagram, use case diagram, state diagram, etc., and can accurately and clearly show the " \
               "system structure, system behavior and system function of the target system through different system " \
               "level abstract description. UML uses visual modeling tools to enable developers to obtain an accurate " \
               "and complete understanding of the target system through the integrated engineering definition, " \
               "analysis, design, production, testing and maintenance process of the structural and behavioral " \
               "characteristics of system requirements. With the continuous development of Internet technology, " \
               "the informatization level of various fields is gradually improving, and the amount of data is also " \
               "increasing with the passage of time, so is UML diagram. Improving UML diagram data not only increases " \
               "the amount of data, but also increases the structural complexity between UML diagrams. "

test_short_4 = "Autoimmune neurological disorders of central nerve system (CNS) can be paraneoplastic and " \
               "non-paraneoplastic. Paraneoplastic autoimmune neurological syndrome is a group of disorders caused by " \
               "cancer affecting nervous system by different immunological mechanisms which are independent of " \
               "metastatic process, metabolic or drug side effects. Limbic encephalitis (LE) is among the common " \
               "autoimmune neurological disorders. Limbic system is a center that comprises hippocampal formation, " \
               "septal region, cingulate gyrus, parahippocampal gyrus, indusium griseum, amygdaloid complex, " \
               "and mammillary body; it regulates memory, emotional responses, self-protection, sleep, appetite, " \
               "anger, fear, sexual behavior and motivation functions. LE is a dysfunction of this system's due to " \
               "inflammation, and characterized by antegrade amnesia, psychiatric symptoms such as, anxiety, " \
               "depression, personality disorder and hallucinations, as well as seizures . Mostly characterized by " \
               "subacute symptoms, LE particularly locates mesiotemporal region and is most commonly secondary to " \
               "small cell carcinoma of lung. Paraneoplastic cerebellar degeneration (PCD) is characterized by rapid " \
               "cerebellar Purkinje cell death. It is a rapidly progressive disease with acute or subacute onset. The " \
               "diseases diagnosed with clinical signs and symptoms, cerebrospinal fluid (CSF) examination, " \
               "computed tomography (CT), magnetic resonance imaging (MRI), and autoimmune antibody screening; early " \
               "diagnosis and treatment may control the disease. In this study the clinical, laboratory, " \
               "and radiological examinations of 7 patients diagnosed with autoimmune neurological syndrome (5LE, " \
               "2 PCD) were evaluated and reviewed literature."

test_short_5 = "The Internet is quite possibly the most successful set of technological standards for interlinking " \
               "myriad functions in everything from culture to finance., a combination of technological weaknesses, " \
               "minimal regulation, and. As the Internet revolutionized contemporary society, a major form of " \
               "conflict, international terrorism, became bolder, peaking in significance with the September 11, " \
               "2001 attacks on New York and Washington DC. Suddenly, the conveyances of globalization, jetliners, " \
               "were weaponized, beginning a more than two-decade struggle against insurgents and terror groups. A " \
               "homeland security doctrine evolved out of the rubble of the World Trade Center. It was focused on " \
               "protecting critical infrastructure–dams, mass transit, pipelines, among other things–from terror " \
               "attack. Now our concern is the weaponization of cyberspace and the employment of cyberattack to " \
               "damage or degrade critical infrastructure. This paper addresses a rapidly evolving problem, " \
               "the cybersecurity issues produced in the computerization and automation of producing, storing, " \
               "transmitting, and consuming energy. While energy resources frequently have been targeted in wartime, " \
               "geographic distance mattered in conventional conflict. We now live in a world where cyberattacks can " \
               "have kinetic effects and an increasing number of countries are preparing to use them in conventional " \
               "and unconventional conflict. "




# TEST LONG (500 WODS OR MORE)

test_long_6 = "The computer networked system has increasingly become a critical infrastructure in supporting a wide " \
               "range of services in the economy, education, and government sectors. The fact that these sectors are " \
               "facing severe challenges and threats, such as human error, equipment failure, deliberate attacks, " \
               "natural disasters, and economic crisis. From a time perspective, it is impossible to respond to all " \
               "unknown threats in advance. From a space perspective, it is rather difficult to transfer or rebuild " \
               "network infrastructure before or after a disaster occurs. Therefore, the network system should have " \
               "the capability to resist internal or external threats and sustain normal services and tasks, " \
               "rather than providing absolute security. Evoluted from the Latin word “resilio”, “resilience” refers " \
               "to a system’s capability to return to normal condition after challenging or destructive events. This " \
               "broad definition applies to fields as diverse as ecology, materials science, psychology, economics, " \
               "and engineering. A variety of definitions on resilience have been proposed by researchers in multiple " \
               "disciplines. For example, Pregenzer defined resilience as the “measure of a system’s capability to " \
               "absorb continuous and unpredictable change and still maintain its vital functions”. Woods declared " \
               "that resilience is the system’s capability to create foresight, identify risks, and mitigate risks " \
               "before adverse consequences. Haimes defined resilience as “the ability of the system to withstand a " \
               "major disruption within acceptable degradation parameters and to recover with an acceptable cost and " \
               "suitable time”. Defined by the National Academy of Sciences (NAS) as “the ability to plan and prepare " \
               "for, absorb, recover from disasters and more successfully adapt to adverse events”, resilience is " \
               "becoming one of the most widely used attributes in various organizations and governments. There also " \
               "exists discussion in literatures about the confusion between resilience and other system attributes, " \
               "such as robustness, vulnerability, and reliability. Robustness is usually defined as insensitivity to " \
               "uncertain disturbances. Uday and Marais added that the purpose of robustness is to immediately " \
               "minimize performance loss after disturbance; in contrast, resilience allows for some performance loss " \
               "in the hope that performance can be restored over time. Vulnerability focuses on susceptibility to " \
               "known disturbances that can be obtained by both attacker and defender in advance. Reliability refers " \
               "to the system’s capability and its components to accomplish required functions within a specified " \
               "time under stated conditions. Different from the above concepts of system attributes, resilience " \
               "places greater emphasis on the recovery and evolutionary capability to resist unknown future threats. " \
               "There emerges diverse network attacks and threats, and network security defenses are also being " \
               "developed into a proactive defense direction, such as the Moving Target Defense . Therefore, " \
               "it has become an urgent problem to reasonably and effectively evaluate and improve the network " \
               "resilience in various attack and defense scenarios. In general, abundant research on resilience has " \
               "been performed from the following three aspects. Measurement and evaluation research is the first " \
               "step to study network resilience, including failure models, measure indicators, and aggregation " \
               "models. Second, optimized and improved strategies for network resilience are conducted under specific " \
               "network scenario based on entity-related analysis. Third, research based on resilience focuses on " \
               "trade-off between networking performance and resource invested in practical network, " \
               "such as transportation network and power supply network  However, existing researches on network " \
               "resilience lack general measurement methods and standards suitable for different network scenarios. " \
               "And most of them were only used to evaluate network resilience on time-invariant network, " \
               "which cannot reflect the dynamic characteristic of real-world network. In this paper, a quantitative " \
               "framework for network resilience evaluation is established using the Dynamic Bayesian Network based " \
               "on modeling of five core resilient capabilities. The proposed framework is suitable for time-varying " \
               "network and can be used to describe the process of network resilience, including preparation, " \
               "resistance, adaptation, recovery, and evolution. "

test_long_7 = "In many engineering applications, accurate modeling is an essential part in order to design " \
              "appropriate control strategies. However, due to the inevitable nonlinearities and approximation " \
              "assumptions, discrepancies between mathematical and physical models do exist. Therefore, " \
              "classical control techniques are insufficient to achieve the required control objectives. A good " \
              "strategy for dealing with such modeling inaccuracies and achieving the required objectives is to use " \
              "robust control techniques. Therefore, control theory has proved to be effective in many applications, " \
              "which are associated with the maximum gain between the system’s input and output. This gain can " \
              "indicate robustness against uncertainties and nonlinear dynamics. So far, there have been many " \
              "articles that aim to solve the design problem, such as the Algebraic Riccatia Equation (ARE)-based " \
              "approach and the Linear Matrix Inequalities (LMIs)-based approach. With the advancement of " \
              "computational technology and its successful applications, the LMI approach was used to formulate the " \
              "design problem as an optimization problem that can be easily solved using existing interior point " \
              "optimization algorithms. LMIs have been extensively used because convex optimization techniques can be " \
              "used to determine state feedback gain. Available optimization parser like YALMIP can be easily " \
              "utilized to implement the LMI conditions, and effective algorithms can be used to solve them. LMIs can " \
              "also be easily expanded to handle systems with uncertainties. Their formulation is quite general to " \
              "define convex subregions in the complex plane with LMI based conditions . Thus, by imposing additional " \
              "LMI regional constraints on the controller synthesis conditions, the desired response can be easily " \
              "guaranteed since the regional constraints are closely related to time domain specifications. " \
              "Proportional and derivative gain for state-feedback LMI controller in Group SO(3) control law were " \
              "formulated in. In , a fractional order model of HIV/AIDS has been investigated through the fixed point " \
              "theorem, which was used to derive stability criteria and uniqueness of the solution for fractional " \
              "order models. Several researchers have studied various control problems in the optimization framework. " \
              "In this work, synthesis conditions for robust control with multi-objective have been proposed and " \
              "applied to a satellite system. More precisely, with and without regional constraints have been " \
              "considered using the LMI formulation. The proposed controller has also been compared to a reference " \
              "controller designed through the classical pole placement method. Comparison simulations showed " \
              "superior response of the proposed controller over the reference controller. The model of the system is " \
              "a Multi-Input–Multi-Output (MIMO) system where the controlled outputs are the yaw, roll, " \
              "and pitch angles. "

test_long_8 = "When the experiments were performed in the laboratory to solve some engineering problems, then due to " \
              "economic constraints, time, space, energy, etc., the experiments couldn't be performed under an " \
              "identical set of operating conditions which prevails in the real place. So, to save money, time, " \
              "and space, the experiments are performed under an altered set of conditions than what exists. So, " \
              "under these circumstances, two pertinent questions usually arise: how the test results from the " \
              "laboratory experiments can be applied to the actual problem. Secondly, is it possible to limit the " \
              "number of experiments and still get the same results as in the real case. The concept of physical " \
              "similarity gives a clue to answering the above questions. With the idea of physical similarity we can " \
              "apply the test results of altered conditions to the actual problem, provided the physics of the " \
              "problem remains the same. Furthermore, we can club the different dimensional variables influencing a " \
              "performance parameter into a single group because of the principle of physical similarity. The " \
              "influence of all the dimensional variables as operating parameters on the performance parameter is " \
              "affected through that parameter group. If many physical variables define a problem, so if the problem " \
              "has to be made similar to the problem of a different condition, then definitely some dimensionless " \
              "terms have to be fixed for both the problems, which represents the criterion of similarity, " \
              "mainly the dynamic similarity. Now the question comes how to find such nondimensional parameters, " \
              "which are the combination of dimensional variables. The answer to this question lies with dimensional " \
              "analysis and dimensional homogeneity. The first instance of dimensional homogeneity is found in the " \
              "work of Fourier. Lord Rayleigh proposed an indicial method to perform dimensional analysis to obtain a " \
              "nondimensional relationship between dimensional variables. Buckingham's Pi theorem was introduced " \
              "later with the full-fledged procedure to evaluate the nondimensional π terms by Buckingham in 1914. " \
              "This paper has set a benchmark in the dimensional analysis and physical similarity principle. Several " \
              "other methods exist, but how Buckingham's π theorem deals with the dimensional analysis is unique as " \
              "it is more practical and systematic as it uses repeating variables. But the major problem with " \
              "Buckingham's π theorem is that the algebra involved in solving the π terms requires a lot of hand " \
              "calculations, and if the number of variables is more, then the chances of error are more. Here comes " \
              "the importance of computer programs for tedious calculations. Python is a very easy to implement, " \
              "efficient, and user-friendly programming language. A very attractive feature of Python is that one " \
              "does not have to write huge lines of code; instead, very complex problems can be solved by just " \
              "writing a few lines of code. The python modules such as NumPy and SymPy are very efficient in handling " \
              "any type of numerical and symbolic computation. Moreover, symbolically solving simultaneous equations " \
              "and segregating the variables is an easy task with SymPy. Parth et al.have developed Python modules to " \
              "handle complex fluid flow problems in a laminar flow regime. The NumPy contains array objects which " \
              "can simplify the tasks a lot. Several researchers have used Python to solve many mathematically " \
              "complex problems. PyBaMM, a python package, has been developed by Sulzer et al. for the collaboration " \
              "of cross-institutional facilitation. Python has also been used by Marowka  for parallel computation. " \
              "For solving heat transfer problems. This research article presents a novel approach to handling " \
              "Buckingham's Pi theorem. Buckingham's Pi theorem has been modelled with the help of Python, " \
              "and the function developed to address π terms is tested against some real-life problems. It has been " \
              "observed that the computer program has not only automated the task for fluid flow problems but it can " \
              "also be extended to the other branches of physics by slight modifications. The codes and python " \
              "functions are written in the Jupyter notebook as it shows both codes and results in one place. " \
              "Moreover, its cell structure gives a better understanding of the code."

test_long_9 ="The first risk which I have identified within my Risk Register is Phishing by compromised links. " \
             "Phishing by compromised links is a serious threat to workstations which aren’t protected against it " \
             "because it can lead to malicious links being opened which pose as a legitimate website. This can have " \
             "massive repercussions such as Drive by Crypto mining, Malicious Hardware being downloaded, " \
             "and credentials being stolen. Additionally, phishing is more common now than ever with APWG seeing " \
             "Phishing attacks hit a new quarterly record for the total number of phishing attacks for Q2 2022. " \
             "Furthermore, phishing attacks are done through various methods however a popular one is imitating " \
             "legitimate websites such as shopping websites. From a survey taken by openX and HarrisPole they found " \
             "that 81% of millennial workers admitted to doing online shopping. Building on this, . Technicapsule is " \
             "a young firm and many of their employees would most likely fit into the bracket of being a millennial. " \
             "With these findings millennial employees would be massive targets for these types of attacks. Necessary " \
             "controls should be implemented to mitigate these risks. A control that can be implemented which helps " \
             "to mitigate this risk is a technical control which is software based and this is DNS Filtering. The " \
             "first reason why I have chosen DNS Filtering as a control is because it is able to block access to " \
             "malicious websites. This is good for an organisation because it decreases the likelihood of an employee " \
             "accessing a malicious website. Another reason why I have chosen this control is because it deploys a " \
             "network wide generalisation for all the employees meaning the administrators set what can and cannot be " \
             "used while on the network which further protects people within the network and the network itself. " \
             "Additionally, DNS Filtering also helps for organisations comply to standards which are put out by big " \
             "agencies such as NIST (National Institute of Standards and Technology) or UKCCIS (UK Council for " \
             "Children Internet Safety). Furthermore, according to  so with this in mind DNS Filtering is a crucial " \
             "control which should be implemented which can significantly decrease the risk of a Phishing attack. The " \
             "cybersecurity tool which implements this control is ‘Restrict Web-Based Content(M1021)’ and this " \
             "mitigates the potential techniques which may be used through Phishing with compromised links such as " \
             "Drive-by compromise and Spearphishing links. "

test_long_10 = "The above scatterplots do a comparison between the metrics Coupling Between Objects (CBO) and Bugs " \
               "for systems 2 and systems 3. When correlating these two metrics the coefficients were 0.30 for system " \
               "2 and 0.24 for system 3. The coefficient outputs for both systems are quite shocking because one " \
               "would assume that as the coupling of a class increases so would the likelihood of bugs being found " \
               "within that class however for both systems, they show a weak relationship when comparing these 2 " \
               "metrics which is very unusual. Additionally, However, for both systems CBO doesn’t seem to be a " \
               "strong predictor for bugs. The unusual results could be due to both systems being new and to an " \
               "extent they exhibit the anti-pattern of ‘Walking in a minefield’ where errors will be discovered as " \
               "the systems are used more. Additionally, both systems may also have not had much testing done on them " \
               "which would be crucial in highlighting errors. Furthermore, testing on the system may have not been " \
               "very extensive or it may have been done by a novice which would lead to poor test quality. When " \
               "looking purely at the number of bugs for each system, system 2 appears to be the more bug prone " \
               "system compared to system 3. When finding the maximum number of bugs from all the classes within the " \
               "respective systems, system 2 had a maximum of 22 while system 3 had a maximum of only 11. " \
               "Furthermore, the average amount of bugs was significantly lower within system 3 compared to system 2 " \
               "with it only having an average of 0.40 while system 2 had an average of 0.96. Based on these findings " \
               "system 2 appears to be a more complex system when comparing the two due to the increase in bugs " \
               "present within the system. Within both systems there are some strong smells present and given this " \
               "there are some opportunities where refactoring can be done to overall help improve the systems. " \
               "Firstly, a class identified within Figure 4 appears to be a Middleman and have Feature Envy. This " \
               "class has a CBO of 38 and bugs of 11. With the CBO being extremely high for this class it could mean " \
               "that the class is serving as a middleman between different classes which increases coupling. " \
               "Additionally, the class could be also accessing data from a different class which thus makes it " \
               "coupled to that class because it needs the data. To help reduce the coupling this class can be " \
               "removed entirely if it appears to be a Middleman class. Secondly, Move Method Refactoring can also be " \
               "used to help decrease the CBO of this class which would tackle the issue of Feature Envy so that the " \
               "class will only have methods which are relevant to its needs and purpose. Moreover, within Figure 3 " \
               "there is an outlier which has a CBO 223, but it only has 4 bugs. Although refactoring may help reduce " \
               "the coupling of this class it may also cause problems since this class is so highly coupled. For this " \
               "class I don’t think any method for refactoring would help it and when considering how low the number " \
               "of bugs found within this class is then potentially refactoring could do more harm than good. " \
               "However, long term reusability may be impacted. Considerations may also need to be considered since " \
               "this system could have potentially had bad testing done on it which hasn’t uncovered many of the bugs " \
               "that exist within it. "

demo_present_text_abstract = "Another principle we used was Perceptual Organisation of Information. When using " \
                             "this we applied some of Gestalt’s laws which helped us design our prototypes. We also " \
                             "used depth cues. The laws which our group focused on was the Law of Common Region and " \
                             "the Law of Proximity and they helped us to visually organise our work. Firstly, we used " \
                             "the Law of Common Region when designing the buttons for the different payment packages " \
                             "by putting them within their own closed region. We also did this with the description " \
                             "box. The reason we did this is because to the user it will help to show that the " \
                             "elements within the box are related due to the boundary which separates it from " \
                             "other elements on the page. However, using this principle had some caveats such " \
                             "as using it too much can cause clutter on the interface, it also overpowers other" \
                             " laws such as the law of proximity, so we learned to use it sparingly and where it " \
                             "was necessary. Adding on, when designing the buttons for our page we also used depth " \
                             "cues such as Drop shadows. The reason we designed our buttons like this is because " \
                             "it makes them stand out against the background and highlights that they are clickable " \
                             "because they appear to be able to be pressed down. The Law of Proximity was another law " \
                             "which we used when aiming to perceptually group the different genres that are available. " \
                             "Firstly, using this principle helped to guide our design by us placing all the available " \
                             "genres near to each other. The reason we did this is because items which are grouped " \
                             "together appear to be more identifiable as being related to the user and doing this " \
                             "helps to accentuate that these are the related. As a designer you want the user to " \
                             "have a conceptual idea of what things are and their purpose. Grouping several " \
                             "objects together helps form a concept of what things do and their purpose for " \
                             "the user. (Smith- Gratto,K and Fisher, 1999). Kepes presents a similar idea to " \
                             "how we perceive things are being grouped however instead from the standpoint of " \
                             "how we read words saying “We read words as segregated wholes because their letters " \
                             "are closer to one another than are the last and first letter of two words.” (Kepes,2020)."


cluster_test = ["I like cats",
                "I hate cats",
                "My day is going amazing",
                "My day is going very badly but i love cats"
                "What is your favourite day of the week and deos your cat like it?",
                "What time is it today man?",
                "Im not sure if I like cats or not",
                "I will google whether or not cats are good or not",
                "I don't really trust google though my dude",
                "I love travelling its so fun",
                "Fancy fancy food yum",
                "Vagabond Chocolate"]



# print(Nlp_Engine.cluster_descriptions(cluster_test))



start = time.time()
# keywords = Search_Engine.Nlp_Engine1.all_keywords(text2)
keywords = Search_Engine.Nlp_Engine1.keyword_extractor_yake(1, 5, text, 0.9)
# keywords_all = Search_Engine.Nlp_Engine1.all_keywords(text1)
multi_grams = Search_Engine.Nlp_Engine1.multi_gram(text)
top_phrases = Search_Engine.Nlp_Engine1.top_phrases(text)
# test_title_method = Search_Engine.title_query('"CNS"',25,0)
query_generator_test = Search_Engine.query_generator(keywords, multi_grams,text)


print("------Keywords Extracted-------")
print(*keywords,sep="\n")
print("------Top_Phrases-------")
print(top_phrases,sep="\n")
print("------Articles-------")
for document in query_generator_test:
    print(document.title)
# documents_dc = []
# for document in query_generator_test:
#     description = str(document.description)
#     if description == "" or None:
#         continue
#     else:
#         documents_dc.append(description)
#     print(document.authorName)
#
# if len(documents_dc) < 5:
#     print("Nothing Related to your work found or an error occured")
# else:
#     print("----cluster-----")
#     array = Nlp_Engine.cluster_descriptions(documents_dc, text, query_generator_test)
#     for x in array:
#         print(x)







