/* ============================================================
   SYNAPSE — Bibliothèque de contenu (français)
   Cartes d'idées personnalisées pour Marien.
   Chaque carte = un insight condensé, façon Deepstash.
   ============================================================ */

const THEMES = {
  neuro:   { id:'neuro',   nom:'Neuroplasticité', emoji:'🧠', couleur:'#38BDF8', desc:"Reconstruire ton cerveau, créer de nouvelles connexions." },
  trading: { id:'trading', nom:'Trading & marché', emoji:'📈', couleur:'#D4AF37', desc:"Devenir un trader stable et redoutable." },
  mental:  { id:'mental',  nom:'Mental & discipline', emoji:'🎯', couleur:'#EF6B6B', desc:"Forger un mental d'acier, dompter tes émotions." },
  physique:{ id:'physique',nom:'Physique & énergie', emoji:'💪', couleur:'#4ADE80', desc:"Un corps fort pour un cerveau fort." },
  appren:  { id:'appren',  nom:'Apprentissage & mémoire', emoji:'📚', couleur:'#A78BFA', desc:"Apprendre vite, retenir pour toujours." },
  reflex:  { id:'reflex',  nom:'Réflexion & décision', emoji:'🔍', couleur:'#60A5FA', desc:"Penser clair, décider juste." },
};

const CARTES = [
  /* ---------------- NEUROPLASTICITÉ ---------------- */
  { id:'n1', theme:'neuro', titre:"Ton cerveau se recâble à chaque instant",
    corps:"La neuroplasticité, c'est la capacité de ton cerveau à créer et renforcer de nouvelles connexions toute la vie — même après une lésion. Chaque chose que tu apprends trace un nouveau chemin neuronal. Ton cerveau n'est pas figé : il se reconstruit. Ce que tu répètes, il le grave.",
    source:"Neurosciences — plasticité cérébrale", auteur:"Fondation pour la Recherche sur le Cerveau" },
  { id:'n2', theme:'neuro', titre:"« Les neurones qui s'activent ensemble se lient ensemble »",
    corps:"C'est la loi de Hebb, le principe fondateur de l'apprentissage. Quand deux neurones s'activent en même temps, la connexion entre eux se renforce. Traduction : plus tu répètes une action ou une idée, plus le circuit devient solide et automatique. La répétition n'est pas ennuyeuse — c'est de la construction.",
    source:"Loi de Hebb (1949)", auteur:"Donald Hebb" },
  { id:'n3', theme:'neuro', titre:"Après une lésion, le cerveau se réorganise",
    corps:"Quand une zone est touchée, les zones voisines peuvent reprendre une partie du travail. De nouvelles routes se créent pour contourner les circuits abîmés. La récupération dépend beaucoup de la stimulation : plus tu sollicites ton cerveau avec des tâches variées, plus tu l'aides à se réparer. L'inaction, elle, laisse les connexions s'éteindre.",
    source:"Récupération après lésion cérébrale", auteur:"Neurosciences cliniques" },
  { id:'n4', theme:'neuro', titre:"Utilise-le ou perds-le",
    corps:"Les connexions neuronales sollicitées se renforcent ; celles qu'on n'utilise plus s'affaiblissent et disparaissent (c'est l'élagage synaptique). Ton cerveau est un jardin : ce que tu arroses pousse, ce que tu ignores fane. Chaque jour de stimulation compte. Chaque jour d'apprentissage protège et développe ton réseau.",
    source:"Élagage synaptique", auteur:"Neurosciences du développement" },
  { id:'n5', theme:'neuro', titre:"La nouveauté fait pousser ton cerveau",
    corps:"Apprendre quelque chose de nouveau et de difficile déclenche la libération de facteurs de croissance qui aident les neurones à se connecter. Le confort n'entraîne aucune plasticité. La difficulté, si. Cherche un peu d'inconfort chaque jour : une idée nouvelle, un geste nouveau, un problème que tu n'avais jamais résolu.",
    source:"Plasticité et apprentissage actif", auteur:"Neurosciences cognitives" },
  { id:'n6', theme:'neuro', titre:"Le sommeil grave tes progrès",
    corps:"Pendant que tu dors, ton cerveau rejoue et consolide ce que tu as appris dans la journée. Les connexions utiles sont renforcées, les inutiles nettoyées. Sans sommeil de qualité, tes efforts d'apprentissage s'effacent. Dormir n'est pas une perte de temps : c'est la moitié du travail de mémorisation.",
    source:"Consolidation mnésique", auteur:"Recherche sur le sommeil" },
  { id:'n7', theme:'neuro', titre:"Bouger nourrit tes neurones",
    corps:"L'exercice physique augmente le BDNF, une protéine qui agit comme un engrais pour le cerveau : elle favorise la naissance de nouveaux neurones et de nouvelles connexions, surtout dans l'hippocampe (la mémoire). 30 minutes de marche ou de sport, et ton cerveau devient littéralement plus apte à apprendre.",
    source:"BDNF & exercice", auteur:"Neurosciences de l'activité physique" },
  { id:'n8', theme:'neuro', titre:"La visualisation active les mêmes circuits que l'action",
    corps:"Imaginer précisément un geste active presque les mêmes réseaux neuronaux que l'exécuter réellement. C'est pour ça que les athlètes et les rééducateurs utilisent la visualisation : elle entretient et reconstruit les circuits même quand le corps ne peut pas encore agir. Visualise ce que tu veux devenir — ton cerveau commence déjà à le câbler.",
    source:"Imagerie motrice", auteur:"Neurosciences du mouvement" },

  /* ---------------- TRADING ---------------- */
  { id:'t1', theme:'trading', titre:"Le meilleur perdant gagne",
    corps:"Les meilleurs traders ne devinent pas mieux le marché. Ils perdent mieux : petit, vite, sans ego. La différence entre celui qui explose son compte et celui qui dure, ce n'est pas la qualité des entrées — c'est la gestion des pertes. Accepte de perdre proprement, et tu survivras assez longtemps pour gagner.",
    source:"Best Loser Wins", auteur:"Tom Hougaard" },
  { id:'t2', theme:'trading', titre:"80 % des traders retail perdent",
    corps:"Les chiffres publics des brokers européens sont brutaux : la grande majorité des particuliers perdent de l'argent. Ce n'est pas un hasard, c'est structurel — manque de discipline, sur-trading, gestion du risque absente. Ta mission n'est pas de rejoindre le troupeau, mais de faire exactement l'inverse de ce que fait la masse qui perd.",
    source:"Rapports AMF / ESMA", auteur:"Régulateurs européens" },
  { id:'t3', theme:'trading', titre:"Le stop-loss n'est pas une option",
    corps:"Décaler un stop-loss est l'acte le plus autodestructeur du trader. Une petite perte planifiée devient une catastrophe non planifiée. Ton stop est un contrat que tu signes avant d'entrer, quand ton cerveau est encore calme. Le respecter n'est pas une faiblesse : c'est la preuve que tu es un professionnel et pas un joueur.",
    source:"Gestion du risque", auteur:"Devenir un trader stable" },
  { id:'t4', theme:'trading', titre:"Risque 1 %, dure 100 trades",
    corps:"Si tu risques 1 % par trade, il te faudrait une série de pertes quasi impossible pour te ruiner. Si tu risques 10 %, dix pertes d'affilée — banales sur une série — et c'est fini. La survie précède le profit. Protège ton capital comme un sniper protège ses dernières balles : chaque trade doit être petit face à ton compte total.",
    source:"Money management", auteur:"Devenir un trader stable" },
  { id:'t5', theme:'trading', titre:"À +1500, ton cortex préfrontal s'éteint",
    corps:"Quand un trade gagne gros, la dopamine inonde ton cerveau et le cortex préfrontal — le siège de la décision rationnelle — se met en retrait. Tu deviens passager de tes émotions. C'est là qu'on rend tout : par euphorie. La parade : décider AVANT d'entrer où tu sors, et exécuter comme un robot quand l'émotion monte.",
    source:"Neurofinance", auteur:"Devenir un trader stable" },
  { id:'t6', theme:'trading', titre:"Perdre fait deux fois plus mal que gagner",
    corps:"Kahneman l'a prouvé : l'aversion à la perte fait qu'une perte de 100 € nous blesse deux fois plus qu'un gain de 100 € nous réjouit. C'est pour ça qu'on coupe les gagnants trop tôt et qu'on laisse courir les perdants. Connaître ce biais, c'est déjà commencer à le neutraliser : agis contre ton instinct, pas avec lui.",
    source:"Système 1 / Système 2", auteur:"Daniel Kahneman" },
  { id:'t7', theme:'trading', titre:"Un plan écrit vaut mille bonnes intentions",
    corps:"« Je verrai en direct » est la phrase des perdants. Le marché en direct, c'est de l'émotion pure. Ton edge, c'est un plan écrit : point d'entrée, stop, objectif, taille de position — décidés à froid. Le trade ne fait qu'exécuter une décision déjà prise. Pas de plan = pas de trade.",
    source:"Processus de trading", auteur:"Devenir un trader stable" },
  { id:'t8', theme:'trading', titre:"Tiens un journal de trading",
    corps:"Ce qui n'est pas mesuré ne s'améliore pas. Note chaque trade : le setup, ton émotion, si tu as respecté ton plan. En relisant, tu verras tes vrais schémas — pas ceux que tu imagines. Le journal transforme l'expérience en compétence. Sans lui, tu répètes les mêmes erreurs en croyant progresser.",
    source:"Amélioration continue", auteur:"Devenir un trader stable" },

  /* ---------------- MENTAL ---------------- */
  { id:'m1', theme:'mental', titre:"La discipline pèse des grammes, le regret pèse des tonnes",
    corps:"Chaque acte de discipline coûte un petit effort sur le moment. Chaque renoncement coûte un lourd regret plus tard. Choisis ta douleur : la petite, maintenant, qui construit — ou la grande, plus tard, qui détruit. Les monstres dans leur domaine ont juste appris à préférer la première.",
    source:"Discipline vs regret", auteur:"Jim Rohn (adapté)" },
  { id:'m2', theme:'mental', titre:"Tu ne montes pas au niveau de tes objectifs, tu tombes au niveau de tes systèmes",
    corps:"La motivation est un feu de paille. Ce qui te porte, ce sont tes routines : ce que tu fais automatiquement, sans négocier avec toi-même. Ne vise pas à être motivé chaque jour — construis des systèmes qui te font avancer même les jours sans envie. Le système bat la volonté.",
    source:"Atomic Habits", auteur:"James Clear" },
  { id:'m3', theme:'mental', titre:"Deviens 1 % meilleur chaque jour",
    corps:"1 % par jour, ça paraît ridicule. Mais sur un an, ça te rend environ 37 fois meilleur. Les résultats spectaculaires ne viennent pas d'un exploit unique, mais de l'accumulation de petits progrès invisibles. Ne cherche pas la transformation d'un coup. Cherche le petit progrès d'aujourd'hui, répété.",
    source:"Effet cumulé", auteur:"James Clear" },
  { id:'m4', theme:'mental', titre:"Entre le stimulus et la réaction, il y a un espace",
    corps:"Un événement te frappe — une perte, une insulte, un échec. Ton pouvoir est dans la fraction de seconde avant ta réaction. Les faibles réagissent automatiquement. Les forts utilisent cet espace pour choisir leur réponse. S'entraîner à faire une pause avant d'agir, c'est s'entraîner à la liberté.",
    source:"Logothérapie", auteur:"Viktor Frankl" },
  { id:'m5', theme:'mental', titre:"Concentre-toi sur ce que tu contrôles",
    corps:"Les stoïciens divisaient le monde en deux : ce qui dépend de toi (tes actes, ton effort, ton attitude) et ce qui n'en dépend pas (le résultat, l'avis des autres, le marché). Toute ton énergie doit aller dans la première colonne. Lâcher le reste, ce n'est pas abandonner — c'est arrêter de gaspiller ta force.",
    source:"Stoïcisme", auteur:"Épictète" },
  { id:'m6', theme:'mental', titre:"La constance bat l'intensité",
    corps:"Un effort énorme un jour, puis rien pendant deux semaines, ne construit rien. Un effort modéré tous les jours construit un empire. Ton cerveau et ton corps répondent à la régularité, pas aux coups d'éclat. Sois la goutte d'eau qui perce la pierre, pas la vague qui frappe une fois et se retire.",
    source:"Régularité", auteur:"Principe d'entraînement" },
  { id:'m7', theme:'mental', titre:"Nomme l'émotion pour la désamorcer",
    corps:"Quand tu mets un mot précis sur ce que tu ressens — « je suis en colère », « j'ai peur de perdre » — l'activité de l'amygdale baisse et ton cerveau rationnel reprend la main. C'est prouvé par imagerie cérébrale. Ne refoule pas tes émotions, nomme-les. Ce qui est nommé peut être dompté.",
    source:"« Name it to tame it »", auteur:"Dan Siegel" },
  { id:'m8', theme:'mental', titre:"Change d'identité, pas juste d'objectif",
    corps:"« Je veux arrêter de sur-trader » est un objectif fragile. « Je suis quelqu'un de discipliné » est une identité qui décide pour toi. Les habitudes durables ne viennent pas de ce que tu veux obtenir, mais de qui tu décides d'être. Chaque action est un vote pour la personne que tu deviens. Demande-toi à chaque choix : « qu'est-ce que ferait le trader que je veux devenir ? »",
    source:"Identity-based habits", auteur:"James Clear" },
  { id:'m9', theme:'mental', titre:"Tu deviens ce que tu répètes",
    corps:"Tu n'es pas ton passé ni ton accident. Tu es la somme de ce que tu fais chaque jour. Reconstruire une identité, c'est empiler des preuves : chaque trade discipliné, chaque carte apprise, chaque séance de sport est une brique. Au début tu joues un rôle ; à force de répétition, le rôle devient toi. La nouvelle personne se fabrique geste après geste.",
    source:"Construction de l'identité", auteur:"Psychologie du comportement" },
  { id:'m10', theme:'mental', titre:"Affronte ton défaut principal en face",
    corps:"On progresse le plus vite en travaillant précisément là où ça fait mal : ton plus gros défaut. L'ignorer le laisse grandir ; le regarder en face le réduit. Identifie le point faible qui te coûte le plus (l'impatience ? l'ego ? la peur ?) et fais-en ton chantier n°1. Ta plus grande faiblesse d'aujourd'hui peut devenir ta plus grande force.",
    source:"Croissance ciblée", auteur:"Développement personnel" },

  /* ---------------- PHYSIQUE ---------------- */
  { id:'p1', theme:'physique', titre:"Un cerveau fort a besoin d'un corps entraîné",
    corps:"Ton cerveau consomme environ 20 % de ton énergie. Sa performance dépend directement de ton corps : circulation, oxygénation, sommeil, nutrition. Négliger le physique, c'est saboter le mental. Le sport n'est pas séparé de la réflexion — c'en est le carburant.",
    source:"Corps-cerveau", auteur:"Physiologie" },
  { id:'p2', theme:'physique', titre:"L'exercice est ton meilleur antidépresseur naturel",
    corps:"Bouger libère des endorphines, de la dopamine et régule le cortisol (l'hormone du stress). 20 à 30 minutes d'activité suffisent à changer ton humeur et ta clarté mentale pour des heures. Quand la tête tourne mal, la solution est souvent dans les jambes : marche, cours, soulève.",
    source:"Exercice & humeur", auteur:"Médecine du sport" },
  { id:'p3', theme:'physique', titre:"Le sommeil est ta performance n°1",
    corps:"Manquer de sommeil dégrade la mémoire, le jugement, le contrôle émotionnel et la prise de risque — exactement les qualités d'un bon trader et d'un cerveau en reconstruction. Dormir 7 à 9 h n'est pas paresseux, c'est stratégique. Le sommeil est le socle sur lequel tout le reste tient.",
    source:"Why We Sleep", auteur:"Matthew Walker" },
  { id:'p4', theme:'physique', titre:"L'hydratation, c'est de la lucidité",
    corps:"Même une légère déshydratation (1 à 2 %) réduit la concentration, la mémoire de travail et l'humeur. Ton cerveau est composé à environ 75 % d'eau. Avant de chercher un café ou une excuse à ta fatigue mentale, bois un grand verre d'eau. Simple, gratuit, immédiat.",
    source:"Hydratation & cognition", auteur:"Neurophysiologie" },
  { id:'p5', theme:'physique', titre:"La respiration lente calme ton système nerveux",
    corps:"Ralentir ta respiration — inspiration 4 s, expiration 6 s — active le nerf vague et bascule ton corps en mode « repos ». En 90 secondes, ton rythme cardiaque baisse et ton cerveau redevient clair. C'est ton bouton d'urgence anti-panique : avant un trade, un examen, une décision importante.",
    source:"Cohérence cardiaque", auteur:"Physiologie du stress" },
  { id:'p6', theme:'physique', titre:"La lumière du matin règle ton horloge",
    corps:"Voir la lumière du jour dans l'heure qui suit ton réveil cale ton horloge biologique : meilleure énergie le jour, meilleur sommeil la nuit. 10 minutes dehors le matin valent mieux que trois cafés. Ton cerveau a besoin de savoir qu'il fait jour pour donner le meilleur de lui-même.",
    source:"Rythme circadien", auteur:"Neurosciences du sommeil" },

  /* ---------------- APPRENTISSAGE ---------------- */
  { id:'a1', theme:'appren', titre:"La répétition espacée grave dans le marbre",
    corps:"Réviser une information juste avant de l'oublier la renforce bien plus que la relire dix fois d'affilée. En espaçant tes révisions dans le temps, tu obliges ton cerveau à reconstruire le souvenir — et il devient plus solide à chaque fois. C'est le principe même de cette app : elle te fait revoir au bon moment.",
    source:"Courbe de l'oubli", auteur:"Hermann Ebbinghaus" },
  { id:'a2', theme:'appren', titre:"Se tester bat relire",
    corps:"Relire ses notes donne l'illusion de savoir. Se tester (récupérer l'info de mémoire, sans regarder) crée l'apprentissage réel. L'effort de rappel renforce la trace neuronale. Ferme le livre et demande-toi : « qu'est-ce que je viens d'apprendre ? » Cette petite gêne, c'est le son de ton cerveau qui grave.",
    source:"Testing effect", auteur:"Sciences cognitives" },
  { id:'a3', theme:'appren', titre:"Explique-le simplement, ou tu ne l'as pas compris",
    corps:"La technique Feynman : pour vérifier que tu maîtrises une idée, explique-la comme à un enfant, sans jargon. Là où tu bloques, c'est là que ta compréhension est trouée. Enseigner — même à un mur — est l'une des façons les plus puissantes d'apprendre et de consolider.",
    source:"Technique Feynman", auteur:"Richard Feynman" },
  { id:'a4', theme:'appren', titre:"Mélange tes sujets pour mieux apprendre",
    corps:"Travailler un seul type de problème en bloc semble efficace mais s'oublie vite. Alterner plusieurs sujets ou compétences (l'entrelacement) est plus dur sur le moment mais grave bien plus profond. La difficulté que tu ressens n'est pas un échec : c'est le signe que l'apprentissage se fait.",
    source:"Interleaving", auteur:"Sciences de l'apprentissage" },
  { id:'a5', theme:'appren', titre:"Les difficultés désirables",
    corps:"Ce qui rend l'apprentissage plus dur sur le moment — se tester, espacer, mélanger — le rend plus durable. À l'inverse, ce qui semble facile et fluide s'évapore. Ne fuis pas l'effort mental : c'est exactement lui qui construit les connexions solides. Le confort d'apprentissage est un piège.",
    source:"Desirable difficulties", auteur:"Robert Bjork" },
  { id:'a6', theme:'appren', titre:"5 minutes par jour battent 5 heures le dimanche",
    corps:"Un petit contact quotidien avec un sujet crée une progression que les longues sessions rares ne donnent jamais. La régularité entretient les circuits, empêche l'oubli et transforme l'apprentissage en habitude. C'est toute la logique de cette app : un peu, mais tous les jours, sans exception.",
    source:"Micro-apprentissage", auteur:"Sciences cognitives" },

  /* ---------------- RÉFLEXION ---------------- */
  { id:'r1', theme:'reflex', titre:"Système 1 rapide, Système 2 lent",
    corps:"Ton cerveau a deux vitesses : le Système 1, intuitif et immédiat (utile mais plein de biais), et le Système 2, lent et rationnel (fiable mais paresseux). Les grosses décisions — argent, vie, trading — méritent le Système 2. Apprends à reconnaître quand ton intuition te mène, et à imposer une pause réfléchie.",
    source:"Thinking, Fast and Slow", auteur:"Daniel Kahneman" },
  { id:'r2', theme:'reflex', titre:"Inverse le problème",
    corps:"Au lieu de te demander « comment réussir ? », demande « qu'est-ce qui me ferait échouer à coup sûr ? » puis évite-le. Cette inversion, chère à Charlie Munger, révèle des pièges qu'on ne voit pas de face. Souvent, éviter la bêtise rapporte plus que chercher le génie.",
    source:"Inversion", auteur:"Charlie Munger" },
  { id:'r3', theme:'reflex', titre:"Méfie-toi du biais de confirmation",
    corps:"Ton cerveau cherche naturellement ce qui confirme ce qu'il croit déjà, et ignore le reste. En trading, ça te fait voir sur le graphique ce que tu veux voir. Le remède : cherche activement les preuves que tu as tort. La question puissante n'est pas « ai-je raison ? » mais « et si je me trompais ? »",
    source:"Biais de confirmation", auteur:"Psychologie cognitive" },
  { id:'r4', theme:'reflex', titre:"Pense en probabilités, pas en certitudes",
    corps:"Le débutant veut avoir raison. Le pro pense en pourcentages : « ce setup gagne 6 fois sur 10 ». Un bon trade peut perdre, un mauvais trade peut gagner — sur un coup. Ce qui compte, c'est la qualité de la décision sur des centaines de coups. Détache-toi du résultat unique, juge le processus.",
    source:"Thinking in Bets", auteur:"Annie Duke" },
  { id:'r5', theme:'reflex', titre:"Le coût irrécupérable est un piège",
    corps:"« J'ai déjà tellement investi, je ne peux pas arrêter maintenant. » Erreur. Ce qui est dépensé est dépensé — argent, temps, position perdante. La seule question valable : à partir de maintenant, quelle est la meilleure décision ? Ne laisse pas ton passé décider de ton avenir.",
    source:"Sunk cost fallacy", auteur:"Économie comportementale" },
  { id:'r6', theme:'reflex', titre:"Ralentis pour aller plus vite",
    corps:"Les décisions prises dans la précipitation coûtent des heures à réparer. Prendre 30 secondes pour respirer et clarifier ton intention avant d'agir améliore radicalement la qualité de tes choix. Dans un monde qui pousse à réagir vite, la capacité à faire une pause devient un super-pouvoir.",
    source:"Décision réfléchie", auteur:"Sagesse pratique" },

  /* ---------------- AJOUTS ---------------- */
  { id:'n9', theme:'neuro', titre:"La dopamine grave ce qui compte",
    corps:"La dopamine n'est pas que le plaisir : c'est le marqueur qui dit à ton cerveau « ça, c'est important, garde-le ». Quand tu ressens une petite victoire — comprendre une idée, réussir un trade propre — ce pic de dopamine renforce le circuit. Célèbre tes micro-réussites : tu programmes ton cerveau à vouloir recommencer.",
    source:"Système de récompense", auteur:"Neurosciences" },
  { id:'n10', theme:'neuro', titre:"Sans attention, pas de plasticité",
    corps:"Ton cerveau ne se recâble que sur ce à quoi tu prêtes vraiment attention. Faire dix choses à la fois n'entraîne rien. Une concentration pleine sur une seule tâche ouvre la porte du changement neuronal. La concentration n'est pas un détail : c'est la condition même de l'apprentissage. Coupe les distractions, et ton cerveau se transforme.",
    source:"Focus & neuroplasticité", auteur:"Andrew Huberman" },
  { id:'n11', theme:'neuro', titre:"L'erreur ouvre la porte du cerveau",
    corps:"Se tromper libère des signaux (dopamine, acétylcholine) qui indiquent au cerveau : « quelque chose ne colle pas, adapte-toi ». C'est juste après une erreur que la plasticité est maximale — si tu restes et corriges. Ne fuis pas tes erreurs : c'est exactement le moment où ton cerveau est le plus prêt à apprendre.",
    source:"Apprentissage par l'erreur", auteur:"Neurosciences" },
  { id:'n12', theme:'neuro', titre:"La méditation muscle ton attention",
    corps:"Quelques minutes par jour à ramener ton attention sur ta respiration renforcent le cortex préfrontal (décision, contrôle de soi) et calment l'amygdale (peur, impulsivité). C'est un entraînement direct des zones qui te servent en trading et dans la vie. Méditer, c'est de la musculation pour ton self-control.",
    source:"Méditation & cerveau", auteur:"Neurosciences contemplatives" },

  { id:'t9', theme:'trading', titre:"Coupe court aux pertes, laisse courir les gains",
    corps:"La règle qui sépare les gagnants des perdants tient en une phrase. La plupart font l'inverse : ils encaissent vite un petit gain (peur de le perdre) et laissent grossir une perte (espoir qu'elle revienne). Fais le contraire de ton instinct : petite perte assumée, gain qu'on laisse respirer. C'est contre-nature, et c'est tout le métier.",
    source:"Règle d'or", auteur:"Devenir un trader stable" },
  { id:'t10', theme:'trading', titre:"Le marché ne te doit rien",
    corps:"Le marché n'a pas de mémoire de ton dernier trade, ne sait pas que tu as besoin d'argent, ne te récompensera pas pour ton effort. Il est neutre. Attendre une « revanche » ou une « justice » du marché, c'est le début de la ruine. Ton seul avantage : un processus à espérance positive, répété avec discipline.",
    source:"Réalité du marché", auteur:"Devenir un trader stable" },
  { id:'t11', theme:'trading', titre:"Ne rien faire est une position",
    corps:"L'envie de « trader pour trader » a ruiné plus de comptes que les mauvaises analyses. Attendre le bon setup, mains sur les genoux, est une compétence rare et rentable. Le marché est ouvert des milliers d'heures ; ton edge n'apparaît que quelques-unes. La patience n'est pas de l'inaction : c'est de la précision.",
    source:"Sur-trading", auteur:"Devenir un trader stable" },
  { id:'t12', theme:'trading', titre:"Juge le processus, pas le résultat",
    corps:"Un trade peut être parfaitement exécuté et perdre ; mal exécuté et gagner. Sur un coup, le hasard décide. Sur mille coups, c'est ton processus qui décide. Arrête de noter tes trades sur « gagné / perdu » et note-les sur « ai-je respecté mon plan ? ». Répète le bon process, et les résultats suivent.",
    source:"Variance & discipline", auteur:"Annie Duke (adapté)" },

  { id:'m11', theme:'mental', titre:"La règle des 2 minutes",
    corps:"Pour vaincre la procrastination, réduis l'action à sa version de 2 minutes : « ouvrir mon graphique », « mettre mes baskets », « lire une carte ». Une fois lancé, le plus dur est fait — le mouvement appelle le mouvement. Ne vise pas la séance parfaite : vise juste à commencer. Le démarrage est 90 % de la bataille.",
    source:"Atomic Habits", auteur:"James Clear" },
  { id:'m12', theme:'mental', titre:"La discipline, c'est la liberté",
    corps:"Ça semble paradoxal : se donner des règles strictes rend libre. La discipline te libère de tes impulsions, de tes humeurs, du chaos. Celui qui n'obéit à aucune règle est esclave de chaque envie. Choisis tes disciplines, et tu choisis ta liberté. Le relâchement, lui, finit toujours en prison de regrets.",
    source:"Discipline Equals Freedom", auteur:"Jocko Willink" },
  { id:'m13', theme:'mental', titre:"Compare-toi à toi d'hier",
    corps:"Te comparer aux autres, c'est courir une course truquée : tu ne vois que leurs sommets, jamais leurs galères. Le seul adversaire utile, c'est toi d'hier. Un peu mieux qu'hier, chaque jour : c'est mesurable, c'est motivant, et ça t'appartient. La vraie compétition est intérieure.",
    source:"Progrès personnel", auteur:"Jordan Peterson (adapté)" },

  { id:'p7', theme:'physique', titre:"Tiens-toi droit, ton cerveau suit",
    corps:"La posture ne fait pas que refléter ton état mental — elle l'influence. Se redresser augmente le sentiment de confiance et d'énergie, se tasser nourrit le doute. Avant un trade ou une décision, redresse-toi, épaules en arrière, respire. Ton corps envoie un signal de calme et de contrôle à ton cerveau.",
    source:"Cognition incarnée", auteur:"Psychologie" },
  { id:'p8', theme:'physique', titre:"Ta glycémie pilote ta lucidité",
    corps:"Des pics et chutes de sucre dans le sang déstabilisent ton humeur, ta concentration et ton self-control — mauvais pour décider. Des repas stables (protéines, fibres, bons gras), moins de sucres rapides, et ton cerveau garde un carburant régulier. On ne trade pas bien le ventre en montagnes russes.",
    source:"Nutrition & cognition", auteur:"Physiologie" },
  { id:'p9', theme:'physique', titre:"Marche pour débloquer tes idées",
    corps:"Marcher, surtout dehors, augmente nettement la créativité et aide à résoudre les problèmes sur lesquels tu bloques. Le mouvement doux met le cerveau dans un mode associatif où les idées se relient. Coincé sur une décision ? Ne force pas devant l'écran : lève-toi et marche 10 minutes. La solution vient souvent en chemin.",
    source:"Marche & créativité", auteur:"Étude Stanford" },

  { id:'a7', theme:'appren', titre:"Apprends, puis dors",
    corps:"Le meilleur moment pour dormir, c'est après avoir appris quelque chose d'important : le sommeil transfère l'info de la mémoire fragile vers la mémoire durable. Réviser une carte le soir, puis dormir, ancre bien mieux que réviser puis rester debout des heures. Fais du sommeil le dernier geste de ton apprentissage.",
    source:"Sommeil & mémoire", auteur:"Neurosciences du sommeil" },
  { id:'a8', theme:'appren', titre:"Enseigner, c'est apprendre deux fois",
    corps:"Quand tu expliques une idée à quelqu'un, tu es obligé de l'organiser, de la simplifier, de combler tes trous. C'est l'un des moyens les plus puissants d'ancrer un savoir. Prends l'habitude, après chaque carte, de la reformuler à voix haute comme si tu l'enseignais. Ce que tu peux transmettre, tu le possèdes vraiment.",
    source:"Effet protégé (learning by teaching)", auteur:"Sciences de l'apprentissage" },
  { id:'a9', theme:'appren', titre:"Regroupe pour mémoriser (chunking)",
    corps:"Ta mémoire de travail ne tient que ~4 éléments à la fois. L'astuce des experts : regrouper l'info en « paquets » qui font sens (un numéro de téléphone en blocs, un setup de trading en une seule image mentale). En reliant le nouveau à ce que tu sais déjà, tu transformes plein de détails en une seule idée solide.",
    source:"Chunking", auteur:"Sciences cognitives" },

  { id:'r7', theme:'reflex', titre:"L'explication la plus simple d'abord",
    corps:"Le rasoir d'Occam : face à plusieurs explications, la plus simple est souvent la bonne. En trading comme dans la vie, on invente des scénarios compliqués pour justifier ce qu'on veut croire. Reviens au plus simple : que disent les faits, sans histoire ? La complexité est souvent le déguisement d'un biais.",
    source:"Rasoir d'Occam", auteur:"Guillaume d'Ockham" },
  { id:'r8', theme:'reflex', titre:"Fais un pré-mortem",
    corps:"Avant une décision importante, imagine qu'on est dans six mois et que ça a échoué. Demande-toi : « qu'est-ce qui a mal tourné ? » Cet exercice révèle les risques que l'optimisme te cache. En trading : « si ce trade tourne mal, ce sera à cause de quoi ? » Tu prépares ta défense avant l'attaque.",
    source:"Pre-mortem", auteur:"Gary Klein" },
  { id:'r9', theme:'reflex', titre:"La carte n'est pas le territoire",
    corps:"Ton idée de la réalité n'est pas la réalité — c'est une carte, forcément simplifiée et parfois fausse. Le graphique n'est pas le marché ; ton plan n'est pas l'avenir. Reste humble face à tes modèles : garde-les tant qu'ils marchent, jette-les quand la réalité les contredit. Confondre la carte et le terrain, c'est foncer dans le mur avec confiance.",
    source:"Sémantique générale", auteur:"Alfred Korzybski" },
];

/* Niveaux de progression — de novice à monstre */
const NIVEAUX = [
  { seuil:0,    nom:"Étincelle",     emoji:"✨" },
  { seuil:50,   nom:"Apprenti",      emoji:"🌱" },
  { seuil:150,  nom:"Disciplié",     emoji:"🔥" },
  { seuil:350,  nom:"Combattant",    emoji:"⚔️" },
  { seuil:700,  nom:"Stratège",      emoji:"🧠" },
  { seuil:1200, nom:"Redoutable",    emoji:"⚡" },
  { seuil:2000, nom:"Monstre",       emoji:"👑" },
];

/* Citations d'accueil rotatives */
const CITATIONS = [
  "« Ton cerveau se reconstruit à chaque idée que tu graves. »",
  "« Un peu, mais tous les jours. C'est comme ça qu'on devient un monstre. »",
  "« Les neurones qui s'activent ensemble se lient ensemble. »",
  "« La discipline pèse des grammes, le regret pèse des tonnes. »",
  "« Le meilleur perdant gagne. »",
  "« 1 % par jour = 37 fois meilleur en un an. »",
];

/* ============================================================
   ILLUSTRATIONS — une image par idée (mémoire visuelle)
   Icônes trait épuré (viewBox 0 0 100 100), colorées au thème.
   ============================================================ */
const ICONS = {
  brain:'<path d="M42 28a13 13 0 0 0 0 44"/><path d="M58 28a13 13 0 0 1 0 44"/><path d="M42 28a11 11 0 0 1 16 0"/><path d="M42 72a11 11 0 0 0 16 0"/><path d="M50 30v40"/>',
  synapse:'<circle cx="30" cy="42" r="8"/><circle cx="70" cy="60" r="8"/><path d="M37 47l26 9"/><path d="M50 34v-8M50 66v8M62 44l6-5M38 62l-6 5"/>',
  reroute:'<circle cx="24" cy="50" r="6"/><circle cx="76" cy="50" r="6"/><path d="M40 46l20 0M42 42l-6-6 6 6-6 6" opacity="0"/><path d="M30 50h6"/><path d="M64 50h6"/><path d="M42 50c0-14 16-14 16 0"/><path d="M40 44l4 6-6 2"/><path d="M46 34l6 4-2 6" fill="none"/><path d="M60 42l4-8 6 4"/>',
  prune:'<path d="M50 78V36"/><path d="M50 50l-14-10M50 58l14-10"/><circle cx="34" cy="38" r="4"/><circle cx="66" cy="46" r="4"/><path d="M40 26l8 8M60 26l-8 8" opacity=".55"/>',
  spark:'<path d="M50 22v18M50 60v18M22 50h18M60 50h18M32 32l12 12M56 56l12 12M68 32L56 44M44 56 32 68"/><circle cx="50" cy="50" r="5" fill="currentColor" stroke="none"/>',
  moon:'<path d="M62 30a24 24 0 1 0 0 40 19 19 0 0 1 0-40z"/><path d="M40 32l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" fill="currentColor" stroke="none"/>',
  run:'<circle cx="60" cy="24" r="6"/><path d="M60 34l-10 12 8 8-4 18"/><path d="M50 46l-14 4M58 54l14 6M50 62l-12 12"/>',
  eye:'<path d="M20 50s12-18 30-18 30 18 30 18-12 18-30 18S20 50 20 50z"/><circle cx="50" cy="50" r="8"/>',
  target:'<circle cx="50" cy="50" r="26"/><circle cx="50" cy="50" r="15"/><circle cx="50" cy="50" r="4" fill="currentColor" stroke="none"/>',
  meditate:'<circle cx="50" cy="30" r="8"/><path d="M50 40v14"/><path d="M50 54c-14 0-22 8-24 20h48c-2-12-10-20-24-20z"/><path d="M30 62l-6 6M70 62l6 6"/>',
  chart:'<path d="M22 78V22M22 78h56"/><path d="M34 66v-10M34 46h8v20h-8zM34 46v-6M42 66v6"/><path d="M56 66v-22M56 32h8v34h-8zM56 32v-4M64 66v4"/><path d="M30 60l24-20 18 8"/>',
  shield:'<path d="M50 20l24 8v18c0 18-12 28-24 34-12-6-24-16-24-34V28z"/><path d="M40 48l7 8 14-16"/>',
  balance:'<path d="M50 22v56M30 78h40"/><path d="M22 34h56M50 34l-1 0"/><path d="M22 34l-8 16a10 10 0 0 0 16 0z"/><path d="M78 34l-8 16a10 10 0 0 0 16 0z"/>',
  brainbolt:'<path d="M40 30a12 12 0 0 0 0 40"/><path d="M40 30a10 10 0 0 1 18 2"/><path d="M40 70a10 10 0 0 0 14 2"/><path d="M40 30v40"/><path d="M64 28l-10 18h9l-11 22" fill="none"/>',
  clipboard:'<rect x="30" y="26" width="40" height="52" rx="4"/><rect x="42" y="20" width="16" height="10" rx="3"/><path d="M38 42h24M38 52h24M38 62h16"/>',
  notebook:'<rect x="30" y="24" width="38" height="54" rx="3"/><path d="M30 24v54"/><path d="M40 38h20M40 48h20M40 58h14"/><path d="M66 30l6 3-16 30-8 3 2-8z" fill="none"/>',
  scissors:'<circle cx="32" cy="34" r="7"/><circle cx="32" cy="66" r="7"/><path d="M38 38l38 26M38 62l38-26"/>',
  globe:'<circle cx="50" cy="50" r="28"/><path d="M22 50h56M50 22v56"/><path d="M50 22c12 10 12 46 0 56M50 22c-12 10-12 46 0 56"/>',
  hourglass:'<path d="M32 22h36M32 78h36"/><path d="M36 22l14 28 14-28M36 78l14-28 14 28"/><path d="M44 64h12" opacity=".6"/>',
  gearcheck:'<path d="M28 44a23 23 0 0 1 42-6"/><path d="M72 56a23 23 0 0 1-42 6"/><path d="M70 26v12h-12M30 74v-12h12"/><path d="M41 50l6 7 12-14"/>',
  feather:'<path d="M68 28C46 26 30 46 28 68l10-2c4-16 14-28 30-38z"/><path d="M40 60l16-16M46 66l18-18"/><path d="M28 68l-6 8"/>',
  loop:'<path d="M32 42a20 20 0 0 1 36-6"/><path d="M68 58a20 20 0 0 1-36 6"/><path d="M68 28v10h-10M32 72v-10h10"/>',
  steps:'<path d="M24 74h14v-14h14v-14h14V32h14"/><path d="M62 24l10 8-10 8" fill="none"/>',
  pause:'<circle cx="50" cy="50" r="28"/><path d="M44 40v20M56 40v20"/>',
  drop:'<path d="M50 22c10 14 18 24 18 34a18 18 0 0 1-36 0c0-10 8-20 18-34z"/><path d="M42 56a8 8 0 0 0 8 8"/>',
  tag:'<path d="M26 26h24l28 28-24 24-28-28z"/><circle cx="40" cy="40" r="5" fill="currentColor" stroke="none"/>',
  mask:'<path d="M30 30h40v18c0 16-10 28-20 28S30 64 30 48z"/><path d="M40 46a4 4 0 0 1 8 0M52 46a4 4 0 0 1 8 0"/><path d="M44 62a8 6 0 0 0 12 0"/>',
  sun:'<circle cx="50" cy="52" r="14"/><path d="M50 26v-6M50 84v-2M24 52h-6M82 52h-6M32 34l-4-4M72 34l4-4M32 70l-4 4M72 70l4 4"/><path d="M20 82h60" opacity=".5"/>',
  breath:'<path d="M50 26v20"/><path d="M50 46c-10 0-16 6-16 16v10a8 8 0 0 0 16 0M50 46c10 0 16 6 16 16v10a8 8 0 0 1-16 0"/><path d="M22 40c6-4 6 8 12 4M78 40c-6-4-6 8-12 4" opacity=".6"/>',
  posture:'<circle cx="50" cy="26" r="7"/><path d="M50 34v28M50 62l-10 18M50 62l10 18M50 44l-14 4M50 44l14 4"/>',
  steadywave:'<path d="M20 50h12l6-14 8 28 8-22 6 8h20"/><path d="M20 72h60" opacity=".4"/>',
  footsteps:'<ellipse cx="38" cy="40" rx="6" ry="9"/><ellipse cx="60" cy="58" rx="6" ry="9"/><path d="M33 50l2 6M65 68l-2 6" opacity=".6"/>',
  curve:'<path d="M24 74V22M24 74h54"/><path d="M28 34c14 0 10 34 46 34"/><path d="M40 30l-6 6M40 30l6 6" opacity="0"/><circle cx="34" cy="40" r="2.5" fill="currentColor" stroke="none"/><circle cx="52" cy="60" r="2.5" fill="currentColor" stroke="none"/>',
  checkbox:'<rect x="28" y="28" width="44" height="44" rx="8"/><path d="M40 50l7 8 16-18"/>',
  speech:'<path d="M26 30h48a6 6 0 0 1 6 6v24a6 6 0 0 1-6 6H46l-14 12v-12h-6a6 6 0 0 1-6-6V36a6 6 0 0 1 6-6z"/><path d="M38 44h24M38 54h16"/>',
  shuffle:'<path d="M24 36h12l28 28h12M24 64h12l10-10M58 46l6-10h12"/><path d="M70 28l8 8-8 8M70 56l8 8-8 8" fill="none"/>',
  dumbbell:'<path d="M30 50h40"/><rect x="20" y="40" width="10" height="20" rx="3"/><rect x="70" y="40" width="10" height="20" rx="3"/><rect x="14" y="44" width="6" height="12" rx="2"/><rect x="80" y="44" width="6" height="12" rx="2"/>',
  twospeed:'<path d="M22 66a28 28 0 0 1 56 0"/><path d="M50 66l16-18"/><circle cx="50" cy="66" r="4" fill="currentColor" stroke="none"/><path d="M30 60l-4-2M70 60l4-2M50 40v-4" opacity=".6"/>',
  invert:'<path d="M38 26v40M38 66l-7-8M38 66l7-8"/><path d="M62 74V34M62 34l-7 8M62 34l7 8"/>',
  magnifier:'<circle cx="44" cy="44" r="18"/><path d="M58 58l18 18"/><path d="M44 36a8 8 0 0 0-8 8" opacity=".6"/>',
  dice:'<rect x="28" y="28" width="44" height="44" rx="8"/><circle cx="40" cy="40" r="3.5" fill="currentColor" stroke="none"/><circle cx="60" cy="40" r="3.5" fill="currentColor" stroke="none"/><circle cx="50" cy="50" r="3.5" fill="currentColor" stroke="none"/><circle cx="40" cy="60" r="3.5" fill="currentColor" stroke="none"/><circle cx="60" cy="60" r="3.5" fill="currentColor" stroke="none"/>',
  map:'<path d="M24 32l18-8 16 8 18-8v44l-18 8-16-8-18 8z"/><path d="M42 24v44M58 32v44"/>',
  turtle:'<path d="M32 60a18 12 0 0 1 36 0z"/><path d="M50 48v12M40 52l4 8M60 52l-4 8"/><path d="M68 56l8-2M32 64l-6 6M40 68l-2 6M60 68l2 6"/><circle cx="74" cy="52" r="4"/>',
  razor:'<path d="M26 62l40-30a6 6 0 0 1 8 8L44 70z"/><path d="M26 62l-4 8 8-4"/><path d="M40 66l6-4" opacity=".6"/>',
  warning:'<path d="M50 24l30 52H20z"/><path d="M50 44v16M50 68v.5"/>',
  trash:'<path d="M30 34h40M40 34v-6h20v6M34 34l3 42h26l3-42"/><path d="M44 44v24M56 44v24"/>',
  control:'<circle cx="50" cy="50" r="10"/><circle cx="50" cy="50" r="26" stroke-dasharray="4 6"/><path d="M50 24v6M50 70v6M24 50h6M70 50h6"/>',
  bodybrain:'<circle cx="50" cy="26" r="9"/><path d="M46 22a4 4 0 0 1 8 0M50 18v3" opacity=".6"/><path d="M50 35v26M50 61l-10 18M50 61l10 18M50 42l-14 5M50 42l14 5"/>',
  book:'<path d="M50 32c-8-6-18-6-24-4v40c6-2 16-2 24 4M50 32c8-6 18-6 24-4v40c-6-2-16-2-24 4M50 32v40"/>',
  chunk:'<rect x="26" y="26" width="20" height="20" rx="4"/><rect x="54" y="26" width="20" height="20" rx="4"/><rect x="40" y="54" width="20" height="20" rx="4"/><path d="M46 46l-2 8M56 46l4 8" opacity=".55"/>',
  bricks:'<path d="M26 40h48M26 56h48M26 72h48"/><path d="M38 40v16M62 40v16M50 56v16M38 72v-4" opacity=".9"/><path d="M26 34h48v38H26z"/>',
  flaw:'<circle cx="50" cy="50" r="26"/><path d="M50 24l-6 20 10 6-8 26" fill="none"/>',
  clock2:'<circle cx="50" cy="52" r="26"/><path d="M50 52V36M50 52l12 8"/><path d="M40 22h20" />',
  brokenchain:'<path d="M32 44a10 10 0 0 1 14-14l6 6"/><path d="M68 56a10 10 0 0 1-14 14l-6-6"/><path d="M44 40l-6 6M62 54l-6 6" opacity=".5"/><path d="M50 46l0 8" opacity="0"/>',
  growthup:'<path d="M24 74h52"/><path d="M32 66V50M46 66V38M60 66V26"/><path d="M60 26l-6 4M60 26l6 4" opacity=".7"/>',
  moodup:'<circle cx="50" cy="50" r="26"/><path d="M40 46a3 3 0 0 1 6 0M54 46a3 3 0 0 1 6 0"/><path d="M38 58a14 10 0 0 0 24 0"/>',
  bed:'<path d="M22 44v28M22 60h56v12M78 52v20"/><path d="M22 60c0-8 6-12 14-12h26a16 16 0 0 1 16 16"/><circle cx="36" cy="52" r="5"/>',
  teach:'<path d="M50 26l28 12-28 12-28-12z"/><path d="M50 50v12M38 44v14a12 6 0 0 0 24 0V44" opacity=".9"/>'
};

/* id de carte -> illustration */
const VISUELS = {
  n1:'brain', n2:'synapse', n3:'reroute', n4:'prune', n5:'spark', n6:'moon', n7:'run', n8:'eye', n9:'target', n10:'eye', n11:'flaw', n12:'meditate',
  t1:'balance', t2:'chart', t3:'shield', t4:'control', t5:'brainbolt', t6:'balance', t7:'clipboard', t8:'notebook', t9:'scissors', t10:'globe', t11:'hourglass', t12:'gearcheck',
  m1:'feather', m2:'loop', m3:'steps', m4:'pause', m5:'control', m6:'drop', m7:'tag', m8:'mask', m9:'bricks', m10:'flaw', m11:'clock2', m12:'brokenchain', m13:'growthup',
  p1:'bodybrain', p2:'moodup', p3:'bed', p4:'drop', p5:'breath', p6:'sun', p7:'posture', p8:'steadywave', p9:'footsteps',
  a1:'curve', a2:'checkbox', a3:'speech', a4:'shuffle', a5:'dumbbell', a6:'clock2', a7:'bed', a8:'teach', a9:'chunk',
  r1:'twospeed', r2:'invert', r3:'magnifier', r4:'dice', r5:'trash', r6:'turtle', r7:'razor', r8:'warning', r9:'map'
};
const THEME_ICON = { neuro:'brain', trading:'chart', mental:'feather', physique:'bodybrain', appren:'book', reflex:'twospeed' };

/* ============================================================
   SCÈNES — infographies pédagogiques (une image qui explique l'idée)
   viewBox 0 0 320 180. c = couleur du thème.
   ============================================================ */
const SCENES = {
  plast:(c)=>`
    <text x="52" y="24" fill="#fff" font-size="12" font-weight="700">Avant</text>
    <text x="196" y="24" fill="${c}" font-size="12" font-weight="700">Après apprentissage</text>
    <g stroke="${c}" stroke-width="2" opacity=".55"><circle cx="55" cy="70" r="4" fill="${c}"/><circle cx="95" cy="105" r="4" fill="${c}"/><circle cx="70" cy="140" r="4" fill="${c}"/><line x1="55" y1="70" x2="95" y2="105"/></g>
    <path d="M150 95 h26 m-7 -6 l7 6 -7 6" stroke="#fff" stroke-width="2.5"/>
    <g stroke="${c}" stroke-width="2"><circle cx="228" cy="60" r="4" fill="${c}"/><circle cx="278" cy="88" r="4" fill="${c}"/><circle cx="240" cy="120" r="4" fill="${c}"/><circle cx="290" cy="140" r="4" fill="${c}"/><circle cx="210" cy="108" r="4" fill="${c}"/>
      <line x1="228" y1="60" x2="278" y2="88"/><line x1="278" y1="88" x2="240" y2="120"/><line x1="240" y1="120" x2="210" y2="108"/><line x1="210" y1="108" x2="228" y2="60"/><line x1="240" y1="120" x2="290" y2="140"/><line x1="278" y1="88" x2="290" y2="140"/></g>`,
  hebb:(c)=>`
    <circle cx="80" cy="82" r="20" stroke="${c}" stroke-width="3"/><circle cx="240" cy="82" r="20" stroke="${c}" stroke-width="3"/>
    <g stroke="${c}" stroke-width="2"><path d="M62 72l-20-8M60 90l-20 8M58 82l-22 0"/><path d="M258 72l20-8M260 90l20 8M262 82l22 0"/></g>
    <path d="M102 82 h116" stroke="${c}" stroke-width="3"/>
    <path d="M150 68 l5 10 11 2 -11 3 -3 12 -5 -11 -11 -2 11 -3z" fill="${c}" stroke="none"/>
    <text x="70" y="150" fill="#fff" font-size="13" font-weight="700">S'activent ensemble → se lient</text>`,
  reorg:(c)=>`
    <circle cx="46" cy="92" r="6" fill="${c}"/><circle cx="274" cy="92" r="6" fill="${c}"/>
    <path d="M52 92 h56" stroke="${c}" stroke-width="3"/>
    <g stroke="#EF6B6B" stroke-width="3"><path d="M120 78 l18 18 -18 18M138 78 l-18 18 18 18"/></g>
    <path d="M112 90 C 150 36, 220 36, 268 86" stroke="${c}" stroke-width="3"/>
    <path d="M262 80 l8 8 -11 3" stroke="${c}" stroke-width="3"/>
    <text x="82" y="150" fill="#fff" font-size="12.5" font-weight="700">Une route contourne la lésion</text>`,
  uselose:(c)=>`
    <text x="42" y="24" fill="${c}" font-size="12" font-weight="700">Utilisé → renforcé</text>
    <text x="186" y="24" fill="#fff" fill-opacity=".55" font-size="12" font-weight="700">Ignoré → s'efface</text>
    <g stroke="${c}" stroke-width="3"><circle cx="60" cy="70" r="5" fill="${c}"/><circle cx="105" cy="105" r="5" fill="${c}"/><circle cx="70" cy="140" r="5" fill="${c}"/><line x1="60" y1="70" x2="105" y2="105"/><line x1="105" y1="105" x2="70" y2="140"/><line x1="70" y1="140" x2="60" y2="70"/></g>
    <g stroke="#fff" stroke-opacity=".28" stroke-width="2" stroke-dasharray="4 5"><circle cx="230" cy="80" r="5" fill="#fff" fill-opacity=".2"/><circle cx="278" cy="115" r="5" fill="#fff" fill-opacity=".12"/><circle cx="238" cy="145" r="5" fill="#fff" fill-opacity=".08"/><line x1="230" y1="80" x2="278" y2="115"/><line x1="278" y1="115" x2="238" y2="145"/></g>`,
  sleepmem:(c)=>`
    <circle cx="55" cy="78" r="14" stroke="${c}" stroke-width="3"/><g stroke="${c}" stroke-width="2"><path d="M55 56v-7M55 107v-7M31 78h-7M86 78h-7M39 62l-5-5M76 94l-5-5M71 62l5-5M39 94l-5 5"/></g>
    <text x="34" y="150" fill="#fff" font-size="11" font-weight="700">Apprendre</text>
    <path d="M104 78 h24 m-7 -6 l7 6 -7 6" stroke="#fff" stroke-width="2.5"/>
    <path d="M172 62 a20 20 0 1 0 0 30 15 15 0 0 1 0-30z" stroke="${c}" stroke-width="3"/>
    <text x="150" y="150" fill="#fff" font-size="11" font-weight="700">Dormir</text>
    <path d="M212 78 h24 m-7 -6 l7 6 -7 6" stroke="#fff" stroke-width="2.5"/>
    <g stroke="${c}" stroke-width="3"><circle cx="285" cy="66" r="4" fill="${c}"/><circle cx="268" cy="92" r="4" fill="${c}"/><circle cx="293" cy="98" r="4" fill="${c}"/><line x1="285" y1="66" x2="268" y2="92"/><line x1="268" y1="92" x2="293" y2="98"/><line x1="293" y1="98" x2="285" y2="66"/></g>
    <text x="246" y="150" fill="${c}" font-size="11" font-weight="700">Mémoire</text>`,
  bdnf:(c)=>`
    <circle cx="52" cy="66" r="6" fill="${c}"/><path d="M52 72 l-8 12 8 8 -4 18" stroke="${c}" stroke-width="3"/><g stroke="${c}" stroke-width="3"><path d="M44 84l-10 4M60 92l10 6M44 100l-8 10"/></g>
    <text x="34" y="150" fill="#fff" font-size="11" font-weight="700">Bouger</text>
    <path d="M96 88 h26 m-7 -6 l7 6 -7 6" stroke="#fff" stroke-width="2.5"/>
    <rect x="140" y="72" width="66" height="30" rx="7" stroke="${c}" stroke-width="2.5"/><text x="150" y="92" fill="${c}" font-size="14" font-weight="800">BDNF</text>
    <path d="M220 88 h24 m-7 -6 l7 6 -7 6" stroke="#fff" stroke-width="2.5"/>
    <g stroke="${c}" stroke-width="3"><circle cx="288" cy="70" r="4" fill="${c}"/><circle cx="270" cy="98" r="4" fill="${c}"/><circle cx="296" cy="104" r="4" fill="${c}"/><line x1="288" y1="70" x2="270" y2="98"/><line x1="270" y1="98" x2="296" y2="104"/></g>
    <text x="240" y="150" fill="${c}" font-size="11" font-weight="700">+ neurones</text>`,
  dopa:(c)=>`
    <circle cx="160" cy="96" r="32" stroke="${c}" stroke-width="3"/><circle cx="160" cy="96" r="17" stroke="${c}" stroke-width="2.5"/><circle cx="160" cy="96" r="5" fill="${c}"/>
    <path d="M160 24 l6 14 15 1 -11 10 4 15 -14 -9 -14 9 4 -15 -11 -10 15 -1z" fill="${c}" stroke="none"/>
    <text x="86" y="168" fill="#fff" font-size="12" font-weight="700">Petite victoire → le cerveau grave</text>`,
  attention:(c)=>`
    <text x="30" y="26" fill="#fff" fill-opacity=".6" font-size="11" font-weight="700">distractions</text>
    <g stroke="#fff" stroke-opacity=".4" stroke-width="2"><line x1="40" y1="52" x2="120" y2="86"/><line x1="40" y1="78" x2="120" y2="92"/><line x1="40" y1="104" x2="120" y2="98"/><line x1="40" y1="128" x2="120" y2="104"/></g>
    <path d="M120 74 L172 92 L120 110 Z" stroke="${c}" stroke-width="3"/>
    <path d="M172 92 h44 m-7 -6 l7 6 -7 6" stroke="${c}" stroke-width="3"/>
    <g stroke="${c}" stroke-width="3"><circle cx="248" cy="74" r="4" fill="${c}"/><circle cx="280" cy="98" r="4" fill="${c}"/><circle cx="244" cy="112" r="4" fill="${c}"/><line x1="248" y1="74" x2="280" y2="98"/><line x1="280" y1="98" x2="244" y2="112"/></g>
    <text x="150" y="164" fill="${c}" font-size="12" font-weight="700">1 focus → plasticité</text>`,
  prefrontal:(c)=>`
    <text x="140" y="26" fill="#fff" font-size="13" font-weight="800">À +1500 €</text>
    <path d="M120 66 a30 26 0 1 0 0 42" stroke="${c}" stroke-width="3"/><path d="M120 66 a24 20 0 0 1 40 6" stroke="${c}" stroke-width="3"/><path d="M120 108 a24 20 0 0 0 34 6" stroke="${c}" stroke-width="3"/>
    <path d="M98 72 a16 26 0 0 0 0 30" stroke="#EF6B6B" stroke-width="4"/>
    <text x="52" y="150" fill="#EF6B6B" font-size="12" font-weight="700">Préfrontal OFF</text>
    <path d="M188 60 l-11 22 h10 l-12 24" stroke="${c}" stroke-width="3"/>
    <text x="205" y="96" fill="${c}" font-size="12" font-weight="700">dopamine</text>`,
  bestloser:(c)=>`
    <text x="40" y="26" fill="#fff" font-size="13" font-weight="700">Perdre petit = durer</text>
    <line x1="40" y1="98" x2="290" y2="98" stroke="#fff" stroke-opacity=".25"/>
    <path d="M40 98 L110 116 L160 92 L230 114 L288 88" stroke="${c}" stroke-width="3"/>
    <text x="200" y="80" fill="${c}" font-size="11" font-weight="700">survit</text>
    <path d="M40 98 L90 90 L140 110 L190 140 L232 166" stroke="#EF6B6B" stroke-width="3"/>
    <text x="150" y="162" fill="#EF6B6B" font-size="11" font-weight="700">compte cramé</text>`,
  eighty:(c)=>`
    <rect x="40" y="66" width="176" height="42" fill="#EF6B6B" fill-opacity=".9"/><rect x="216" y="66" width="64" height="42" fill="${c}"/>
    <text x="82" y="92" fill="#fff" font-size="16" font-weight="800">80% perdent</text>
    <text x="226" y="92" fill="#101010" font-size="15" font-weight="800">20%</text>
    <text x="40" y="140" fill="#fff" font-size="12.5" font-weight="700">Fais l'inverse de la masse</text>`,
  stoploss:(c)=>`
    <text x="40" y="26" fill="#fff" font-size="12.5" font-weight="700">Le stop protège le capital</text>
    <path d="M40 58 L80 88 L110 68 L150 108 L180 92 L208 138" stroke="${c}" stroke-width="3"/>
    <line x1="40" y1="120" x2="290" y2="120" stroke="#EF6B6B" stroke-width="2.5" stroke-dasharray="6 5"/>
    <text x="214" y="116" fill="#EF6B6B" font-size="12" font-weight="800">STOP</text>
    <path d="M250 52 l24 8 v15 c0 16-12 23-24 29 -12-6-24-13-24-29 V60z" stroke="${c}" stroke-width="2.5"/><path d="M240 78 l7 8 12-14" stroke="${c}" stroke-width="2.5"/>`,
  risk1:(c)=>`
    <text x="40" y="26" fill="${c}" font-size="12" font-weight="700">99% capital protégé</text>
    <rect x="40" y="60" width="240" height="42" stroke="#fff" stroke-opacity=".45" stroke-width="2"/><rect x="40" y="60" width="8" height="42" fill="#EF6B6B"/>
    <text x="30" y="126" fill="#EF6B6B" font-size="12" font-weight="700">1% risqué</text>
    <text x="40" y="158" fill="#fff" font-size="12.5" font-weight="700">Risque 1% → tu dures 100 trades</text>`,
  lossav:(c)=>`
    <path d="M160 42 v72 M120 150 h80" stroke="#fff" stroke-width="3"/>
    <path d="M104 58 h112" stroke="#fff" stroke-width="3" transform="rotate(-13 160 58)"/>
    <circle cx="118" cy="92" r="22" fill="#EF6B6B" fill-opacity=".9"/><text x="101" y="97" fill="#fff" font-size="13" font-weight="800">-100</text>
    <circle cx="208" cy="50" r="15" fill="${c}"/><text x="194" y="55" fill="#101010" font-size="12" font-weight="800">+100</text>
    <text x="52" y="170" fill="#fff" font-size="12.5" font-weight="700">La perte pèse deux fois plus</text>`,
  plan:(c)=>`
    <text x="66" y="26" fill="${c}" font-size="12" font-weight="700">Plan écrit AVANT d'entrer</text>
    <rect x="95" y="42" width="130" height="108" rx="8" stroke="${c}" stroke-width="2.5"/>
    <g stroke="${c}" stroke-width="2.5"><path d="M110 66 l6 6 10-12"/><path d="M110 96 l6 6 10-12"/><path d="M110 126 l6 6 10-12"/></g>
    <text x="134" y="70" fill="#fff" font-size="13" font-weight="700">Entrée</text>
    <text x="134" y="100" fill="#fff" font-size="13" font-weight="700">Stop</text>
    <text x="134" y="130" fill="#fff" font-size="13" font-weight="700">Objectif</text>`,
  compound:(c)=>`
    <line x1="40" y1="150" x2="292" y2="150" stroke="#fff" stroke-opacity=".3"/><line x1="40" y1="28" x2="40" y2="150" stroke="#fff" stroke-opacity=".3"/>
    <path d="M40 148 C 170 145, 225 120, 286 40" stroke="${c}" stroke-width="3.5"/><circle cx="286" cy="40" r="5" fill="${c}"/>
    <text x="150" y="76" fill="${c}" font-size="17" font-weight="800">×37</text>
    <text x="58" y="140" fill="#fff" font-size="12" font-weight="700">1% par jour</text>
    <text x="205" y="168" fill="#fff" font-size="12" font-weight="700">en 1 an</text>`,
  systems:(c)=>`
    <path d="M160 50 A46 46 0 1 1 118 60" stroke="${c}" stroke-width="3"/><path d="M118 60 l-3 -16 16 5" stroke="${c}" stroke-width="3"/>
    <text x="132" y="46" fill="#fff" font-size="13" font-weight="700">Système</text>
    <text x="196" y="100" fill="#fff" font-size="13" font-weight="700">Action</text>
    <text x="120" y="160" fill="#fff" font-size="13" font-weight="700">Résultat</text>
    <text x="40" y="100" fill="${c}" font-size="12" font-weight="700">répète</text>`,
  identity:(c)=>`
    <rect x="40" y="52" width="164" height="34" rx="8" stroke="${c}" stroke-width="2.5"/><text x="52" y="74" fill="#fff" font-size="12.5" font-weight="700">« Je suis discipliné »</text>
    <path d="M120 90 v14 m-6 -6 l6 6 6 -6" stroke="#fff" stroke-width="2.5"/>
    <g stroke="${c}" stroke-width="2.5"><path d="M56 120 l5 6 10-12"/><path d="M96 120 l5 6 10-12"/><path d="M136 120 l5 6 10-12"/></g>
    <text x="60" y="152" fill="${c}" font-size="11.5" font-weight="700">chaque acte = un vote</text>
    <circle cx="256" cy="76" r="15" stroke="${c}" stroke-width="2.5"/><path d="M234 120 a22 20 0 0 1 44 0" stroke="${c}" stroke-width="2.5"/>`,
  twospeed:(c)=>`
    <text x="46" y="26" fill="${c}" font-size="11" font-weight="700">rapide</text><text x="228" y="26" fill="#fff" font-size="11" font-weight="700">lent</text>
    <path d="M72 66 a32 32 0 0 0 0 64z" stroke="${c}" stroke-width="3" fill="${c}" fill-opacity=".15"/>
    <text x="42" y="152" fill="${c}" font-size="12.5" font-weight="700">Système 1</text>
    <path d="M248 66 a32 32 0 0 1 0 64z" stroke="#fff" stroke-width="3" fill="#fff" fill-opacity=".1"/>
    <text x="222" y="152" fill="#fff" font-size="12.5" font-weight="700">Système 2</text>
    <line x1="160" y1="46" x2="160" y2="140" stroke="#fff" stroke-opacity=".2" stroke-dasharray="4 5"/>`,
  spaced:(c)=>`
    <line x1="42" y1="30" x2="42" y2="150" stroke="#fff" stroke-opacity=".3"/><line x1="42" y1="150" x2="298" y2="150" stroke="#fff" stroke-opacity=".3"/>
    <path d="M42 44 C 80 120, 108 138, 118 138 L118 66 C 150 130,168 138,178 138 L178 74 C 214 128,232 134,298 122" stroke="${c}" stroke-width="3"/>
    <g fill="${c}"><circle cx="118" cy="66" r="4"/><circle cx="178" cy="74" r="4"/></g>
    <text x="46" y="24" fill="#fff" font-size="11" font-weight="700">Mémoire</text>
    <text x="248" y="168" fill="#fff" font-size="11" font-weight="700">Temps →</text>
    <text x="120" y="58" fill="${c}" font-size="10.5" font-weight="700">révision</text>
    <text x="182" y="66" fill="${c}" font-size="10.5" font-weight="700">révision</text>`,
  feynman:(c)=>`
    <circle cx="74" cy="74" r="15" stroke="${c}" stroke-width="3"/><path d="M74 90 v22" stroke="${c}" stroke-width="3"/><path d="M56 150 a18 16 0 0 1 36 0" stroke="${c}" stroke-width="3"/>
    <path d="M120 62 h94 a6 6 0 0 1 6 6 v36 a6 6 0 0 1 -6 6 h-58 l-16 12 v-12 h-20 a6 6 0 0 1 -6 -6 v-36 a6 6 0 0 1 6 -6z" stroke="${c}" stroke-width="2.5"/>
    <text x="134" y="88" fill="#fff" font-size="12.5" font-weight="700">Explique</text>
    <text x="134" y="106" fill="#fff" font-size="12.5" font-weight="700">simplement</text>
    <text x="44" y="172" fill="${c}" font-size="11" font-weight="700">→ tes trous apparaissent</text>`,
  sleepbed:(c)=>`
    <path d="M56 122 v-28 a12 12 0 0 1 12 -12 h58 a26 26 0 0 1 26 26 v14 M56 108 h108 M164 96 v26 M56 122 v16 M164 122 v16" stroke="${c}" stroke-width="3"/><circle cx="82" cy="96" r="8" stroke="${c}" stroke-width="3"/>
    <path d="M226 60 a20 20 0 1 0 0 30 15 15 0 0 1 0-30z" stroke="${c}" stroke-width="3"/>
    <text x="52" y="162" fill="#fff" font-size="12.5" font-weight="700">Dormir consolide la mémoire</text>`
};
const SCENE_OF = {
  n1:'plast', n2:'hebb', n3:'reorg', n4:'uselose', n6:'sleepmem', n7:'bdnf', n9:'dopa', n10:'attention',
  t1:'bestloser', t2:'eighty', t3:'stoploss', t4:'risk1', t5:'prefrontal', t6:'lossav', t7:'plan',
  m2:'systems', m3:'compound', m8:'identity', m9:'identity',
  a1:'spaced', a3:'feynman', a7:'sleepbed',
  r1:'twospeed',
  p3:'sleepbed'
};

/* ============================================================
   SOCIAL — pseudos & commentaires (pour l'ambiance "appli vivante")
   ============================================================ */
const NOMS = ["Léa M.","Thomas R.","Sofia_","Karim B.","yasmine.k","Lucas","Emma D.","noah_trade","Chloé","Maxime P.",
 "inès","Gabriel","Jade.R","Ethan","camille_z","Nathan","Manon","adam.fx","Sarah L.","Rayan",
 "Louna","Théo B.","mila_","Hugo","Anaïs","yanis.dev","Zoé","Enzo M.","clara__","Aaron",
 "Lina","Paul R.","juju","Nour","Tom_","Alicia","samir","Eva","mehdi.k","Romane"];
const COMMENTAIRES = [
 "Ça change tout 🔥","Je note direct dans ma biblio","Tellement vrai…","Punchline 💯","J'en avais besoin aujourd'hui",
 "Wow je (re)découvre ça","Merci pour le rappel 🙏","Ça résume 3 livres en 10 sec","Je partage à mon frère",
 "Exactement mon problème 😅","À relire chaque matin","La carte la plus utile ici","Ça pique mais c'est vrai",
 "Enfin expliqué simplement","Je bloque là-dessus depuis des mois","Sauvegardé ✅","Gros déclic 🤯","Trop réel",
 "C'est devenu ma routine","Appliqué depuis 2 semaines, ça marche","Le genre de truc qu'on n'apprend pas à l'école",
 "Simple et puissant","J'aurais aimé voir ça avant","Ça vaut de l'or 💰","Répète ça 100 fois","Mindset 🧠",
 "Screenshot direct","Chaque jour un peu 💪","Discipline > motivation, validé","On oublie tellement ça"];
const REPONSES=["totalement","+1","facts","carré","👏👏","grave","bien dit","💯","oui !!","exactement"];

/* ---------------- NOUVELLES CARTES (v7) ---------------- */
CARTES.push(
  { id:'n13', theme:'neuro', titre:"Le cerveau retient les histoires, pas les listes",
    corps:"Ton cerveau est câblé pour la narration. Une info transformée en histoire (avec un personnage, un enjeu, une émotion) se retient bien mieux qu'une liste sèche. Quand tu veux ancrer une idée, raconte-la : « imagine quelqu'un qui… ». Le récit crée des accroches émotionnelles auxquelles la mémoire s'agrippe.",
    source:"Mémoire narrative", auteur:"Sciences cognitives" },
  { id:'n14', theme:'neuro', titre:"Dis-le à voix haute pour mieux le retenir",
    corps:"Prononcer une information à voix haute la grave mieux que la lire en silence : c'est l'effet de production. Le geste d'articuler ajoute une trace motrice et auditive au souvenir. Après une carte, reformule-la à voix haute avec tes mots. Ton cerveau enregistre trois fois : en lisant, en parlant, en t'entendant.",
    source:"Effet de production", auteur:"Psychologie de la mémoire" },
  { id:'t13', theme:'trading', titre:"Le marché paie la patience, pas l'agitation",
    corps:"Le trader qui clique tout le temps se fatigue et se fait tondre. Celui qui attend son setup, immobile, frappe fort quand ça compte. La bourse transfère l'argent des impatients vers les patients. Ton edge n'est pas dans le nombre de trades, mais dans la qualité de ceux que tu oses ne pas prendre.",
    source:"Patience", auteur:"Devenir un trader stable" },
  { id:'t14', theme:'trading', titre:"Accepte de ne jamais être sûr",
    corps:"Le besoin de certitude est l'ennemi du trader. Le marché est probabiliste : même le meilleur setup peut perdre. Vouloir « être sûr » avant d'entrer te fait rater les bons trades et t'accrocher aux mauvais. Agis avec un plan malgré le doute. La confiance ne vient pas de la certitude, mais de ton processus.",
    source:"Incertitude", auteur:"Devenir un trader stable" },
  { id:'m14', theme:'mental', titre:"Ton environnement bat ta volonté",
    corps:"Compter sur la volonté seule est épuisant et perdant. Change plutôt ton environnement : range ton téléphone dans une autre pièce, prépare tes affaires de sport la veille, supprime l'appli qui te distrait. Rendre le bon comportement facile et le mauvais difficile fait 90 % du travail. Conçois ton décor, il décidera pour toi.",
    source:"Design de l'environnement", auteur:"James Clear" },
  { id:'m15', theme:'mental', titre:"Fais-le, même effrayé",
    corps:"Le courage n'est pas l'absence de peur, c'est agir avec elle. Attendre de ne plus avoir peur, c'est attendre pour toujours. La confiance vient APRÈS l'action, pas avant. Fais le petit pas qui te fait peur aujourd'hui : passer l'appel, prendre le trade planifié, dire la vérité. De l'autre côté de la peur, il y a ta croissance.",
    source:"Courage", auteur:"Développement personnel" },
  { id:'p10', theme:'physique', titre:"Le froid réveille ton système nerveux",
    corps:"Une douche froide de 30 secondes déclenche une décharge de noradrénaline qui booste la vigilance, l'humeur et la résistance au stress pendant des heures. C'est un entraînement mental autant que physique : rester calme dans l'inconfort volontaire. Commence tiède, finis froid. Tu apprends à ton cerveau à ne pas fuir la difficulté.",
    source:"Exposition au froid", auteur:"Physiologie" },
  { id:'p11', theme:'physique', titre:"Nourris ton cerveau (oméga-3, vrai carburant)",
    corps:"Ton cerveau est composé en grande partie de gras : les oméga-3 (poissons gras, noix, graines) entretiennent les membranes des neurones et la fluidité des connexions. Trop de sucre et d'ultra-transformé, à l'inverse, encrasse la machine. Manger pour ton cerveau, c'est manger pour ta lucidité et ta mémoire.",
    source:"Nutrition cérébrale", auteur:"Neuronutrition" },
  { id:'a10', theme:'appren', titre:"Prends tes notes à la main",
    corps:"Écrire à la main est plus lent que taper — et c'est justement pour ça que c'est plus efficace. La lenteur t'oblige à reformuler, sélectionner, comprendre au lieu de recopier mot à mot. Les études montrent une meilleure mémorisation avec le stylo. Pour ancrer une idée, ne la tape pas : écris-la.",
    source:"Note-taking", auteur:"Sciences de l'apprentissage" },
  { id:'a11', theme:'appren', titre:"Fais des pauses : le cerveau apprend au repos",
    corps:"Juste après avoir appris, de courtes pauses (même 10 secondes les yeux fermés) permettent au cerveau de rejouer et consolider l'info à toute vitesse. Enchaîner sans respirer sature la mémoire. Alterne travail concentré et micro-pauses. Le repos n'est pas l'arrêt de l'apprentissage : c'en est une partie active.",
    source:"Consolidation éveillée", auteur:"Neurosciences" },
  { id:'r10', theme:'reflex', titre:"La règle 10/10/10",
    corps:"Avant une décision, demande-toi : comment je me sentirai dans 10 minutes ? dans 10 mois ? dans 10 ans ? Ce zoom arrière dégonfle les émotions du moment et révèle ce qui compte vraiment. Beaucoup de tentations perdent leur pouvoir quand on les regarde à l'échelle de 10 ans. Décide depuis le futur, pas depuis l'impulsion.",
    source:"10/10/10", auteur:"Suzy Welch" },
  { id:'r11', theme:'reflex', titre:"Sépare le signal du bruit",
    corps:"On se noie sous l'information : actus, avis, notifications. 95 % est du bruit qui agite sans informer. Le signal, c'est le petit nombre de faits qui changent vraiment ta décision. Apprends à demander : « est-ce que ça modifie ce que je vais faire ? » Sinon, ignore. Protéger ton attention, c'est protéger ta lucidité.",
    source:"Signal vs bruit", auteur:"Nassim Taleb (adapté)" }
);
