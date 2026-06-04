from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "support-technique-seance-04.html"
INDEX_OUT = ROOT / "index.html"


DOCS = {
    "download": "https://claude.com/download",
    "support": "https://support.claude.com/",
    "mcp": "https://support.claude.com/en/articles/11175166-about-custom-connectors-using-remote-mcp",
    "transcription": "transcription/seance-04-cowork-transcription.md",
}


IMAGES = [
    "01-download-claude-desktop.png",
    "02-open-claude-app.png",
    "03-cowork-home.png",
    "04-create-qg-folder.png",
    "05-choose-folder-menu.png",
    "06-finder-qg-denem.png",
    "07-connectors-menu.png",
    "08-connectors-directory.png",
    "09-settings-connectors.png",
    "10-custom-mcp-connector.png",
    "11-google-calendar-detail.png",
    "12-connected-tools-menu.png",
    "13-calendar-task-auth.png",
    "14-calendar-progress.png",
    "15-final-menu-connectors.png",
    "16-skills-directory.png",
]


def section(
    title: str,
    moment: str,
    image: int,
    why: str,
    action: str,
    check: str,
    example: str,
    *,
    link: str = "support",
) -> dict[str, str | int]:
    return {
        "title": title,
        "moment": moment,
        "image": image,
        "why": why,
        "action": action,
        "check": check,
        "example": example,
        "link": link,
    }


CHAPTERS = [
    (
        "Acte 1 - Placer Cowork dans la méthode",
        "La séance commence par une idée simple : Cowork sert de QG pour organiser le business, les clients, les dossiers et les outils connectés.",
        "Comprendre",
        "blue",
        [
            section("Le rôle de Cowork", "00:00", 3, "Cowork est présenté comme le dernier outil de l’acte 1. Claude Code sert à construire, Codex sert à déléguer quand le projet devient plus complexe, n8n sert à automatiser avec une vue claire, et Cowork sert à organiser tout le travail autour des projets.", "Gardez cette séparation dès le départ. Si le besoin est de créer du code, ce n’est pas Cowork. Si le besoin est de retrouver, organiser, planifier et centraliser, Cowork devient le bon endroit.", "Le rôle de chaque outil est clair avant de commencer une tâche.", "Question terrain : est-ce que le problème actuel demande de construire, automatiser, déléguer ou organiser ?"),
            section("Le QG d’organisation", "00:32", 3, "Le formateur insiste sur le mot QG. L’idée n’est pas d’ouvrir encore une application de plus. L’idée est de créer un espace central où les documents, les comptes rendus, les rendez-vous, les dossiers clients et les consignes restent accessibles.", "Pensez Cowork comme une base de travail. Les éléments importants doivent finir dans le bon dossier ou dans le bon outil connecté, sinon Cowork n’a pas assez de contexte.", "Le QG donne une vue simple du travail en cours.", "Exemple : un dossier client contient le brief, le devis, les notes de réunion, les livrables et les prochaines actions."),
            section("Pourquoi l’organisation passe avant la vitesse", "00:41", 3, "La séance rappelle qu’un business devient vite dur à gérer si les informations sont dispersées. Quand les rendez-vous sont dans Calendar, les fichiers dans Drive, les notes dans Fireflies et les propositions dans Docs, chaque recherche coûte du temps.", "Avant de chercher une automatisation, rangez le processus. Cowork aide quand les informations ont déjà une place logique.", "Le même client ne demande pas cinq recherches dans cinq outils différents.", "Si un client appelle, vous devez pouvoir retrouver le contexte sans fouiller partout."),
            section("Le lien avec la séance 6", "00:46", 3, "La formation annonce une suite : connecter Gmail, Calendar, Drive et Fireflies, puis créer des templates de propositions, contrats, dossiers clients et comptes rendus. Cette séance prépare le terrain.", "Ne cherchez pas à tout connecter dès maintenant. Comprenez d’abord le principe, puis ajoutez les outils quand ils servent vraiment le workflow business.", "Les prochaines séances pourront s’appuyer sur un QG propre.", "Objectif court : installer, connecter un dossier, connecter Calendar, comprendre les connecteurs."),
            section("Le problème des réunions", "01:01", 3, "Le formateur prend l’exemple d’un call client d’une heure. Réécouter toute la réunion pour retrouver les points importants fait perdre du temps. Cowork devient utile quand il peut lire un récap, extraire les actions et préparer une suite.", "Après chaque réunion importante, conservez une trace exploitable : transcription, résumé, décisions, tâches et questions ouvertes.", "Une réunion produit une suite claire, pas seulement un fichier oublié.", "Demande possible : résume les points importants et prépare les actions à faire par personne."),
            section("Le but commercial", "01:35", 3, "Le support ne parle pas seulement d’outil. Dans la vidéo, Cowork sert à mieux préparer une présentation, mieux répondre au besoin client et augmenter les chances de signer. L’organisation sert directement la vente et la livraison.", "Reliez chaque action Cowork à un résultat business : gagner du temps, mieux préparer un call, suivre un client, livrer plus proprement.", "Chaque dossier ou document sert une décision, une vente ou une livraison.", "Un compte rendu clair peut devenir une proposition mieux ciblée."),
            section("La partie connecteurs", "01:42", 7, "Le point fort mis en avant est la partie connecteurs. Cowork devient utile quand il peut accéder à Calendar, Drive, Gmail, Notion, Fireflies ou d’autres outils. Sans connecteurs, il reste plus proche d’un chat amélioré.", "Listez les outils que vous utilisez vraiment. Un connecteur inutile ajoute du bruit. Un bon connecteur donne accès à une donnée que vous consultez souvent.", "Les connecteurs choisis correspondent à votre quotidien.", "Exemple : Calendar pour planifier, Drive pour retrouver, Notion pour structurer, Gmail pour résumer."),
            section("La situation du freelance", "01:57", 3, "La formation parle d’une personne seule qui veut monter une agence ou travailler en indépendant. Le problème n’est pas seulement de produire. Le problème est de suivre plusieurs clients sans perdre le fil.", "Mettez en place une organisation que vous pouvez tenir même avec plusieurs projets en parallèle. Le QG doit rester simple et lisible.", "Un nouveau projet peut entrer dans le système sans tout casser.", "Règle simple : un client, un dossier, une synthèse, une prochaine action."),
            section("La méthode du formateur", "02:31", 3, "Le formateur explique qu’il utilise lui-même cette structure pour gagner du temps. Ce n’est pas présenté comme une démo isolée, mais comme une méthode de livraison organisée.", "Reprenez la méthode avant de la personnaliser. Une organisation simple testée vaut mieux qu’un système complexe inventé trop tôt.", "La méthode permet de retrouver rapidement les informations importantes.", "Si vous gérez 7 à 8 clients, le système doit encore tenir."),
            section("Le résumé de l’outil", "02:56", 3, "Cowork est décrit comme un agent IA dans l’application Claude Desktop. Il travaille sur l’ordinateur, peut utiliser des applications, naviguer, créer des fichiers et organiser des dossiers selon la tâche demandée.", "Retenez que Cowork travaille dans un contexte. Le résultat dépend du dossier sélectionné, des connecteurs actifs et de la précision du prompt.", "Le prompt, le dossier et les connecteurs racontent la même histoire.", "Formule simple : contexte + tâche + résultat attendu + limite de sécurité."),
        ],
    ),
    (
        "Acte 2 - Installer Claude Desktop et préparer le QG",
        "La séance passe ensuite à la pratique : télécharger l’application Desktop, l’ouvrir, puis préparer un dossier qui servira de base de travail.",
        "Installation",
        "violet",
        [
            section("Le passage par Claude Desktop", "04:29", 1, "Le formateur précise que l’usage se fait dans l’application Desktop, pas seulement dans l’application web. C’est important parce que Cowork est présenté comme un espace de travail relié au bureau, aux fichiers et aux apps.", "Téléchargez Claude Desktop depuis la page officielle. Sur Mac, le bouton propose macOS. Sur Windows, la page propose le téléchargement adapté.", "L’application Claude est installée et peut être ouverte depuis les applications.", "Lien utile : claude.com/download.", link="download"),
            section("Le téléchargement propre", "04:39", 1, "Le téléchargement est montré en direct. Le formateur ne reste pas dessus longtemps parce que l’application est déjà installée, mais le passage rappelle une règle simple : partir de la page officielle.", "Évitez les liens envoyés au hasard. Téléchargez depuis le domaine Claude officiel puis installez normalement.", "Le fichier téléchargé vient bien du site officiel.", "Si la page propose macOS ou Windows, prenez la version de votre machine.", link="download"),
            section("L’ouverture de l’application", "05:32", 2, "Une fois installée, l’application se retrouve dans les applications. Le formateur montre l’idée : ouvrir Claude Desktop puis travailler dans l’interface avec l’onglet Cowork.", "Ouvrez l’application Claude, connectez-vous si nécessaire, puis repérez les onglets Chat, Cowork et Code.", "L’onglet Cowork est visible dans l’application.", "Ne commencez pas dans le navigateur si la séance demande Cowork Desktop."),
            section("La différence avec le web", "05:38", 3, "L’interface ressemble à Claude web, mais l’objectif est différent. Ici, Cowork doit pouvoir travailler avec un dossier local et des connecteurs. Cela change la manière de penser la tâche.", "Avant de lancer une demande, vérifiez que vous êtes dans Cowork et que le bon dossier est sélectionné.", "Le dossier actif apparaît dans la zone de prompt.", "Un mauvais dossier donne un mauvais contexte."),
            section("Le dossier de travail", "05:50", 4, "La vidéo insiste sur le dossier. Pour travailler proprement avec Cowork, il faut un dossier qui regroupe les documents clients, la stratégie et les éléments importants.", "Créez un dossier simple, par exemple `QG DENEM`, `QG AGENCE` ou `CLIENTS`. Ne le cachez pas dans un chemin impossible à retrouver.", "Le dossier existe et son nom est clair.", "Le nom du dossier doit vous parler dans trois semaines."),
            section("Le nom du QG", "06:01", 4, "Le formateur crée un nouveau dossier et l’appelle QG. Le nom exact importe moins que la logique : un endroit central pour le travail important.", "Choisissez un nom court et stable. Évitez les dossiers temporaires qui changent de place.", "Le dossier reste au même endroit pendant la formation.", "Bon nom : `QG DENEM`. Mauvais nom : `test nouveau final`."),
            section("Le choix du dossier dans Cowork", "06:09", 5, "Le menu du dossier permet de choisir un autre dossier. C’est le moment où Cowork comprend dans quel espace local il doit travailler.", "Cliquez sur le menu du dossier, choisissez un autre dossier, puis sélectionnez le QG créé sur le bureau ou dans vos documents.", "Le chemin du dossier affiché correspond au bon QG.", "Si vous choisissez le mauvais dossier, Cowork risque de lire ou créer au mauvais endroit."),
            section("La fenêtre Finder", "06:13", 6, "La fenêtre Finder sert à sélectionner le dossier QG. Ce passage paraît simple, mais il est essentiel : Cowork travaille avec le contexte qu’on lui donne.", "Ouvrez le dossier, validez, puis revenez dans Cowork. Ne sélectionnez pas un fichier isolé si vous voulez travailler sur tout un espace.", "Cowork affiche le dossier choisi dans l’interface.", "Un dossier vide est acceptable au départ, mais il doit être le bon."),
            section("Le dossier vide au départ", "06:28", 6, "La vidéo montre que le dossier est vide. Le formateur explique que ce n’est pas grave : la suite de la formation servira à le remplir avec les documents et projets utiles.", "Ne bloquez pas parce que le dossier est vide. Le but de cette séance est de comprendre la connexion, pas de créer tout le système final.", "Le QG est prêt à recevoir les futurs fichiers.", "Le dossier vide est une base, pas un échec."),
            section("La raison du QG", "06:56", 6, "Le point important est répété : quand les documents deviennent nombreux, il faut un cap constant, un suivi personnel et une organisation qui évite de perdre du temps.", "Pensez au futur volume : clients, briefs, contrats, comptes rendus, exports, supports, propositions. Tout doit pouvoir être rangé sans réfléchir.", "Le QG peut accueillir plusieurs projets sans devenir illisible.", "Un bon QG vous aide surtout quand vous êtes occupé."),
        ],
    ),
    (
        "Acte 3 - Comprendre l’interface Cowork",
        "Une fois le dossier prêt, la séance montre comment discuter avec Cowork, choisir le contexte et suivre ce qu’il fait pendant une tâche.",
        "Interface",
        "cyan",
        [
            section("La zone de demande", "05:38", 3, "La grande zone de saisie permet d’expliquer la tâche. Le formateur rappelle que, comme avec Claude Code, on crée un prompt puis l’agent réalise la tâche.", "Écrivez une demande concrète. Dites le résultat attendu, le contexte et les limites. Cowork doit savoir s’il doit créer, organiser, lire, planifier ou résumer.", "La demande contient une action claire.", "Exemple : prépare un compte rendu avec les décisions et les actions à faire."),
            section("Le modèle choisi", "05:38", 3, "L’interface affiche le modèle utilisé. Dans la vidéo, le modèle apparaît dans la zone de prompt. Ce détail rappelle que Cowork reste une IA : il faut vérifier le résultat.", "Gardez le modèle par défaut si vous débutez. Concentrez-vous d’abord sur la qualité du prompt et du contexte.", "La sortie est relue avant d’être utilisée pour un client.", "Même avec un bon modèle, une vérification reste nécessaire."),
            section("Le dossier dans la zone de prompt", "05:47", 5, "Le dossier sélectionné apparaît directement dans l’interface. C’est le contexte local que Cowork peut utiliser.", "Vérifiez le nom du dossier avant chaque tâche importante. Si vous changez de client, changez aussi le dossier ou le contexte.", "La tâche démarre dans le bon QG.", "Pour un client A, ne laissez pas le dossier du client B actif."),
            section("Le plus dans l’interface", "08:07", 7, "Le formateur utilise le bouton plus pour accéder aux fichiers, compétences, connecteurs et plugins. Ce bouton devient une porte d’entrée vers les ressources de Cowork.", "Repérez ce bouton dès le début. Il sert à ajouter du contexte ou à connecter un outil sans quitter l’espace de travail.", "Vous savez ouvrir le menu et retrouver connecteurs, compétences et plugins.", "Si Cowork n’a pas accès à une donnée, commencez par ce menu."),
            section("Le panneau de progression", "12:00", 13, "Quand une tâche démarre, Cowork affiche une progression. Le formateur montre qu’il s’organise en étapes et que l’on peut voir ce qu’il tente de faire.", "Pendant une tâche longue, regardez la progression au lieu d’attendre sans comprendre. Cela permet de voir si Cowork travaille sur la bonne action.", "La progression correspond à la demande donnée.", "Si la progression part dans une mauvaise direction, stoppez ou corrigez."),
            section("Les logs et les actions", "12:08", 14, "Cowork montre les actions et les outils utilisés. Dans l’exemple Calendar, on voit qu’il prépare puis crée des événements.", "Lisez les actions avant de valider une permission sensible. Les logs expliquent ce que Cowork est en train de faire.", "Vous comprenez quelle action est en cours.", "Créer un événement Calendar n’est pas la même chose que lire le calendrier."),
            section("La validation humaine", "12:31", 13, "Au moment de créer les événements, Cowork demande une autorisation. C’est une étape importante : l’agent ne doit pas agir sans votre accord quand il touche à un outil réel.", "Autorisez seulement si l’action correspond à votre demande. Refusez si l’outil ou la donnée ne sont pas les bons.", "Aucune action externe sensible ne part sans validation.", "Avant d’autoriser, posez-vous : qu’est-ce qui sera créé, modifié ou envoyé ?"),
            section("La réponse finale", "12:57", 15, "Après l’exécution, Cowork annonce ce qu’il a fait. Le formateur vérifie ensuite le résultat dans Google Calendar.", "Ne vous arrêtez pas au message de succès. Ouvrez l’outil cible et vérifiez que le résultat existe vraiment.", "Le résultat est visible hors de Cowork.", "Pour Calendar, ouvrez la semaine concernée et regardez les événements."),
            section("Le contexte latéral", "13:00", 14, "Le panneau latéral peut montrer le dossier, les instructions et les connecteurs utilisés. Cela aide à comprendre pourquoi Cowork prend une décision.", "Gardez un œil sur le contexte. Si un connecteur manque, la tâche peut échouer ou partir sur une solution de remplacement.", "Le connecteur attendu apparaît dans le contexte.", "Pour une tâche Calendar, Google Calendar doit être visible comme connecteur."),
            section("La logique d’une tâche Cowork", "03:57", 13, "La vidéo résume la méthode : décrire le résultat, laisser Cowork planifier, puis vérifier le résultat. C’est simple, mais ça demande une demande claire.", "Structurez vos prompts avec quatre lignes : contexte, tâche, format attendu, limite. Cette structure évite les demandes trop vagues.", "Cowork sait quoi faire, dans quel outil et sous quel format.", "Prompt court : planifie ma semaine de prospection dans Google Calendar avec ces créneaux."),
        ],
    ),
    (
        "Acte 4 - Les connecteurs comme centre de la séance",
        "Le passage central de la vidéo montre que Cowork prend sa valeur quand il peut accéder aux outils utilisés tous les jours.",
        "Connecteurs",
        "violet",
        [
            section("Le menu connecteurs", "08:11", 7, "Le formateur ouvre les connecteurs depuis le bouton plus. C’est ici que Cowork peut accéder aux outils externes.", "Ouvrez le menu, choisissez Connecteurs, puis vérifiez la liste des outils déjà activés.", "Les connecteurs utiles sont visibles dans le menu.", "Le bon réflexe : regarder les connecteurs avant de demander une action externe."),
            section("Le répertoire", "08:24", 8, "Le répertoire contient de nombreux connecteurs. Le formateur cite plusieurs usages : déployer, chercher du SEO, gérer des bases, planifier, récupérer des informations.", "Parcourez le répertoire sans tout installer. Cherchez d’abord les outils que vous utilisez vraiment dans votre business.", "La liste des connecteurs n’est pas confondue avec une liste d’objectifs.", "Un connecteur doit répondre à un besoin réel, pas à une curiosité."),
            section("Les connecteurs officiels", "03:53", 8, "La vidéo parle des connecteurs officiels d’Anthropic. Ils simplifient la connexion aux outils connus, comme Google Calendar ou Drive.", "Privilégiez un connecteur officiel quand il existe. Il sera généralement plus simple à connecter et à maintenir.", "Le connecteur vient d’une source de confiance.", "Pour Calendar, utilisez le connecteur Google Calendar officiel."),
            section("Les connecteurs personnalisés", "09:16", 10, "Le formateur montre aussi la possibilité d’ajouter un connecteur personnalisé. Il explique que cela passe par MCP, avec un serveur distant et une clé ou un accès.", "Utilisez cette option seulement quand aucun connecteur officiel ne couvre votre besoin. Notez le nom, l’URL du serveur MCP et les accès nécessaires.", "Le connecteur personnalisé a un nom clair et une URL correcte.", "Exemple vu dans la logique : ajouter Papers via un serveur MCP.", link="mcp"),
            section("MCP en mots simples", "09:58", 10, "Dans la séance, MCP est expliqué comme un serveur qui relie Cowork à l’application cible. L’idée à retenir : MCP donne des outils à Claude pour agir avec un service.", "Ne cherchez pas à retenir tout le protocole au début. Retenez l’usage : connecter un outil externe à Cowork avec des actions contrôlées.", "Vous savez expliquer MCP sans phrase technique compliquée.", "Phrase simple : MCP permet à Claude d’utiliser un outil externe de façon structurée.", link="mcp"),
            section("Les permissions", "10:58", 11, "Quand Google demande des droits, le formateur accepte les accès nécessaires. Ce passage rappelle que les connecteurs donnent de vrais pouvoirs à Cowork.", "Lisez toujours les permissions. Si un outil peut lire, modifier ou créer, vous devez savoir pourquoi.", "Les permissions correspondent au besoin de la tâche.", "Pour Calendar, créer des événements demande plus qu’une simple lecture."),
            section("La connexion Calendar", "10:26", 11, "Le formateur connecte Google Calendar depuis le répertoire, choisit le compte puis valide. Après la redirection, le connecteur apparaît comme connecté.", "Connectez le bon compte. Un mauvais compte crée des événements au mauvais endroit et rend la vérification confuse.", "Google Calendar apparaît bien comme connecté.", "Si plusieurs comptes existent, vérifiez l’adresse avant de continuer."),
            section("La liste des connecteurs actifs", "09:44", 9, "Dans les paramètres, on voit les connecteurs actifs : Drive, Calendar, Notion, Claude in Chrome et d’autres. Cette page sert à contrôler l’état des connexions.", "Ouvrez Paramètres puis Connecteurs pour voir ce qui est connecté, configurer ou déconnecter.", "La liste correspond aux outils que vous voulez vraiment utiliser.", "Supprimez ou déconnectez ce qui n’a plus de rôle."),
            section("Déconnecter ce qui ne sert pas", "17:00", 9, "La vidéo montre l’idée de retirer un connecteur qui ne sert pas. Ce n’est pas obligatoire, mais c’est sain pour garder un environnement lisible.", "Nettoyez les connecteurs inutiles. Moins d’accès veut dire moins de confusion et moins de risque.", "Les connecteurs actifs sont utiles et compris.", "Si vous n’utilisez pas un connecteur, il n’a pas besoin d’être actif."),
            section("Adapter les outils au business", "08:31", 8, "Le formateur cite plusieurs usages possibles : Calendly pour les rendez-vous, Gmail pour les mails, Clay pour la prospection, Drive pour les fichiers. Le bon connecteur dépend du business.", "Faites une carte de vos outils : vente, livraison, documents, rendez-vous, suivi. Choisissez un connecteur par zone importante.", "Chaque zone du business a un outil clair.", "Vente : Gmail ou CRM. Organisation : Calendar. Documents : Drive ou Notion."),
        ],
    ),
    (
        "Acte 5 - L’exercice Google Calendar",
        "La démonstration principale consiste à demander à Cowork de planifier une semaine de prospection dans Google Calendar.",
        "Calendar",
        "green",
        [
            section("L’objectif de l’exercice", "07:57", 13, "Le formateur annonce un exercice simple : planifier une semaine. Le but n’est pas Calendar en lui-même. Le but est de voir Cowork agir avec un connecteur réel.", "Choisissez une tâche simple pour le premier test. Une tâche simple permet de vérifier le connecteur sans risque inutile.", "La tâche est claire et vérifiable.", "Créer cinq événements est plus facile à contrôler qu’une demande trop large."),
            section("Le prompt de planification", "11:30", 13, "La demande donnée à Cowork précise la semaine de prospection, les créneaux, les sujets et l’idée de couleurs différentes. C’est un prompt concret, pas une question vague.", "Donnez les jours, horaires, titres et descriptions. Plus la demande est précise, plus le résultat est contrôlable.", "Le prompt contient toutes les informations nécessaires.", "Exemple : lundi 9h-10h30 production client, mardi 14h appel découverte, etc."),
            section("Limiter les connecteurs utilisés", "11:46", 12, "L’interface affiche plusieurs connecteurs, mais le formateur précise que l’exercice n’a besoin que de Google Calendar.", "Quand une tâche ne demande qu’un outil, dites-le. Cela évite que Cowork cherche dans Drive, Notion ou d’autres outils sans raison.", "Le connecteur utile est bien celui utilisé.", "Phrase pratique : pour cette tâche, utilise seulement Google Calendar."),
            section("La progression en étapes", "12:00", 14, "Cowork décompose l’action en étapes. On voit la progression : créer les événements, vérifier, avancer dans la liste.", "Pendant la tâche, surveillez la progression. C’est le meilleur moyen de voir si l’agent comprend le plan.", "Les étapes affichées correspondent au résultat demandé.", "Si la progression annonce une action non prévue, arrêtez et corrigez."),
            section("L’authentification", "12:31", 13, "Au moment d’agir, Cowork demande une autorisation. Cela montre que l’agent passe par un outil réel, avec une action réelle.", "Ne cliquez pas automatiquement sur Autoriser. Vérifiez le connecteur, l’action et le compte.", "L’autorisation correspond à la création d’événements attendue.", "Autoriser une création Calendar est logique ici, mais pas pour supprimer des fichiers."),
            section("La création des événements", "12:39", 14, "Cowork crée les événements demandés. Dans la vidéo, il travaille sur plusieurs créneaux de la semaine.", "Après la création, attendez la fin de la tâche. Ne relancez pas une demande identique pendant que Cowork travaille.", "La progression arrive au bout sans erreur bloquante.", "Une demande répétée peut créer des doublons dans le calendrier."),
            section("La vérification dans Google Calendar", "13:05", 15, "Le formateur ouvre Google Calendar pour vérifier que les événements existent bien. C’est une étape essentielle : le message de Cowork ne suffit pas.", "Ouvrez Calendar sur le bon compte et la bonne semaine. Vérifiez les jours, heures, titres et descriptions.", "Les événements sont visibles et cohérents.", "Contrôle rapide : lundi, mardi, mercredi, jeudi, vendredi."),
            section("La correction possible", "15:51", 15, "La vidéo évoque la possibilité de demander à Cowork de supprimer une tâche ou un événement. Cela montre que l’agent peut aussi corriger ou modifier.", "Pour une correction, soyez précis : quel événement, quelle date, quel changement. Évitez `corrige ça` sans contexte.", "La correction touche seulement l’élément visé.", "Demande claire : supprime l’événement de mardi 14h dans Google Calendar."),
            section("Le risque des doublons", "13:22", 14, "Quand un agent crée plusieurs événements, le risque principal est de créer deux fois la même chose ou de choisir la mauvaise semaine.", "Avant de relancer une tâche, vérifiez si une partie existe déjà. Demandez à Cowork de lire avant de créer si vous avez un doute.", "Aucun doublon n’apparaît dans le calendrier.", "Commande prudente : vérifie d’abord si ces événements existent déjà."),
            section("Le vrai apprentissage", "13:33", 15, "L’exercice Calendar montre la logique complète : connecter un outil, donner un prompt précis, autoriser, suivre, puis vérifier. Cette méthode servira pour Notion, Drive, Gmail ou d’autres outils.", "Gardez ce modèle comme base. Chaque nouveau connecteur doit passer par le même cycle.", "Le cycle est compris et reproductible.", "Connecter, demander, autoriser, vérifier, documenter."),
        ],
    ),
    (
        "Acte 6 - Notion, Drive et documents",
        "Après Calendar, la séance montre que Cowork peut aussi produire des pages, travailler avec Drive et créer des documents dans le dossier.",
        "Documents",
        "orange",
        [
            section("La suite avec Notion", "13:39", 15, "Après les événements Calendar, le formateur demande de créer une page Notion avec le même contenu. Il rappelle qu’il faut connecter Notion comme Calendar.", "Connectez Notion avant de demander une création. Le système reste le même : connecteur, autorisation, tâche, vérification.", "Notion est connecté avant la demande.", "Sans connecteur Notion, Cowork peut proposer une autre solution mais ne pourra pas créer directement dedans."),
            section("Créer un récap visuel", "14:47", 15, "Le résultat Notion sert à avoir une vue propre de la semaine. Le formateur insiste sur le côté visuel et organisé.", "Demandez un format clair : titre, semaine, tableau, checklist, prochaines actions.", "Le récap peut être relu rapidement.", "Une page de suivi doit aider à agir, pas seulement faire joli."),
            section("Centraliser les sorties", "14:20", 15, "Le formateur revient sur le besoin de centraliser : planifier, créer, résumer et garder les informations dans une même app ou un même QG.", "Quand Cowork produit quelque chose, décidez où cette sortie doit vivre : Calendar, Notion, Drive ou dossier local.", "Chaque sortie a une destination claire.", "Un résumé client sans destination finit souvent oublié."),
            section("Le connecteur Drive", "16:13", 9, "La vidéo montre ensuite l’idée d’utiliser Drive pour retrouver ou créer des informations. Le formateur tente de gérer le connecteur et montre qu’un problème peut arriver.", "Si Drive ne répond pas comme prévu, ne forcez pas. Vérifiez le compte connecté, les droits et la disponibilité des documents.", "Le problème est identifié avant de changer de stratégie.", "Si le Drive est vide ou mal connecté, Cowork ne peut pas inventer les fichiers."),
            section("Le bug comme apprentissage", "18:26", 9, "Le formateur montre une difficulté en live. C’est utile : les connecteurs ne marchent pas toujours parfaitement du premier coup.", "Quand une erreur arrive, gardez une méthode : lire le message, vérifier le compte, vérifier les droits, tester une demande plus simple.", "La correction suit une logique, pas des clics au hasard.", "Test simple : liste les fichiers récents du Drive connecté."),
            section("La solution alternative", "18:36", 15, "Cowork propose parfois une autre façon de faire si un connecteur bloque. Cela peut aider, mais il faut garder le besoin initial en tête.", "Acceptez une solution alternative seulement si elle répond au besoin. Sinon, revenez au connecteur attendu.", "La solution ne remplace pas l’objectif sans raison.", "Si le besoin est un fichier Drive, un texte dans le chat ne suffit pas."),
            section("La création de document", "19:18", 15, "La vidéo montre que Cowork peut créer un document, installer un package et produire un fichier dans le dossier. Cela rejoint l’idée de QG local.", "Pour un document local, demandez le nom du fichier, le format et l’endroit où l’enregistrer.", "Le fichier existe dans le dossier QG.", "Exemple : crée un document de récap de la semaine de prospection dans le QG."),
            section("Le rôle du dossier local", "20:42", 6, "Une fois le document créé dans le dossier, une prochaine session peut retrouver ce contenu. C’est exactement l’intérêt du QG.", "Gardez les documents importants dans le dossier relié à Cowork. Cela donne une mémoire de travail simple.", "Le fichier peut être réutilisé dans une autre demande.", "Nouvelle demande : relis le document de prospection et propose les prochaines actions."),
            section("Les photos et fichiers", "21:07", 12, "Cowork permet d’ajouter des fichiers ou des photos, mais le formateur précise que ce n’est pas le plus important dans cette séance.", "Utilisez l’ajout de fichiers quand cela sert la tâche. N’ajoutez pas des documents sans objectif.", "Le fichier ajouté est utile à la demande.", "Un fichier de brief client sert. Une capture sans contexte sert moins."),
            section("La règle de destination", "20:51", 15, "La séance montre plusieurs destinations : Calendar pour les événements, Notion pour la page, dossier local pour les documents. C’est la base d’une organisation saine.", "Avant chaque prompt, décidez la destination finale. Cowork doit savoir où le résultat doit apparaître.", "Le résultat final est au bon endroit.", "Demande complète : crée les événements dans Calendar et un récap dans le dossier QG."),
        ],
    ),
    (
        "Acte 7 - Compétences et plugins",
        "La fin de la séance ouvre la porte aux compétences et plugins, sans chercher à tout maîtriser tout de suite.",
        "Compétences",
        "blue",
        [
            section("La partie compétences", "21:14", 16, "Le formateur explique que les compétences sont très utiles. Elles ressemblent à des fichiers Markdown qui donnent plus de contexte et de méthode à Claude.", "Ouvrez le répertoire des compétences pour comprendre la logique. Une compétence sert à guider Claude sur une tâche précise.", "Vous savez distinguer connecteur, compétence et plugin.", "Connecteur = accès outil. Compétence = méthode. Plugin = capacité ajoutée."),
            section("Le lien avec les fichiers MD", "21:19", 16, "La séance relie les compétences aux fichiers `.md` vus plus tôt. Le principe reste le même : donner un contexte structuré pour améliorer le comportement de l’agent.", "Quand une méthode revient souvent, transformez-la en consigne écrite. Claude comprendra mieux un fichier clair qu’une demande improvisée.", "La consigne est stable et réutilisable.", "Exemple : une compétence pour comparer deux solutions client."),
            section("Les exemples de skills", "21:29", 16, "Dans l’interface, on voit des fichiers comme comparator, grader ou d’autres éléments. Le formateur explique que cela permet d’analyser, comparer et évaluer.", "Utilisez une compétence quand la tâche demande une méthode répétable : analyse, comparaison, rédaction, audit, génération de document.", "La compétence correspond à la tâche demandée.", "Une compétence d’analyse ne doit pas servir à écrire un email commercial."),
            section("Ne pas tout ouvrir trop tôt", "21:57", 16, "Le formateur prévient que certaines parties seront vues plus tard pour ne pas perdre le fil. C’est important : trop d’options au début crée de la confusion.", "Explorez doucement. Pour cette séance, retenez surtout QG, dossier, connecteurs, Calendar et compétences.", "Les bases sont comprises avant les options avancées.", "Si une option ne sert pas l’exercice actuel, notez-la pour plus tard."),
            section("Les compétences design et MCP", "21:47", 16, "La vidéo mentionne des compétences autour du design, du MCP builder, des thèmes ou de la documentation. Ce sont des pistes futures.", "Ne mélangez pas tout. MCP côté connecteur et compétence côté méthode sont deux notions différentes.", "La différence reste claire.", "MCP connecte un outil. Une compétence donne une façon de travailler."),
            section("La partie plugins", "22:02", 16, "Le formateur montre aussi les plugins, avec l’idée d’ajouter des capacités comme créer ou voir un PDF.", "Installez un plugin seulement si une tâche le demande. Un plugin inutile ajoute de la complexité.", "Le plugin installé a un usage précis.", "Besoin PDF : plugin document. Besoin planning : connecteur Calendar."),
            section("Le plugin productivité", "22:12", 16, "La vidéo montre une zone productivité et un plugin lié à la gestion des tâches. Le formateur souligne l’intérêt pour l’organisation.", "Pour un QG business, les capacités de tâches, documents et suivi sont souvent prioritaires.", "Le plugin renforce l’organisation, pas la décoration.", "Un bon plugin aide à suivre une livraison ou un plan d’action."),
            section("Installer puis gérer", "22:15", 16, "Le formateur montre le bouton installer puis gérer. Cela signifie qu’un ajout doit ensuite être configuré ou compris.", "Après installation, ouvrez la gestion du plugin. Lisez son rôle avant de l’utiliser.", "Le plugin est installé, configuré et compris.", "Ne cliquez pas partout sans savoir ce que l’outil va faire."),
            section("La description compte", "22:24", 16, "L’interface affiche une description. Elle explique ce que le plugin ou la compétence sait faire.", "Lisez la description comme un contrat. Si la description ne correspond pas au besoin, ne l’utilisez pas.", "L’usage est aligné avec la description.", "Une description de gestion de tâches ne sert pas à résumer une réunion."),
            section("La suite de la formation", "22:37", 16, "Le formateur explique que Cowork sera revu plus en détail. Cette séance donne les bases théoriques et quelques exercices pour mettre la main sur l’outil.", "Gardez cette séance comme une mise en place. Les usages plus profonds viendront quand les projets clients commenceront.", "Les bases sont prêtes pour les prochaines séances.", "À ce stade : installer, choisir un QG, connecter, tester, vérifier."),
        ],
    ),
    (
        "Acte 8 - La méthode à garder",
        "La conclusion de la vidéo rappelle que le début peut sembler dense, mais la méthode sert à livrer des projets clients de manière organisée.",
        "Méthode",
        "green",
        [
            section("Le bon rythme de départ", "22:44", 3, "Le formateur explique que l’acte 1 donne de la théorie et des exercices courts. Le but est de pouvoir suivre ensuite quand la formation devient plus pratique.", "Ne cherchez pas à tout maîtriser en une journée. Faites les exercices simples et vérifiez que chaque base fonctionne.", "Les bases sont testées, pas seulement lues.", "Exercice minimal : ouvrir Cowork, choisir le QG, connecter Calendar, créer un événement test."),
            section("La difficulté normale", "23:03", 3, "La vidéo reconnaît que le début peut être compliqué parce que les outils sont nouveaux : Claude Code, Codex, Cowork, connecteurs et organisation.", "Acceptez que la première prise en main demande du temps. Ce qui compte, c’est de suivre la méthode étape par étape.", "La difficulté ne bloque pas l’action suivante.", "Si un point bloque, revenez au dernier élément qui fonctionnait."),
            section("Pas besoin de savoir coder au départ", "23:29", 3, "Le formateur insiste : même sans savoir coder, il sera possible de livrer des projets clients si la méthode est suivie.", "Concentrez-vous sur la compréhension du besoin client, la structure du dossier, le prompt et la vérification du résultat.", "Le travail avance même sans écrire de code.", "Une bonne demande et un bon contrôle valent mieux qu’un outil lancé sans méthode."),
            section("La vision 30-60-90 jours", "24:02", 3, "La conclusion parle d’un changement progressif sur 30, 60, 90 jours. Cowork fait partie d’un système d’apprentissage et d’exécution.", "Transformez la séance en routine : une action simple maintenant, puis une amélioration chaque semaine.", "Une progression réelle est visible dans l’organisation.", "Jour 1 : QG. Jour 30 : dossiers clients. Jour 60 : connecteurs. Jour 90 : livraison fluide."),
            section("La routine QG", "06:56", 6, "Le QG doit devenir un réflexe. Chaque nouveau projet, document ou compte rendu doit avoir une place.", "Créez une routine : ranger le document, demander le résumé, extraire les actions, mettre à jour le suivi.", "Le QG reste propre après plusieurs projets.", "Routine après un call : transcript, résumé, actions, prochaine date."),
            section("La routine connecteurs", "08:11", 7, "Les connecteurs doivent être utilisés selon la tâche. On ne connecte pas tout pour faire joli.", "Avant une demande, dites quel connecteur doit être utilisé. Après la demande, vérifiez l’outil cible.", "Le connecteur utilisé est volontaire.", "Pour un planning, Calendar. Pour un document, Drive ou dossier local. Pour une base, Notion."),
            section("La routine vérification", "12:57", 15, "Chaque action externe doit être vérifiée. Le formateur le fait avec Google Calendar après la création des événements.", "Vérifiez dans l’outil réel, puis corrigez si besoin. Ne laissez pas Cowork être le seul juge de son résultat.", "Le résultat existe et correspond à la demande.", "Une réponse de succès ne remplace pas un contrôle dans Calendar."),
            section("La routine de prompt", "11:30", 13, "Le prompt de l’exercice Calendar est précis. Il donne les événements, les jours, les heures et le contexte de prospection.", "Utilisez un format stable : objectif, données, outil, format de sortie, limite.", "Le prompt ne laisse pas Cowork deviner l’essentiel.", "Objectif : planifier. Données : créneaux. Outil : Calendar. Limite : ne pas toucher aux autres événements."),
            section("Le résumé à retenir", "22:32", 3, "Cowork sert à organiser, connecter, créer, planifier et centraliser. Ce n’est pas un remplacement de Claude Code ou Codex, c’est la couche QG du business.", "Quand vous hésitez, revenez à cette phrase : Cowork organise le travail autour des outils et du dossier.", "Le rôle de Cowork reste clair.", "Cowork = QG. Claude Code = construction. Codex = délégation. n8n = automatisation visuelle."),
            section("Checklist finale", "24:16", 16, "La séance se termine en invitant à suivre les modules suivants. Avant de continuer, il faut que les bases Cowork soient prêtes.", "Validez la checklist : Claude Desktop installé, Cowork ouvert, dossier QG créé, dossier connecté, Calendar testé, connecteurs compris, compétences repérées.", "La suite peut commencer sans repartir de zéro.", "Si un élément manque, corrigez-le avant de passer à une séance plus pratique."),
        ],
    ),
]


def e(text: object) -> str:
    return escape(str(text), quote=True)


def flat_sections() -> list[dict[str, str | int]]:
    output: list[dict[str, str | int]] = []
    for chapter_i, (chapter, intro, tag, color, items) in enumerate(CHAPTERS, start=1):
        for item_i, item in enumerate(items, start=1):
            merged = dict(item)
            merged["chapter"] = chapter
            merged["chapter_intro"] = intro
            merged["tag"] = tag
            merged["color"] = color
            merged["chapter_i"] = chapter_i
            merged["item_i"] = item_i
            output.append(merged)
    return output


def badge(text: str, color: str) -> str:
    colors = {
        "blue": "bg-blue-600 text-white",
        "violet": "bg-violet-600 text-white",
        "cyan": "bg-cyan-400 text-slate-950",
        "green": "bg-emerald-400 text-slate-950",
        "orange": "bg-orange-400 text-slate-950",
    }
    return f'<span class="border-2 border-slate-950 px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] shadow-neo-sm {colors[color]}">{e(text)}</span>'


def image_src(image_index: int) -> str:
    return f"img/session-04/{IMAGES[image_index - 1]}"


def image_card(section_data: dict[str, str | int], number: int) -> str:
    src = image_src(int(section_data["image"]))
    return f"""
      <figure class="group min-w-0 overflow-hidden border-2 border-slate-950 bg-white shadow-neo">
        <img src="{src}" alt="{e(section_data['title'])}" loading="lazy" class="aspect-video w-full bg-white object-contain transition duration-300 group-hover:scale-[1.015]">
        <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold leading-6 text-slate-700">
          Visuel {number:02d} · extrait de la séance · {e(section_data['moment'])}
        </figcaption>
      </figure>
    """


def info_card(label: str, text: object, color: str) -> str:
    colors = {
        "blue": "bg-blue-50 text-blue-700",
        "violet": "bg-violet-50 text-violet-700",
        "cyan": "bg-cyan-50 text-cyan-700",
        "green": "bg-emerald-50 text-emerald-700",
        "orange": "bg-orange-50 text-orange-700",
        "white": "bg-white text-slate-500",
    }
    return f"""
      <div class="border-2 border-slate-950 {colors[color].split()[0]} p-5 shadow-neo-sm">
        <p class="font-mono text-xs font-black uppercase tracking-[.16em] {colors[color].split()[1]}">{e(label)}</p>
        <p class="mt-3 leading-8 text-slate-800">{e(text)}</p>
      </div>
    """


def section_html(section_data: dict[str, str | int], number: int) -> str:
    variant = number % 5
    link = DOCS[str(section_data["link"])]
    source_link = f"""
      <a href="{link}" target="_blank" rel="noreferrer" class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-blue-700 shadow-neo-sm transition hover:-translate-y-0.5">Source</a>
    """
    intro = f"""
      <div class="flex flex-wrap items-center gap-3">
        {badge(str(section_data['tag']), str(section_data['color']))}
        <span class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] shadow-neo-sm">{number:02d}</span>
        <span class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-slate-500 shadow-neo-sm">{e(section_data['moment'])}</span>
        {source_link}
      </div>
      <h2 class="mt-6 max-w-4xl text-4xl font-black leading-[1.02] tracking-normal text-slate-950 md:text-6xl">{e(section_data['title'])}</h2>
      <p class="mt-5 text-lg leading-8 text-slate-700">{e(section_data['why'])}</p>
    """
    action = info_card("Ce que vous faites", section_data["action"], "violet")
    check = info_card("Comment vérifier", section_data["check"], "cyan")
    example = info_card("Exemple terrain", section_data["example"], "blue")
    recap = f"""
      <div class="mt-6 border-2 border-slate-950 bg-slate-950 p-5 text-white shadow-neo">
        <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-cyan-200">À retenir</p>
        <p class="mt-3 leading-8">Cette section reprend le passage vidéo autour de {e(section_data['moment'])}. Le but est de garder une action simple, vérifiable et réutilisable dans votre QG.</p>
      </div>
    """
    img = image_card(section_data, number)
    if variant == 1:
        body = f"""
          <div class="grid gap-8 lg:grid-cols-[.95fr_1.05fr] lg:items-start">
            <div>{intro}{action}{recap}</div>
            <div>{img}{check}{example}</div>
          </div>
        """
    elif variant == 2:
        body = f"""
          <div class="grid gap-8 lg:grid-cols-[1.05fr_.95fr] lg:items-start">
            <div>{intro}{check}{example}</div>
            <div>{img}{action}</div>
          </div>
        """
    elif variant == 3:
        body = f"""
          <div>{intro}{img}
            <div class="mt-8 grid gap-5 md:grid-cols-3">{action}{check}{example}</div>
          </div>
        """
    elif variant == 4:
        body = f"""
          <div class="grid gap-8 lg:grid-cols-2 lg:items-start">
            <div>{img}{recap}</div>
            <div>{intro}{action}{check}{example}</div>
          </div>
        """
    else:
        body = f"""
          <div>{intro}
            <div class="mt-8 grid gap-6 lg:grid-cols-[.9fr_1.1fr] lg:items-start">
              <div>{action}{check}{example}</div>
              <div>{img}{recap}</div>
            </div>
          </div>
        """
    return f"""
    <section id="section-{number:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {body}
    </section>
    """


def chapter_nav() -> str:
    cards = ""
    for i, (chapter, intro, tag, color, _) in enumerate(CHAPTERS, start=1):
        start = (i - 1) * 10 + 1
        end = i * 10
        cards += f"""
          <a href="#section-{start:02d}" class="group border-2 border-slate-950 bg-white p-5 shadow-neo transition hover:-translate-y-1 hover:bg-blue-50">
            <div class="flex items-center justify-between gap-4">
              {badge(tag, color)}
              <span class="font-mono text-xs font-black text-slate-500">{start:02d}-{end:02d}</span>
            </div>
            <h3 class="mt-5 text-2xl font-black leading-tight text-slate-950">{e(chapter.replace(' - ', ' · '))}</h3>
            <p class="mt-3 text-sm leading-7 text-slate-600">{e(intro)}</p>
          </a>
        """
    return f"""
      <section class="mx-auto max-w-7xl bg-white px-4 py-12 sm:px-6 lg:px-8">
        <div class="grid gap-5 md:grid-cols-2 xl:grid-cols-4">{cards}</div>
      </section>
    """


def sources_table() -> str:
    rows = [
        ("Transcription de la séance", DOCS["transcription"], "Transcription locale horodatée utilisée pour construire le support."),
        ("Claude Download", DOCS["download"], "Téléchargement officiel de Claude Desktop."),
        ("Claude Help Center", DOCS["support"], "Support officiel pour Claude, Desktop, connecteurs et paramètres."),
        ("Custom connectors MCP", DOCS["mcp"], "Documentation officielle sur les connecteurs personnalisés via MCP."),
    ]
    body = ""
    cards = ""
    for name, url, desc in rows:
        body += f"""
          <tr>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 font-bold">{e(name)}</td>
            <td class="border-2 border-slate-950 bg-white px-4 py-3"><a class="font-semibold text-blue-700 underline decoration-2 underline-offset-4" href="{url}" target="_blank" rel="noreferrer">{e(url)}</a></td>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 text-slate-700">{e(desc)}</td>
          </tr>
        """
        cards += f"""
          <article class="source-card min-w-0 w-full border-2 border-slate-950 bg-white p-4 shadow-neo-sm">
            <h3 class="text-lg font-black text-slate-950">{e(name)}</h3>
            <p class="mt-2 text-sm leading-6 text-slate-700">{e(desc)}</p>
            <a class="mt-3 block break-all text-sm font-bold text-blue-700 underline decoration-2 underline-offset-4" href="{url}" target="_blank" rel="noreferrer">{e(url)}</a>
          </article>
        """
    return f"""
      <section id="sources" class="mx-auto max-w-7xl bg-white px-4 py-16 sm:px-6 lg:px-8">
        <div class="border-2 border-slate-950 bg-white p-6 shadow-neo">
          <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-violet-700">Sources</p>
          <h2 class="mt-4 text-4xl font-black text-slate-950">Liens et transcription</h2>
          <div class="source-card-list mt-6 grid grid-cols-1 gap-4 sm:hidden">{cards}</div>
          <div class="mt-6 hidden overflow-x-auto sm:block">
            <table class="min-w-[850px] border-collapse text-sm">{body}</table>
          </div>
        </div>
      </section>
    """


def render() -> str:
    sections = flat_sections()
    section_markup = "\n".join(section_html(item, i) for i, item in enumerate(sections, start=1))
    return f"""<!doctype html>
<html lang="fr" class="scroll-smooth">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>DENEM Academy · Séance 4 · Claude Cowork</title>
    <meta name="description" content="Support technique séance 4 : Claude Cowork, QG d’organisation, dossiers, connecteurs, Calendar, Drive, Notion, compétences et plugins.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" href="logo-denem.jpeg">
    <link rel="stylesheet" href="assets/tailwind-s4.css?v=20260604">
    <style>
      :root {{ color-scheme: light; }}
      * {{ box-sizing: border-box; }}
      body {{ margin: 0; background: #fff; color: #0f172a; font-family: Inter, system-ui, sans-serif; letter-spacing: 0; }}
      .reveal {{ opacity: 0; transform: translateY(20px); transition: opacity .6s ease, transform .6s ease; }}
      .reveal.in-view {{ opacity: 1; transform: translateY(0); }}
      .shadow-neo {{ box-shadow: 8px 8px 0 #0f172a; }}
      .shadow-neo-sm {{ box-shadow: 4px 4px 0 #0f172a; }}
      .progress {{ transform-origin: left; transform: scaleX(0); }}
      .section-block:nth-child(odd) {{ background-image: linear-gradient(90deg, rgba(37,99,235,.045) 0 1px, transparent 1px), linear-gradient(rgba(124,58,237,.035) 0 1px, transparent 1px); background-size: 34px 34px; }}
      .source-card-list {{ grid-template-columns: minmax(0, 1fr); }}
      .source-card {{ width: 100%; max-width: 100%; min-width: 0; overflow: hidden; }}
      .source-card a {{ overflow-wrap: anywhere; word-break: break-word; }}
      @media (prefers-reduced-motion: reduce) {{ .reveal {{ opacity: 1; transform: none; transition: none; }} * {{ scroll-behavior: auto !important; }} }}
    </style>
  </head>
  <body class="bg-white">
    <div class="progress fixed left-0 top-0 z-[70] h-1 w-full bg-gradient-to-r from-blue-600 via-violet-600 to-cyan-500" id="progress"></div>
    <nav class="sticky top-0 z-50 border-b-2 border-slate-950 bg-white/95 backdrop-blur">
      <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-3 sm:px-6 lg:px-8">
        <a href="#" class="flex items-center gap-3">
          <img src="logo-denem.jpeg" alt="DENEM Academy" class="h-9 w-9 border-2 border-slate-950 object-cover shadow-neo-sm">
          <span class="text-sm font-black uppercase tracking-[.18em] text-slate-950">DENEM Academy</span>
        </a>
        <div class="hidden items-center gap-2 md:flex">
          <a class="border-2 border-slate-950 bg-blue-600 px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-white shadow-neo-sm" href="#section-01">Départ</a>
          <a class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-slate-950 shadow-neo-sm" href="#sources">Sources</a>
        </div>
      </div>
    </nav>

    <header class="relative overflow-hidden border-b-2 border-slate-950 bg-white">
      <div class="mx-auto grid min-h-[82vh] max-w-7xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-[1fr_.9fr] lg:items-center lg:px-8">
        <div>
          <div class="flex flex-wrap gap-3">
            {badge('Séance 04', 'blue')}
            {badge('Claude Cowork', 'violet')}
            {badge('QG business', 'cyan')}
          </div>
          <h1 class="mt-8 text-5xl font-black leading-[.95] tracking-normal text-slate-950 md:text-7xl">
            Claude Cowork comme QG d’organisation
          </h1>
          <p class="mt-6 max-w-2xl text-xl leading-9 text-slate-700">
            Cette séance montre comment utiliser Claude Desktop et Cowork pour centraliser le travail : dossier QG, connecteurs, Google Calendar, Notion, Drive, compétences et plugins.
          </p>
          <div class="mt-8 border-2 border-slate-950 bg-violet-50 p-5 shadow-neo">
            <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-violet-700">Fil rouge</p>
            <p class="mt-3 leading-8 text-slate-800">Une personne seule veut organiser son business et ses projets clients. Elle crée un QG, connecte ses outils, planifie une semaine de prospection, vérifie le résultat et prépare la suite de la formation.</p>
          </div>
          <div class="mt-6 grid gap-3 sm:grid-cols-2">
            <div class="border-2 border-slate-950 bg-white p-4 shadow-neo-sm"><p class="font-mono text-[11px] font-black uppercase tracking-[.14em] text-blue-700">1 · Installer</p><p class="mt-2 text-sm font-semibold leading-6 text-slate-700">Passer par Claude Desktop et ouvrir l’onglet Cowork.</p></div>
            <div class="border-2 border-slate-950 bg-white p-4 shadow-neo-sm"><p class="font-mono text-[11px] font-black uppercase tracking-[.14em] text-violet-700">2 · Organiser</p><p class="mt-2 text-sm font-semibold leading-6 text-slate-700">Créer un dossier QG pour les projets et documents.</p></div>
            <div class="border-2 border-slate-950 bg-white p-4 shadow-neo-sm"><p class="font-mono text-[11px] font-black uppercase tracking-[.14em] text-cyan-700">3 · Connecter</p><p class="mt-2 text-sm font-semibold leading-6 text-slate-700">Brancher Calendar, Drive, Notion ou un connecteur MCP.</p></div>
            <div class="border-2 border-slate-950 bg-white p-4 shadow-neo-sm"><p class="font-mono text-[11px] font-black uppercase tracking-[.14em] text-emerald-700">4 · Vérifier</p><p class="mt-2 text-sm font-semibold leading-6 text-slate-700">Contrôler chaque action dans l’outil réel.</p></div>
          </div>
        </div>
        <figure class="border-2 border-slate-950 bg-white p-3 shadow-neo">
          <img src="img/session-04/03-cowork-home.png" alt="Interface Claude Cowork" class="aspect-video w-full object-contain">
          <figcaption class="border-t-2 border-slate-950 px-3 py-3 text-sm font-semibold text-slate-700">Claude Cowork · dossier QG · connecteurs · tâches</figcaption>
        </figure>
      </div>
    </header>

    {chapter_nav()}

    <main>
      {section_markup}
      {sources_table()}
    </main>

    <footer class="border-t-2 border-slate-950 bg-slate-950 px-4 py-10 text-white sm:px-6 lg:px-8">
      <div class="mx-auto flex max-w-7xl flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <p class="font-black">DENEM Academy · Séance 4 · Claude Cowork</p>
        <p class="text-sm text-slate-300">80 sections · transcription horodatée · 16 visuels de la séance</p>
      </div>
    </footer>

    <script>
      const progress = document.getElementById('progress');
      const reveals = Array.from(document.querySelectorAll('.reveal'));
      const io = new IntersectionObserver((entries) => {{
        entries.forEach((entry) => {{
          if (entry.isIntersecting) entry.target.classList.add('in-view');
        }});
      }}, {{ threshold: 0.08 }});
      reveals.forEach((el) => io.observe(el));
      window.addEventListener('scroll', () => {{
        const max = document.documentElement.scrollHeight - innerHeight;
        const value = max > 0 ? scrollY / max : 0;
        progress.style.transform = `scaleX(${{value}})`;
      }}, {{ passive: true }});
    </script>
  </body>
</html>
"""


def main() -> None:
    html = render()
    OUT.write_text(html, encoding="utf-8")
    INDEX_OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.name} and {INDEX_OUT.name} with {len(flat_sections())} sections")


if __name__ == "__main__":
    main()
