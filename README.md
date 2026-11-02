# GO GYM MSAKEN — Premium website (GitHub Pages)

**Site complet statique** : 10 pages HTML, CSS premium, JavaScript interactif, 10 vraies photos optimisées en WebP, 1 visuel d'ambiance IA, contenu et référencement local.

## 1. Voir le site sur Windows

- Décompresse le fichier ZIP.
- Ouvre `index.html` dans Chrome pour la première prévisualisation.
- Pour toutes les fonctionnalités et des URL fiables, ouvre un terminal dans le dossier et exécute `python -m http.server 8000` (ou `py -m http.server 8000`). Ouvre `http://localhost:8000/`.

## 2. Mettre sur GitHub Pages (sans Node, ni npm, ni Firebase)

1. Connecte-toi à [github.com](https://github.com) et crée un **nouveau dépôt public**, par exemple `go-gym-msaken`.
2. Clique sur **Add file → Upload files**, et importe **le contenu du dossier `GO_GYM_MSAKEN_SITE`**, pas le ZIP dans le dépôt. La racine du dépôt doit contenir `index.html`, `css/`, `js/`, `assets/`, etc.
3. Clique sur **Commit changes**.
4. Va dans **Settings → Pages → Build and deployment**.
5. Sélectionne **Deploy from a branch → main → /(root) → Save**.
6. L'adresse sera typiquement `https://TON-USERNAME.github.io/go-gym-msaken/`. Si le dépôt est nommé autrement, utilise le vrai nom.
7. Pour obtenir le meilleur SEO, passe à l'étape suivante avant de publier définitivement.

## 3. SEO final — important

Les balises `title`, descriptions, textes des pages, attributs `alt` et JSON-LD `ExerciseGym` sont déjà intégrés. Pour ajouter les **URL canoniques absolues**, Open Graph et un **sitemap.xml valide**, exécute AVANT d'envoyer sur GitHub :

```bash
python scripts/configure_site.py https://TON-USERNAME.github.io/go-gym-msaken/
```

**Remplace l'adresse par la véritable URL du site.** Par exemple avec un domaine personnalisé :

```bash
python scripts/configure_site.py https://www.mondomaine.tn/
```

Le script prépare les 10 pages, `sitemap.xml` et `robots.txt`. Il peut être relancé avec le vrai domaine si celui-ci change.

Puis, une fois le site publié :

- Ajouter le site à Google Search Console.
- Soumettre `https://ADRESSE-REELLE/sitemap.xml` dans **Sitemaps**.
- Mettre à jour la fiche Google Business Profile avec l'adresse du site, horaires, images, téléphone, site.
- Vérifier l'affichage des pages sur mobile et les résultats du [Rich Results Test](https://search.google.com/test/rich-results).
- Demander de vrais avis Google à de vrais adhérents. Ne pas utiliser des témoignages fictifs comme preuves sociales réelles.

**SEO ne signifie pas garantie de 1re position Google.** La présence locale dépend notamment de l'adresse, la pertinence, les signaux locaux et la qualité de la fiche Business Profile.

## 4. Pages incluses

- `index.html` — accueil premium avec image IA indiquée, photos réelles, animations, services, avis démo identifiés et FAQ.
- `la-salle.html` — présentation + photos réelles.
- `activites.html` — 3 espaces : musculation, cardio, cours collectifs.
- `abonnements.html` — demandes de tarifs sans prix inventés.
- `galerie.html` — 10 photographies réelles, filtres et affichage plein écran.
- `contact.html` — WhatsApp, téléphone, carte et formulaire WhatsApp sans base de données.
- `blog/index.html` — index blog SEO.
- `blog/*.html` — trois guides utiles.
- `404.html` — page d'erreur.

## 5. Données et transparence

- Nom : **GO GYM MSAKEN**.
- Téléphone fourni : **+216 25 000 314** (URL WhatsApp : `wa.me/21625000314`).
- Adresse : **PHWQ+324, P1, M'saken, Tunisie**.
- Instagram : `https://www.instagram.com/gogym.msaken/`.
- Facebook : `https://www.facebook.com/gogym.tn/?locale=fr_FR`.
- Photos : les **10 photographies reçues dans le ZIP** ont été compressées au format WebP ; 1 image hero IA est explicitement étiquetée comme illustration d'ambiance (elle ne prétend pas montrer le vrai local).
- **Avis / témoignages** : 3 textes de démonstration clairement désignés comme fictifs. Remplacer par des avis authentiques et autorisés avant une utilisation commerciale ; ne pas les marquer comme avis Google.
- **Tarifs / horaires / disciplines précises** : aucune donnée non confirmée inventée. Demandes dirigées vers la salle.
- **Téléphone** : certains annuaires publics affichent une autre variante du téléphone, vérifie et harmonise ta fiche Google Business Profile et tes réseaux si besoin.
- Identité : wordmark `GO GYM` créé pour ce prototype ; si tu as le logo vectoriel officiel, remplace-le avant publication.

## 6. Modifier les couleurs et le contenu

- Couleurs : dans `css/style.css`, bloc `:root` (`--accent` pour le jaune lime, `--blue` pour le bleu).
- Textes : dans les fichiers `.html` directement.
- Photos : `assets/images/`; les fichiers finissent en `.webp`.
- Téléphone dans le formulaire WhatsApp : `js/main.js`.
- Liens sociaux et téléphone du footer : tous les fichiers HTML.

## 7. Performances et accessibilité

Aucun framework à builder, pas de dépendance JavaScript à installer, images WebP, CSS adaptable aux smartphones, effets limités quand le système demande `prefers-reduced-motion`, liens téléphoniques et WhatsApp fonctionnels. Google Fonts est la seule ressource de style chargée à distance ; le site dispose de polices système de secours.

## 8. Mise en garde

Ce site est un site **vitrine / prise de contact** ; il ne dispose pas d'espace d'administration, de vrai module de paiement ou de réservation en ligne, ni de synchronisation automatique des avis Google. Le formulaire ouvre WhatsApp et ne sauvegarde pas de données. Le site reste publiable sur GitHub Pages tel quel, sans base de données.
