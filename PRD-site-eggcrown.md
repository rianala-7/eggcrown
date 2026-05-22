# PRD — Site internet EggCrown

| | |
|---|---|
| **Produit** | Site vitrine + prise de commande EggCrown |
| **Version** | 1.0 (maquette) |
| **Date** | 12 mai 2026 |
| **Statut** | Maquette validée — en attente de contenus réels et de développement |
| **Marque** | EggCrown — producteur fermier d'œufs |
| **Localisation** | Antananarivo, Madagascar |
| **Livrable de référence** | `eggcrown-website.html` (maquette statique single-file) |

---

## 1. Vision & objectif

EggCrown est une petite ferme d'œufs lancée le 12 mai 2026 à Antananarivo (10 poules, équipe de 4 personnes). Le site doit transformer une présence en ligne en **outil de vente concret**, pas une simple vitrine.

**Objectif principal :** permettre à un habitant de Tana de découvrir EggCrown, comprendre l'offre, et passer commande en moins de 2 minutes — principalement via WhatsApp.

**Promesse de marque :** *« Frais, locaux, sérieux. »* — « Pondu le matin, livré dans la journée ».

---

## 2. Objectifs mesurables (KPI)

- Taux de clic vers WhatsApp ≥ 15 % des visiteurs
- Temps de compréhension de l'offre < 30 s
- Site lisible et commandable à 100 % sur mobile (cible : majorité du trafic)
- Chargement initial < 3 s sur connexion mobile malgache
- Zéro information inventée / fausse (traçabilité du contenu)

---

## 3. Public cible

| Persona | Besoin | Canal privilégié |
|---|---|---|
| **Famille de Tana** | Œufs frais réguliers, livrés à domicile | WhatsApp, livraison |
| **Restaurateur / pâtissier** | Volume (plateau de 30, commandes en gros) | Téléphone, abonnement |
| **Client de passage** | Acheter sur un marché / en magasin | Marché, point de vente |

---

## 4. Périmètre

### Dans le périmètre (v1)
- Site vitrine responsive (1 page, sections ancrées)
- Catalogue produits avec prix en Ariary
- Tunnel de commande léger (WhatsApp / téléphone / email — pas de panier e-commerce)
- Information livraison, paiement, fraîcheur
- FAQ, histoire de la marque, contact
- Multilingue prévu (FR / MG / EN)

### Hors périmètre (v1)
- Panier / paiement en ligne intégré
- Compte client / espace membre
- Gestion de stock automatisée
- Back-office d'administration

---

## 5. Architecture de l'information (sitemap)

Page unique avec navigation par ancres :

1. **Header** (sticky) — wordmark + nav + sélecteur de langue
2. **Hero** — logo doré sur fond sombre + accroche + CTA
3. **Engagements** — 3 valeurs (petite échelle / production limitée / 4 canaux)
4. **Nos œufs** — 3 formats + bandeau de disponibilité + remise gros volume
5. **Comment commander** — 4 étapes
6. **Bande de confiance** — fraîcheur / MVola / livraison Tana
7. **Où nous trouver** — 4 canaux + zone de livraison
8. **Abonnement hebdomadaire**
9. **Notre histoire**
10. **Avis clients** (en attente de validation)
11. **FAQ** — 7 questions
12. **Contact**
13. **Footer** — logo + liens + coordonnées + réseaux
14. **Bouton WhatsApp flottant** (global)

---

## 6. Exigences fonctionnelles (par section)

### 6.1 Header
- Wordmark « EggCrown » en dégradé doré
- Navigation : Nos œufs · Commander · Livraison · FAQ · Contact
- Sélecteur de langue FR · MG · EN (à activer en v1.1)
- Sticky avec fond sombre translucide

### 6.2 Hero
- Logo emblème doré (poule + couronne + nid + œuf + lauriers) sur fond sombre
- Accroche courte + 2 CTA (« Commander » primaire doré, « Notre histoire » secondaire)

### 6.3 Nos œufs (catalogue)
- 3 formats : carton de 6 (3 300 Ar), carton de 12 (6 600 Ar), plateau de 30 (16 500 Ar)
- Prix unitaire : **550 Ar / œuf**
- Remise automatique **−5 % dès 60 œufs**
- Badge de stock par produit (Disponible / Sur réservation)
- Bandeau de disponibilité hebdomadaire (~50 œufs/semaine)
- Photo produit carrée par format
- CTA « Ajouter » → ouvre la commande (WhatsApp en v1)

### 6.4 Comment commander
- 4 étapes : Choisir → Écrire (WhatsApp/tél/email) → Ramassage du matin → Livraison/retrait

### 6.5 Livraison & paiement
- Zone : **Antananarivo uniquement** (quartiers listés)
- Modèle : pondu le matin, livré dans la journée ; commande avant midi → livraison après-midi
- Paiement : **MVola** (Mobile Money) ou **espèces à la livraison**
- *Tarif de livraison : à définir par EggCrown*

### 6.6 Abonnement hebdomadaire
- Livraison récurrente d'un format au choix, annulable
- *Modalités exactes : à définir (CTA actuellement inactif)*

### 6.7 Avis clients
- 3 cartes (étoiles + citation + auteur)
- **Tout avis doit être validé par EggCrown avant publication** (workflow de modération obligatoire)
- État actuel : exemples marqués « À valider », non publiables tels quels

### 6.8 FAQ
- 7 questions en accordéon : fraîcheur, conservation, commande, paiement, délais, quantité min, élevage

### 6.9 Contact
- Téléphone : 034 28 234 85 *(à confirmer — voir §10)*
- WhatsApp : **0383792542** (+261383792542)
- Email : rianalanathan@gmail.com
- Facebook : Nathan Rianala *(URL exacte à fournir)*

### 6.10 Bouton WhatsApp flottant
- Lien `wa.me/261383792542`
- Visible sur toutes les sections, texte masqué sur mobile (icône seule)

---

## 7. Exigences de contenu

- **Devise unique :** Ariary (Ar), séparateur d'espace (ex. « 6 600 Ar »)
- **Langue principale :** français ; MG et EN à venir
- **Ton :** chaleureux, honnête, premium accessible — jamais corporate
- **Règle d'or :** aucun contenu inventé. Les éléments non confirmés sont marqués « à confirmer » / « à valider »
- **Pas de noms de personnes en prose** ; le nom de famille **RIANALA** peut apparaître ; le compte Facebook affiche « Nathan Rianala »

---

## 8. Exigences design / UX

### Système de couleurs (palette or premium)
| Rôle | Hex |
|---|---|
| Fond clair (Cloud Dancer) | `#F0EEE9` |
| Fond crème | `#FAF6EB` |
| Or antique (accent) | `#B5862B` |
| Or vif (highlights) | `#C8941F` |
| Or clair (dégradés) | `#E8C25A` |
| Driftwood (texte secondaire) | `#7C6F5A` |
| Espresso (texte) | `#2C2A26` |
| Bark / sombre | `#221913` |
| Near-black (surfaces sombres) | `#14100B` |

### Typographie
- **Titres :** PP Editorial New / Recoleta / Georgia (serif éditorial)
- **Corps :** Helvetica Neue / Inter / Arial (sans-serif)
- Eyebrows en capitales très espacées (letter-spacing 0.6em)

### Logo
- Emblème doré (poule + couronne + nid + œuf doré + lauriers + wordmark + tagline + 3 indicateurs)
- Versions disponibles : original noir, transparent, fond blanc, 18 variantes de couleur (bronze, terre cuite, moka, etc.)
- Usage : grand sur fonds sombres (hero, footer) ; le détail ne convient pas en miniature

### Principes UX
- Zones sombres (header/hero/footer) où l'or brille ; corps clair lisible avec accents dorés
- Hiérarchie d'action : boutons dorés = action principale ; outline = secondaire
- Icônes SVG dorées en ligne fine (pas d'emojis)

---

## 9. Exigences non-fonctionnelles

| Domaine | Exigence |
|---|---|
| **Responsive** | Mobile-first ; bascule colonne unique < 800px |
| **Performance** | Chargement < 3s mobile ; images en `loading="lazy"` |
| **Accessibilité** | Attributs `alt`, contrastes suffisants, navigation clavier |
| **SEO** | `<title>`, meta description, mots-clés « œufs frais Antananarivo », favicon SVG |
| **Compatibilité** | Navigateurs récents mobile + desktop |
| **Hébergement** | Statique (le site est un fichier HTML autonome) — hébergeable n'importe où |

---

## 10. Points ouverts / décisions en attente

| # | Élément | Responsable | Statut |
|---|---|---|---|
| 1 | Tarif de livraison | EggCrown | À définir |
| 2 | Marchés précis (noms, horaires) | EggCrown | À confirmer |
| 3 | Magasins partenaires | EggCrown | À confirmer |
| 4 | URL exacte du compte Facebook | EggCrown | À fournir |
| 5 | Photos réelles (poules, œufs, poulailler) | EggCrown | À fournir (Unsplash en placeholder) |
| 6 | Modalités de l'abonnement | EggCrown | À définir |
| 7 | Cohérence du numéro de téléphone (034… vs 038… WhatsApp) | EggCrown | À vérifier |
| 8 | Type d'élevage exact (réponse « autre ») | EggCrown | À préciser si affiché |
| 9 | Vrais avis clients | EggCrown | Après premières ventes |
| 10 | Traductions MG / EN | À produire | v1.1 |

---

## 11. Intégrations

- **WhatsApp** : lien direct `wa.me` (v1) ; pré-remplissage du message à étudier
- **MVola** : mention dans le contenu ; pas d'intégration de paiement en v1
- **Réseaux sociaux** : Facebook (lien à fournir)

---

## 12. Roadmap (post-v1)

**v1.1** — Traductions MG/EN actives · photos réelles · tarif livraison · URL Facebook
**v1.2** — Formulaire de commande structuré · message WhatsApp pré-rempli · vrais avis validés
**v2.0** — Abonnement opérationnel · panier + paiement Mobile Money en ligne · page produit détaillée · blog/recettes (SEO)

---

## 13. Critères d'acceptation (v1)

- [ ] Le site s'ouvre et s'affiche correctement sur mobile et desktop
- [ ] Tous les prix sont en Ariary et exacts (550 Ar/œuf, remise 60+)
- [ ] Le bouton WhatsApp ouvre une conversation vers +261383792542
- [ ] Aucune information fausse ou inventée n'est présentée comme certaine
- [ ] Les avis affichent clairement leur statut « à valider »
- [ ] Le logo doré s'affiche net sur les fonds sombres
- [ ] La navigation par ancres fonctionne sur toutes les sections
- [ ] Le contenu non confirmé est visiblement marqué « à confirmer »

---

## 14. User stories

Format : *En tant que [persona], je veux [action] afin de [bénéfice].*
Priorité MoSCoW : **M** = Must (v1) · **S** = Should · **C** = Could (v2+).

### 14.1 Famille de Tana (acheteur récurrent)

| # | User story | Prio | Critère d'acceptation |
|---|---|---|---|
| F1 | En tant que famille, je veux **comprendre l'offre et les prix en moins de 30 s** afin de décider rapidement. | M | Les 3 formats et le prix au 550 Ar/œuf sont visibles dès la section « Nos œufs » sans scroll profond. |
| F2 | En tant que famille, je veux **commander en un clic via WhatsApp** afin d'éviter tout formulaire compliqué. | M | Le bouton flottant ouvre une conversation vers +261383792542 depuis n'importe quelle section. |
| F3 | En tant que famille, je veux **savoir si les œufs sont frais** afin d'avoir confiance. | M | La promesse « Pondu le matin, livré dans la journée » apparaît dans la bande de confiance + la FAQ. |
| F4 | En tant que famille, je veux **connaître la zone et le délai de livraison** afin de vérifier que mon quartier est couvert. | M | La section livraison liste les quartiers de Tana + le modèle « commande avant midi → livraison l'après-midi ». |
| F5 | En tant que famille, je veux **payer par MVola ou en espèces** afin d'utiliser mon moyen habituel. | M | Les modes de paiement sont annoncés dans la bande de confiance et la FAQ. |
| F6 | En tant que famille, je veux **m'abonner pour être livré chaque semaine** afin de ne plus y penser. | S | La section abonnement permet de choisir un format récurrent (CTA actif en v2). |

### 14.2 Restaurateur / pâtissier (volume)

| # | User story | Prio | Critère d'acceptation |
|---|---|---|---|
| R1 | En tant que restaurateur, je veux **commander de gros volumes** afin d'approvisionner mon établissement. | M | Le plateau de 30 et la mention « commandes en gros » sont disponibles. |
| R2 | En tant que restaurateur, je veux **bénéficier d'une remise sur les grosses quantités** afin de réduire mon coût. | M | La remise −5 % dès 60 œufs est affichée clairement (section produits + note). |
| R3 | En tant que restaurateur, je veux **un contact direct (tél/WhatsApp)** afin de négocier livraison et récurrence. | M | Les coordonnées sont accessibles en header, contact et footer. |
| R4 | En tant que restaurateur, je veux **une livraison fiable et planifiée** afin de sécuriser mon service. | S | Mention d'un créneau convenu ; abonnement pro à préciser (v2). |

### 14.3 Nouveau visiteur / client de passage

| # | User story | Prio | Critère d'acceptation |
|---|---|---|---|
| V1 | En tant que nouveau visiteur, je veux **comprendre qui est EggCrown** afin d'évaluer la confiance. | M | La section « Notre histoire » présente la ferme (sans inventer). |
| V2 | En tant que visiteur, je veux **voir des avis** afin d'être rassuré. | S | Section avis présente ; **aucun avis publié sans validation EggCrown** (workflow obligatoire). |
| V3 | En tant que visiteur, je veux **trouver les réponses aux questions courantes** afin de ne pas avoir à écrire. | M | FAQ de 7 questions (fraîcheur, conservation, paiement, délais…). |
| V4 | En tant que visiteur, je veux **acheter sur un marché ou en magasin** afin d'éviter la livraison. | S | Section « Où nous trouver » liste les 4 canaux (marchés/magasins « à confirmer »). |
| V5 | En tant que visiteur, je veux **lire le site dans ma langue (FR/MG/EN)** afin d'être à l'aise. | C | Sélecteur de langue fonctionnel (v1.1). |

### 14.4 EggCrown (propriétaire / gestionnaire) — partie prenante interne

| # | User story | Prio | Critère d'acceptation |
|---|---|---|---|
| E1 | En tant que gérant, je veux **recevoir les commandes sur WhatsApp** afin de les traiter avec l'outil que j'utilise déjà. | M | Toutes les CTA de commande convergent vers WhatsApp/téléphone. |
| E2 | En tant que gérant, je veux **valider chaque avis avant publication** afin de garder la maîtrise de mon image. | M | Aucun avis n'est publié sans action de validation explicite. |
| E3 | En tant que gérant, je veux **que rien de faux ne soit affiché** afin de rester honnête et crédible. | M | Tout contenu non confirmé est marqué « à confirmer / à valider ». |
| E4 | En tant que gérant, je veux **mettre à jour facilement prix, quartiers et coordonnées** afin de suivre l'évolution de la ferme. | S | Contenu centralisé et clairement identifié dans le HTML (v1) ; CMS léger envisageable (v2). |
| E5 | En tant que gérant, je veux **remplacer les photos par mes vraies poules/œufs** afin de montrer mon vrai produit. | S | Les `<img>` Unsplash sont isolés et remplaçables par des chemins locaux. |

---

## 15. Matrice de traçabilité

Relie chaque user story (§14) à la (aux) section(s) fonctionnelle(s) qui la réalise(nt) et à l'élément concret de la maquette. Permet de vérifier qu'aucune story n'est orpheline et qu'aucune fonctionnalité n'est sans justification.

| Story | Besoin résumé | Section(s) fonctionnelle(s) | Élément concret (maquette) | Prio | État |
|---|---|---|---|---|---|
| F1 | Comprendre offre + prix | §6.2 Hero, §6.3 Nos œufs | Cartes produit + bandeau 550 Ar | M | ✅ Fait |
| F2 | Commander via WhatsApp | §6.4 Comment commander, §6.10 Bouton WA | Bouton flottant `wa.me/261383792542` | M | ✅ Fait |
| F3 | Vérifier la fraîcheur | §6.5 Bande de confiance, §6.8 FAQ | Pilier « Pondu le matin » + FAQ Q1 | M | ✅ Fait |
| F4 | Connaître zone/délai | §6.5 Livraison | Section zone + quartiers Tana | M | ⚠️ Tarif à définir |
| F5 | Payer MVola/espèces | §6.5 Paiement, §6.8 FAQ | Pilier MVola + FAQ Q4 | M | ✅ Fait |
| F6 | S'abonner | §6.6 Abonnement | Bande abonnement + CTA | S | ⚠️ CTA inactif |
| R1 | Gros volumes | §6.3 Nos œufs | Plateau de 30 + note gros | M | ✅ Fait |
| R2 | Remise volume | §6.3 Nos œufs | Mention −5 % dès 60 œufs | M | ✅ Fait |
| R3 | Contact direct | §6.1 Header, §6.9 Contact | Coordonnées header/contact/footer | M | ⚠️ N° tél à vérifier |
| R4 | Livraison planifiée | §6.5, §6.6 | Créneau convenu + abonnement | S | ⚠️ À préciser |
| V1 | Découvrir la marque | §9 Notre histoire | Section histoire | M | ✅ Fait |
| V2 | Voir des avis | §6.7 Avis clients | Cartes avis « À valider » | S | ⚠️ Avis réels en attente |
| V3 | Réponses aux questions | §6.8 FAQ | FAQ 7 questions | M | ✅ Fait |
| V4 | Acheter marché/magasin | §6.5 Où nous trouver | 4 cartes canaux | S | ⚠️ Marchés/magasins à confirmer |
| V5 | Lire dans sa langue | §6.1 Header | Sélecteur FR·MG·EN | C | ⛔ v1.1 (non actif) |
| E1 | Recevoir commandes WA | §6.4, §6.10 | Convergence CTA → WhatsApp | M | ✅ Fait |
| E2 | Valider les avis | §6.7 Avis clients | Workflow « À valider » obligatoire | M | ✅ Fait (process) |
| E3 | Rien de faux affiché | §7 Contenu | Tags « à confirmer / à valider » | M | ✅ Fait |
| E4 | Mettre à jour le contenu | §9 NF, §12 Roadmap | Contenu centralisé HTML | S | ⚠️ CMS en v2 |
| E5 | Vraies photos | §6.3, §8 Design | `<img>` Unsplash remplaçables | S | ⚠️ Photos réelles en attente |

**Légende état :** ✅ Réalisé dans la maquette · ⚠️ Réalisé mais bloqué par une donnée manquante (§10) · ⛔ Reporté à une version ultérieure.

**Lecture rapide :**
- **11 stories sur 20 sont pleinement réalisées** (✅).
- **8 sont en place mais bloquées** par une décision/donnée d'EggCrown (⚠️ — tarif livraison, n° téléphone, abonnement, avis réels, photos, marchés/magasins).
- **1 est reportée** (⛔ V5 multilingue → v1.1).
- **Aucune story orpheline** et **aucune section fonctionnelle sans story** : le périmètre est cohérent.

---

*Document de travail — à mettre à jour au fur et à mesure des décisions d'EggCrown.*
