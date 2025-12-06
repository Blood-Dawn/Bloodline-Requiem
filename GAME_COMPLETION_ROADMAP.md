# BLOODLINE REQUIEM - GAME COMPLETION ROADMAP

**Last Updated:** December 6, 2025  
**Current Version:** 0.5.0 (Phase 1 Complete)  
**Target Version:** 1.0.0 (Full Release)  
**Estimated Completion:** 3-6 months

---

## EXECUTIVE SUMMARY

This document outlines **everything needed** to complete Bloodline Requiem from its current state (Phase 1 - Systems Operational) to a fully playable, polished interactive fiction game with 20-30 hours of content across multiple origins and endings.

**Current State:**
- ✅ Core systems complete (abilities, progression, codex hub)
- ✅ 7 playable origins (Assassin, Varkyr, Lupine, Forsaken, Noble, Commoner, Hunter)
- ✅ Act 1 endgames implemented for all four faction routes
- ⚠️ Act 2-3 not started (only placeholder hub)
- ❌ Romance content not started (NPCs defined, no scenes)
- ❌ Endgame/epilogues not started

**What's Needed:**
- 🔴 Act 1 completion polish/XP sync (~500 lines)
- 🔴 Act 2 creation (~5,000 lines)
- 🔴 Act 3 creation (~3,000 lines)
- 🔴 Romance system (~2,000 lines)
- 🔴 Endgame scenarios (~1,500 lines)
- 🔴 Polish, testing, balancing

**Total New Content Required:** ~12,000+ lines of ChoiceScript

---

## TABLE OF CONTENTS

1. [Phase 2: Origin Completion & Act 1 Integration](#phase-2-origin-completion--act-1-integration)
2. [Phase 3: Act 2 Development](#phase-3-act-2-development)
3. [Phase 4: Act 3 & Endgame](#phase-4-act-3--endgame)
4. [Phase 5: Romance & Character Arcs](#phase-5-romance--character-arcs)
5. [Phase 6: Polish & Testing](#phase-6-polish--testing)
6. [Incomplete Systems & Features](#incomplete-systems--features)
7. [Missing Content Breakdown](#missing-content-breakdown)
8. [File Creation Checklist](#file-creation-checklist)
9. [Scene Flow Architecture](#scene-flow-architecture)
10. [Testing & Quality Assurance](#testing--quality-assurance)
11. [Recommended Development Order](#recommended-development-order)
12. [Appendices](#appendices)

---

## PHASE 2: ORIGIN COMPLETION & ACT 1 INTEGRATION

**Duration:** 3-4 weeks  
**Priority:** CRITICAL  
**Status:** ✅ Origins created; Act 1 integration polish pending

### 2.1 Complete Missing Origins

#### ✅ **origin_noble.txt** (CREATED)
- Status: Implemented in `origins/origin_noble.txt` with branches for study investigation, official inquiry, or exile through the Warren.
- Routes: Human (`act1_human`), Varkyr (`act1_varkyr`), or Lupine (`act1_lupine`) via Embrace/oath choices.
- Hooks: Isabella, Adrian, Lucan, and Rurik introductions; 100-125 XP awarded based on allegiance decisions.

#### ✅ **origin_commoner.txt** (CREATED)
- Status: Implemented in `origins/origin_commoner.txt` starting with the Warren ritual chase (run/hide/fight branches).
- Routes: Human, Varkyr, Lupine, or Forsaken entry points; survival-driven transformations.
- Hooks: Caius, Lucan, Elena rescue, Guild pressure; 50-125 XP depending on escape path.

#### ✅ **origin_hunter.txt** (CREATED)
- Status: Implemented in `origins/origin_hunter.txt` as advanced Order of the Silver Dawn start with selectable hunts (Varkyr/Lupine/Forsaken).
- Routes: Human, Varkyr, Lupine, or Forsaken depending on how the contract resolves.
- Hooks: Nadia briefing, Isabella/Rurik/Caius encounters; 150-200 XP with faction relation shifts.

### 2.2 Refactor Existing Origins

#### 🟡 **Refactor prologue.txt → origin_assassin.txt**
**Status:** Partial content exists, needs reorganization

**Required Changes:**
1. Move prologue.txt content to `origins/origin_assassin.txt`
2. Rename `*label introduction` to `*label assassin_start`
3. Update `origin_select.txt` to route to new location
4. Remove prologue.txt from scene_list in startup.txt
5. Add proper XP grants and progression calls
6. Integrate rank_progression system

**Code Migration:**
```choicescript
*comment OLD (prologue.txt):
*label introduction
*goto forsaken_route

*comment NEW (origin_assassin.txt):
*label assassin_start
*gosub_scene rank_progression gain_xp 50 "Guild Initiation"
*goto contract_selection
```

---

#### 🟡 **Complete origin_varkyr.txt**
**Status:** 354 lines, good intro, needs endgame

**Missing Content:**
- Post-bloodline selection narrative (currently jumps to abilities)
- Crimson Spire trials (currently just ability select)
- First feeding scene
- Conflict with rival fledgling
- Final trial before Act 1
- Route to `act1_varkyr.txt` with proper setup

**Required Additions:** ~150 lines

---

#### 🟡 **Complete origin_lupine.txt**
**Status:** 267 lines, good intro, needs endgame

**Missing Content:**
- Post-hunt completion (currently ends at kill_complete)
- Return to pack with proof
- Alpha's judgment ceremony
- First howl with pack
- Pack hierarchy establishment
- Route to `act1_lupine.txt` with proper setup

**Required Additions:** ~100 lines

---

#### 🟡 **Complete origin_forsaken.txt**
**Status:** 244 lines, good intro, needs endgame

**Missing Content:**
- Post-ability selection (currently ends at abilities_unlock)
- First lesson with Caius (partially written)
- First mission for Forsaken
- Underground exploration
- Meeting other hybrids
- Route to `act1_forsaken_ng+.txt` or new act1_forsaken.txt

**Required Additions:** ~150 lines

---

### 2.3 Integrate Rank Progression into Act 1

**Current Problem:** Act 1 scenes don't call rank_progression, so players can't rank up during gameplay.

**Required Changes:**

#### 🔴 **act1_varkyr.txt** - Add XP Grants
**Locations to add XP:**
1. After tracking vampire (line ~30)
2. After varkyrs_confrontation (line ~59)
3. After combat (line ~112)
4. After investigation complete (line ~247)
5. Before scene end, add `*gosub_scene rank_progression check_progression`

**Example Integration:**
```choicescript
*label varkyr_end

*comment Check for rank progression at end of investigation
*gosub_scene rank_progression check_progression

*line_break

*if (alignment = "varkyrs")
    The investigation complete, you feel the weight of new knowledge—and new power.
```

---

#### 🔴 **act1_lupine.txt** - Add XP Grants
**Locations to add XP:**
1. After entering territory (line ~4)
2. After pack encounter (line ~50)
3. After combat/diplomacy (line ~149)
4. After explaining mission (line ~206)
5. Before end_scene, add progression check

---

#### 🔴 **act1_human.txt** - Complete & Add XP
**Current State:** Only 41 lines, placeholder content

**Required Content:**
- Full Silver Legion training sequence
- Commander Vale interactions
- First monster hunt mission
- Choice: Stay human vs Seek transformation
- Route to hub_city or transformation path
- Multiple XP grants (75-150 total)

**Estimated Additions:** ~300 lines

---

#### 🔴 **act1_forsaken_ng+.txt** - Rename & Expand
**Current State:** 18 lines, just a label

**Required Changes:**
1. Rename to `act1_forsaken.txt` (remove "ng+" suffix)
2. Write full Forsaken Act 1 content:
   - Underground missions for Caius
   - Hybrid stability management
   - Faction conflict (hunted by Varkyrs AND Lupines)
   - Ecliptic Shard introduction
   - Route to Act 2
3. Integrate XP system

**Estimated New Content:** ~500 lines

---

### 2.4 Create Origin Selection Hub

#### 🟡 **origin_select.txt** - Complete All Routes
**Current State:** 7 origins listed, 3 incomplete

**Required Changes:**
1. Update routes for Noble, Commoner, Hunter
2. Add recommended difficulty markers
3. Add brief faction teasers
4. Test all 7 routes work

**Current Code Issues:**
```choicescript
*comment CURRENT (broken routes):
#Human Noble - Heir to a Tarnished Throne
    *goto_scene origin_noble murder_investigation
    *comment ❌ origin_noble.txt doesn't exist!

*comment NEEDED:
#Human Noble - Heir to a Tarnished Throne
    *set alignment "human"
    *set rank "Minor Noble"
    *set age 24
    *goto_scene origin_noble noble_start
```

---

### 2.5 Complete Act 1 Endgame Sequences

All four Act 1 routes currently end abruptly. Each needs proper conclusion:

#### 🔴 **act1_varkyr.txt** - Add Ending
**After line ~247 (varkyr_end):**
- Crimson Spire summons player
- First rank-up ceremony (if eligible)
- Introduction to Varkyr politics
- Ecliptic Amulet mention
- Choice: Loyal to Spire vs Independent vs Rebel
- Route to Act 2 hub

**Required Addition:** ~200 lines

---

#### 🔴 **act1_lupine.txt** - Add Ending
**After line ~295 (end_scene):**
- Return to Whispering Pines
- Pack acceptance ceremony
- Rurik's mission briefing
- Moon phase advancement
- Choice: Serve pack vs Lone wolf vs Unite packs
- Route to Act 2 hub

**Required Addition:** ~200 lines

---

#### 🔴 **act1_human.txt** - Add Ending
**Current ending at line 41 - needs full completion:**
- Legion promotion or Guild advancement
- First successful hunt
- Transformation decision point
- Artifact acquisition opportunity
- Choice: Remain human vs Transform vs Hybrid hunter
- Route to Act 2 hub

**Required Addition:** ~250 lines

---

#### 🔴 **act1_forsaken.txt** - Create Full Arc
**Completely new file needed:**
- Caius's missions
- Hybrid stability trials
- Hunted by both factions
- First Eclipse ability unlock
- Choice: Serve Caius vs Independent vs Seek acceptance
- Route to Act 2 hub

**Required Creation:** ~500 lines

---

## PHASE 3: ACT 2 DEVELOPMENT

**Duration:** 6-8 weeks  
**Priority:** HIGH  
**Status:** 🔴 Not Started (only placeholder hub exists)

### 3.1 Act 2 Overview

**Setting:** War escalation, faction conflict intensifies  
**Player Level:** Rank 3-5 (mid-tier abilities unlocked)  
**Main Quest:** Ecliptic Amulet shard hunt  
**Content:** ~5,000 lines across multiple scenes

**Core Themes:**
- Political intrigue between factions
- First major choices affect world state
- Romance routes become available
- Ecliptic Amulet lore deepens
- Build toward faction war or peace

---

### 3.2 Required Act 2 Scenes

#### 🔴 **act2_common_hub.txt** - Expand
**Current State:** 30 lines, basic placeholder

**Required Content:**
```choicescript
*label act2_start
*set act 2
*set chapter 1

*comment INTRO: Greyhaven Council meeting
*comment Faction tensions revealed
*comment Player chooses alliance

*comment MAIN BRANCHES:
  *comment 1. Varkyr court intrigue
  *comment 2. Lupine pack politics  
  *comment 3. Forsaken underground war
  *comment 4. Human resistance movement

*comment SHARED ELEMENTS:
  *comment - Ecliptic Shard quest intro
  *comment - Romance interactions
  *comment - Faction war buildup
  *comment - Time passage (moon phases)
```

**Required Expansion:** ~400 lines

---

#### 🔴 **act2_varkyr_court.txt** (NEW FILE)
**Estimated Lines:** 1,200+

**Required Content:**
1. **Crimson Spire Politics**
   - Noble house rivalries
   - Matriarch's secret plans
   - Blood magic research
   - Rank advancement opportunities

2. **Isabella Romance Path** (if pursuing)
   - Diplomatic missions together
   - Political alliance or genuine affection
   - Relationship progression scenes

3. **Vincent Subplot**
   - Shadow bloodline assassination contracts
   - Night Council conspiracy
   - Player choice: Join vs Expose

4. **Ecliptic Shard Quest**
   - Varkyr Shard location revealed
   - Heist or diplomacy to acquire
   - Consequences for faction standing

5. **Endgame Decision**
   - Support Matriarch's war plans
   - Seek peace with Lupines
   - Independent power play

**Labels Needed:**
- `*label court_entry`
- `*label noble_intrigue`
- `*label shard_heist`
- `*label varkyr_romance`
- `*label court_finale`

---

#### 🔴 **act2_lupine_territory.txt** (NEW FILE)
**Estimated Lines:** 1,200+

**Required Content:**
1. **Pack Politics**
   - Alpha challenges
   - Pack unification efforts
   - Moon ritual participation
   - Rank advancement trials

2. **Rurik/Thane/Rhea Interactions**
   - Pack leadership decisions
   - Romance paths available
   - Loyalty vs ambition choices

3. **Skylar Subplot**
   - Lone wolf reconciliation
   - Exile reversal opportunity
   - Alternative pack formation

4. **Ecliptic Shard Quest**
   - Lupine Shard guarded by ancient alpha
   - Trial by combat or wisdom
   - Pack honor at stake

5. **Endgame Decision**
   - Unite all packs under player
   - Maintain independence
   - Alliance with other faction

**Labels Needed:**
- `*label territory_entry`
- `*label pack_trials`
- `*label shard_trial`
- `*label lupine_romance`
- `*label pack_finale`

---

#### 🔴 **act2_forsaken_underground.txt** (NEW FILE)
**Estimated Lines:** 1,000+

**Required Content:**
1. **Underground Society**
   - Forsaken enclave exploration
   - Hybrid stability management
   - Caius's true plans revealed
   - War Form unlock opportunity

2. **Dante/Mira Romance Paths**
   - Hybrid bonding unique mechanics
   - Stability affects relationships
   - Dual nature acceptance

3. **Hunted Subplot**
   - Varkyr AND Lupine assassins
   - Survival against both factions
   - Prove Forsaken legitimacy

4. **Ecliptic Shard Quest**
   - Caius already controls 1-2 shards
   - Choice: Help him get more vs Steal vs Destroy

5. **Endgame Decision**
   - Serve Caius's vision
   - Break away and lead own group
   - Seek recognition from factions

**Labels Needed:**
- `*label underground_entry`
- `*label hybrid_trials`
- `*label shard_confrontation`
- `*label forsaken_romance`
- `*label underground_finale`

---

#### 🔴 **act2_human_resistance.txt** (NEW FILE)
**Estimated Lines:** 1,000+

**Required Content:**
1. **Human Factions**
   - Assassin Guild contracts
   - Silver Legion operations
   - Church hunters
   - Noble house politics

2. **Lucan/Adrian/Nadia Paths**
   - Human solidarity vs pragmatism
   - Transformation temptation
   - Romance if stayed human

3. **Artifact Hunt**
   - Alternative to supernatural powers
   - Ancient weapons/relics
   - Ecliptic Shard from human perspective

4. **Transformation Decision**
   - If still human, final choice point
   - Accept Embrace/Bite/Hybrid
   - Or remain human with artifacts

5. **Endgame Decision**
   - Lead human resistance
   - Broker peace between factions
   - Seek power through transformation

**Labels Needed:**
- `*label resistance_entry`
- `*label human_operations`
- `*label artifact_quest`
- `*label human_romance`
- `*label resistance_finale`

---

### 3.3 Act 2 Shared Systems

#### 🔴 **Time Passage System** (NEW)
**File:** `systems/time_passage.txt`  
**Estimated Lines:** 200+

**Required Features:**
```choicescript
*label advance_time
*comment Advances moon phase, drains blood satiation, ages NPCs

*gosub advance_moon_phase
*if (alignment = "varkyrs")
    *gosub varkyr_time_effects
*if (alignment = "lupine")
    *gosub lupine_time_effects

*return

*label advance_moon_phase
*comment Cycles through 8 moon phases
*comment (already partially implemented in docs, needs full scene)

*label varkyr_time_effects
*set blood_satiation -10
*if (blood_satiation < 30)
    *set Bloodlust +5
*return

*label lupine_time_effects
*if (moon_phase = "Full")
    *set strength +20
    *set rage +10
*elseif (moon_phase = "New")
    *set strength -10
*return
```

**Integration:** Call from act2 scenes during travel/rest

---

#### 🔴 **Active Ability Equip** (NEW)
**File:** `systems/ability_equip.txt`  
**Estimated Lines:** 300+

**Purpose:** Player chooses 5 abilities from unlocked pool to use in combat

**Required Features:**
```choicescript
*label equip_abilities
*temp slot1 ""
*temp slot2 ""
*temp slot3 ""
*temp slot4 ""
*temp slot5 ""

Choose 5 abilities to equip:

*comment List all unlocked abilities
*if (shadow_step)
    #Equip Shadow Step
        *set slot1 "shadow_step"
        *goto select_slot2

*comment Save equipped abilities to persistent variables
*comment During combat, only check equipped abilities
```

**Integration:** Available at hub cities, before major battles

---

#### 🔴 **Reputation Consequences** (NEW)
**File:** `systems/reputation_effects.txt`  
**Estimated Lines:** 150+

**Purpose:** Faction relations affect available options

**Required Features:**
```choicescript
*label check_reputation
*if (varkyrs_relation < 30)
    *comment Varkyrs hostile, block certain routes
*if (lupine_relation > 70)
    *comment Lupines offer aid in missions

*comment Reputation gates for:
  *comment - Shop prices
  *comment - Quest availability  
  *comment - Romance options
  *comment - Endings available
```

**Integration:** Called at start of major scenes

---

### 3.4 Act 2 Hub & Navigation

#### 🔴 **hub_city.txt** - Major Expansion
**Current State:** 200 lines, basic placeholder

**Required Additions:**
1. **Shop/Inventory System**
   - Buy blood vials (Varkyrs)
   - Silver weapons (Hunters)
   - Artifacts for all factions
   - Prices affected by reputation

2. **NPC Interactions**
   - Random encounters with romance NPCs
   - Faction recruiters
   - Questgivers

3. **Fast Travel**
   - Crimson Spire
   - Whispering Pines
   - Forsaken Underground
   - Human districts

4. **Time Advancement**
   - Rest (advance time, restore stats)
   - Training (gain XP)
   - Socializing (romance progress)

**Required Expansion:** ~400 lines

---

#### 🔴 **mission_board.txt** - Complete System
**Current State:** 200 lines, partial implementation

**Required Features:**
1. **Dynamic Quests**
   - 10+ side missions
   - Faction-specific contracts
   - Repeatable bounties
   - One-time events

2. **Quest Types:**
   - Assassination contracts
   - Escort missions
   - Item retrieval
   - Faction diplomacy
   - Monster hunts

3. **Rewards:**
   - XP (50-200 per mission)
   - Faction reputation
   - Money (for shop)
   - Unique items

**Required Expansion:** ~500 lines

---

## PHASE 4: ACT 3 & ENDGAME

**Duration:** 4-6 weeks  
**Priority:** MEDIUM  
**Status:** 🔴 Not Started

### 4.1 Act 3 Overview

**Setting:** Faction war at breaking point OR peace negotiations  
**Player Level:** Rank 6-9 (high-tier abilities)  
**Main Quest:** Ecliptic Amulet reunification  
**Content:** ~3,000 lines

**Core Themes:**
- Player's choices from Act 1-2 determine path
- Multiple faction endings
- Romance climaxes
- Ultimate power or peace
- Legacy choices

---

### 4.2 Required Act 3 Scenes

#### 🔴 **act3_war_path.txt** (NEW FILE)
**Estimated Lines:** 1,500+  
**Condition:** If player chose conflict in Act 2

**Required Content:**
1. **Final Battles**
   - Crimson Spire siege OR defense
   - Whispering Pines pack war
   - Forsaken uprising
   - Human resistance climax

2. **Ecliptic Amulet Completion**
   - Gather all 4 shards
   - Ritual to reunite artifact
   - Ultimate power unlock

3. **Boss Fights**
   - Rival faction leaders
   - Corrupted progenitor (if war path)
   - Ancient guardians

4. **Consequences**
   - Factions destroyed or subjugated
   - World state permanently altered
   - Romance partners' reactions

**Labels Needed:**
- `*label war_declaration`
- `*label final_siege`
- `*label amulet_ritual`
- `*label ultimate_power`
- `*label war_epilogue`

---

#### 🔴 **act3_peace_path.txt** (NEW FILE)
**Estimated Lines:** 1,500+  
**Condition:** If player chose diplomacy in Act 2

**Required Content:**
1. **Peace Summit**
   - Negotiate between all factions
   - Skill checks (cunning, will)
   - Ecliptic Amulet as peace symbol

2. **Sabotage Attempts**
   - Hardliners try to break peace
   - Player must stop assassinations
   - Prove cooperation possible

3. **New Pact**
   - Recreate Mirror Lake Pact
   - Establish new faction council
   - Veilfall Accord strengthened

4. **Consequences**
   - Uneasy peace maintained
   - Player as mediator/leader
   - Romance partners' reactions

**Labels Needed:**
- `*label peace_summit`
- `*label sabotage_defense`
- `*label new_pact`
- `*label peace_epilogue`

---

### 4.3 Endgame Scenarios

#### 🔴 **Ending_Scenarios.txt** - Expand Massively
**Current State:** Listed in root, content unknown

**Required Content:** 15+ unique endings based on:

**Faction Endings:**
1. **Varkyr Progenitor** - Ascend to mythic vampire
2. **Lupine Lunar Progenitor** - Become Origin Wolf reborn
3. **Forsaken Eclipse Lord** - Unite all hybrids
4. **Human Artifact Master** - Wield ancient power
5. **Assassin Guildmaster** - Control balance from shadows

**Alignment Endings:**
6. **Tyrant** - Conquer all factions (war path)
7. **Peacemaker** - Unite factions (peace path)
8. **Destroyer** - Destroy Ecliptic Amulet, end magic
9. **Neutral** - Maintain status quo, walk away

**Romance Endings:**
10. **Isabella Romance** - Rule Crimson Spire together
11. **Rurik Romance** - Lead united packs
12. **Caius Romance** - Forsaken new world order
13. **Skylar Romance** - Found new pack/independent
14. **Multiple Romances** - Consequences/harem path

**Special Endings:**
15. **Sacrifice** - Player dies for greater good
16. **Corruption** - Become villain, final boss fight
17. **Ascension** - Transcend mortality entirely
18. **Legacy** - NG+ setup, play as descendant

**Estimated Content:** ~1,500 lines total

---

## PHASE 5: ROMANCE & CHARACTER ARCS

**Duration:** 3-4 weeks  
**Priority:** MEDIUM  
**Status:** 🔴 Not Started

### 5.1 Romance System Overview

**Current State:** 13 NPCs defined, NO romance content written

**Required Features:**
- Relationship progression (0-100 scale)
- 4 romance stages per NPC
- Faction-specific romance mechanics
- Multiple romance support (consequences)
- Romance affects endings

---

### 5.2 Romance Content by NPC

Each romance requires **4 major scenes:**

1. **First Meeting/Introduction** (~150 lines)
   - Already partially covered in Act 1
   - Needs romance flag setup
   - Initial attraction/interest

2. **Act 2 Romance Development** (~200 lines)
   - 2-3 personal scenes
   - Relationship progression choices
   - Intimacy building
   - Approval thresholds

3. **Act 3 Romance Climax** (~150 lines)
   - Confession/commitment
   - Final relationship choice
   - Affects ending path

4. **Romance Ending** (~100 lines)
   - Integrated into epilogues
   - Unique per NPC + faction combo

**Total per NPC:** ~600 lines  
**Total for 13 NPCs:** ~7,800 lines

---

### 5.3 Priority Romance NPCs

#### HIGH PRIORITY (Core Routes):

##### 🔴 **Isabella Crimson** (Varkyr)
**File:** `romance/isabella_romance.txt` (NEW)  
**Estimated Lines:** 600+

**Romance Flavor:** Political alliance becomes genuine affection  
**Requirements:** Varkyr alignment, Viscount+ rank, varkyrs_relation 60+

**Key Scenes:**
- Act 2: Diplomatic mission together
- Act 2: Blood-sharing intimacy (Varkyr ritual)
- Act 3: Choose her vs faction loyalty
- Ending: Rule Crimson Spire together

---

##### 🔴 **Rurik Blackfang** (Lupine)
**File:** `romance/rurik_romance.txt` (NEW)  
**Estimated Lines:** 600+

**Romance Flavor:** Alpha finds equal, pack bonding  
**Requirements:** Lupine alignment, Beta+ rank, lupine_relation 70+

**Key Scenes:**
- Act 2: Hunt together under full moon
- Act 2: Pack bond ceremony (soul-deep connection)
- Act 3: Alpha challenge together vs apart
- Ending: Lead united packs as equals

---

##### 🔴 **Caius the Unbound** (Forsaken)
**File:** `romance/caius_romance.txt` (NEW)  
**Estimated Lines:** 600+

**Romance Flavor:** Mentor becomes partner, hybrid harmony  
**Requirements:** Forsaken alignment, Sentinel+ rank, hybrid_stability 70+

**Key Scenes:**
- Act 2: Caius reveals vulnerability/past
- Act 2: Eclipse ritual shared power
- Act 3: Choice: equal partners vs servant
- Ending: New world order for Forsaken

---

##### 🔴 **Skylar Ironclaw** (Lupine - Lone Wolf)
**File:** `romance/skylar_romance.txt` (NEW)  
**Estimated Lines:** 600+

**Romance Flavor:** Two outcasts find each other  
**Requirements:** Any alignment, met_Skylar, independent personality choices

**Key Scenes:**
- Act 2: Skylar helps player in crisis
- Act 2: Campfire honesty, shared exile
- Act 3: Found new pack together OR stay independent
- Ending: Freedom/adventure romance

---

#### MEDIUM PRIORITY:

- **Dante Ashwood** (Forsaken) - 600 lines
- **Mira Thornveil** (Forsaken) - 600 lines
- **Lucan Graves** (Human) - 600 lines
- **Nadia Winters** (Human) - 600 lines

#### LOWER PRIORITY:

- **Vincent Ashenheart** (Varkyr) - 600 lines
- **Cassandra Nightfall** (Varkyr) - 600 lines
- **Thane Silverpelt** (Lupine) - 600 lines
- **Rhea Moonshadow** (Lupine) - 600 lines
- **Adrian Blackwell** (Human) - 600 lines

---

### 5.4 Romance Mechanics

#### 🔴 **romance_system.txt** (NEW FILE)
**Estimated Lines:** 400+

**Required Features:**
```choicescript
*label romance_check
*comment Check if romance requirements met

*if (met_Isabella) and (Isabella_relation >= 60) and (alignment = "varkyrs")
    *comment Isabella romance available
    *set isabella_romance_available true

*label romance_scene
*comment Template for romance interactions

*choice
    #Flirt
        *set [NPC]_relation +5
    #Show affection
        *set [NPC]_relation +10
        *comment Requires relation 50+
    #Confess feelings
        *set [NPC]_relation +20
        *set [NPC]_romance true
        *comment Requires relation 70+
    #Remain professional
        *comment No change

*label romance_conflict
*comment If romancing multiple NPCs
*if (isabella_romance) and (rurik_romance)
    *comment Jealousy/drama scene
    *comment Must choose or face consequences
```

---

## PHASE 6: POLISH & TESTING

**Duration:** 2-3 weeks  
**Priority:** CRITICAL (before release)  
**Status:** 🔴 Not Started

### 6.1 Complete Codex

#### 🔴 **codex/codex_factions.txt** (NEW FILE)
**Estimated Lines:** 600+

**Required Content:**
- Varkyr Courts (Crimson Spire hierarchy)
- Lupine Packs (major packs, territories)
- Forsaken Enclave (Caius's organization)
- Assassin Guild (structure, code)
- Human Crown (monarchy, politics)
- Night Council (secret Varkyr cabal)
- Church (monster hunters)
- Silver Legion (human army)

**Format:** Same as codex_races.txt (detailed entries with lore)

---

#### 🔴 **codex/codex_locations.txt** (NEW FILE)
**Estimated Lines:** 500+

**Required Content:**
- Veilfall City (districts, history)
- Mirror Lake (Pact site, significance)
- Whispering Pines Forest (Lupine territory)
- Crimson Spire (Varkyr citadel)
- Forsaken Underground (tunnel network)
- Greyhaven (Council location)
- The Warren (slums)
- Cathedral Heights (Church stronghold)

**Format:** Description, history, significance, current state

---

#### 🔴 **codex/codex_characters.txt** (NEW FILE)
**Estimated Lines:** 800+

**Required Content:**
- All 13 romance NPCs (detailed profiles)
- Caius the Unbound (expanded)
- The Progenitor (historical)
- The Origin Wolf (historical)
- Guild Master (mysterious)
- The Matriarch (Varkyr leader)
- Notable historical figures
- Legendary war heroes

**Format:** Like current stats screen NPC entries, but more lore

---

### 6.2 Testing & Debugging

#### 🔴 **Expand tests/test_gotos.py**
**Current State:** Basic scene/goto checks

**Required Tests:**
1. All scenes in scene_list exist
2. All `*goto` targets have matching `*label`
3. All `*goto_scene` targets exist
4. No infinite loops
5. All variables defined before use
6. All ability flags checked before use

**New Test Functions:**
```python
def test_all_labels_reachable():
    """Ensure no orphaned labels"""
    pass

def test_variable_initialization():
    """All used variables exist in startup.txt"""
    pass

def test_ability_flags():
    """All ability checks use valid flags"""
    pass
```

---

#### 🔴 **Manual Playtesting Checklist**

**Full Playthrough Tests:**
- [ ] Each origin (7 total) to Act 1 completion
- [ ] Each Act 1 route to Act 2
- [ ] Each Act 2 faction path to Act 3
- [ ] War path to ending
- [ ] Peace path to ending
- [ ] At least 5 different endings
- [ ] Each romance route to completion
- [ ] Rank progression works in all scenes
- [ ] Ability selection at each rank
- [ ] Abilities usable in combat
- [ ] Stats affect choices properly
- [ ] Codex accessible and complete
- [ ] No undefined variables crash
- [ ] No infinite loops
- [ ] Time passage works correctly
- [ ] Moon phases cycle properly
- [ ] Blood satiation drains/feeds work
- [ ] Hybrid stability functions

---

### 6.3 Balance Tuning

#### 🔴 **Balance Document** (NEW)
**File:** `BALANCE_GUIDE.md`

**Required Analysis:**
- XP gain rates (ensure players rank up 2-3 times per act)
- Ability power scaling (higher ranks clearly stronger)
- Combat difficulty curves
- Stat check thresholds (not too hard/easy)
- Romance progression rates
- Reputation gain/loss amounts
- Blood satiation drain rates
- Moon phase strength modifiers

**Testing Method:**
- Playtest each route
- Record XP earned, ranks achieved
- Identify too-easy/too-hard checks
- Adjust values in startup.txt and scenes

---

### 6.4 Polish Tasks

#### 🔴 **Narrative Polish**
- [ ] Proofread all content for typos
- [ ] Consistency check (NPC names, titles)
- [ ] Tone consistency (dark fantasy maintained)
- [ ] Flow check (transitions smooth)
- [ ] No plot holes or contradictions

#### 🔴 **Technical Polish**
- [ ] Remove debug comments
- [ ] Clean up old code
- [ ] Optimize long scenes (split if >1000 lines)
- [ ] Add *page_break at natural points
- [ ] Add *line_break for readability

#### 🔴 **UI/UX Polish**
- [ ] Stats screen complete and clear
- [ ] Codex well-organized
- [ ] Choice formatting consistent
- [ ] Important choices bolded
- [ ] Relationship meters clear

---

## INCOMPLETE SYSTEMS & FEATURES

### Critical Systems Missing

#### 🔴 **Inventory System**
**Status:** Not implemented  
**Needed For:** Act 2-3 shops, item quests

**Required Implementation:**
```choicescript
*comment In startup.txt:
*create money 100
*create inventory ""  *comment semicolon-separated list

*comment Example items:
*create has_silver_dagger false
*create has_blood_vial false
*create has_uv_flashlight false
*create has_ecliptic_shard_1 false
```

**Required Scenes:**
- `systems/inventory.txt` (~300 lines)
  - Add item
  - Remove item
  - Check if has item
  - Use item

---

#### 🔴 **Combat System**
**Status:** Narrative only, no mechanics  
**Needed For:** Major battles, balance

**Required Implementation:**
- Health/damage tracking (optional)
- Ability cooldowns (optional)
- Enemy AI patterns
- Victory/defeat conditions
- Flee option

**Recommendation:** Keep narrative-focused, add stat checks for success/failure

---

#### 🔴 **Saving/Loading**
**Status:** ChoiceScript handles automatically  
**Action Required:** None (built-in)

---

#### 🔴 **Achievements**
**Status:** Not implemented  
**Priority:** Low (optional)

**If Implemented:**
```choicescript
*achievement vampire_lord visible Vampire Lord
    Reached Progenitor rank as Varkyr

*achievement peacemaker visible Peacemaker
    United all factions peacefully
```

---

### Partially Implemented Systems

#### 🟡 **Moon Phase System**
**Status:** Variable exists, needs automation

**Required:** Auto-advance in time_passage.txt

---

#### 🟡 **Blood Satiation System**
**Status:** Variable exists, needs drain/feed scenes

**Required:** 
- Feed scenes in act2/act3
- Auto-drain in time_passage.txt
- Frenzy risk at low satiation

---

#### 🟡 **Hybrid Stability System**
**Status:** Variable exists, needs consequences

**Required:**
- Stability loss from conflict
- Stability gain from balance
- War Form instability
- Death risk if too unstable

---

## MISSING CONTENT BREAKDOWN

### By Category

#### Origins
- ✅ origin_noble.txt (created, multi-route to human/varkyr/lupine)
- ✅ origin_commoner.txt (created, survival start with all faction routes)
- ✅ origin_hunter.txt (created, advanced hunt origin with faction pivots)
- 🟡 origin_assassin.txt (refactor prologue, +100 lines)
- 🟡 origin_varkyr.txt (+150 lines endgame polish)
- 🟡 origin_lupine.txt (+100 lines endgame polish)
- 🟡 origin_forsaken.txt (+150 lines endgame polish)

**Total New Origin Content:** ~500 lines

---

#### Act 1
- ✅ act1_varkyr.txt (endgame complete, XP integrated)
- ✅ act1_lupine.txt (endgame complete, XP integrated)
- ✅ act1_human.txt (complete rebuild with Legion conspiracy)
- ✅ act1_forsaken_ng+.txt (complete rebuild with Forsaken trials)

**Total Act 1 Content:** Complete; minor polish/XP sync remaining (~500 lines)

---

#### Act 2
- 🟡 act2_common_hub.txt (+400 lines)
- ❌ act2_varkyr_court.txt (1,200 lines)
- ❌ act2_lupine_territory.txt (1,200 lines)
- ❌ act2_forsaken_underground.txt (1,000 lines)
- ❌ act2_human_resistance.txt (1,000 lines)
- 🟡 hub_city.txt (+400 lines)
- 🟡 mission_board.txt (+500 lines)

**Total Act 2 Content:** ~5,700 lines

---

#### Act 3
- ❌ act3_war_path.txt (1,500 lines)
- ❌ act3_peace_path.txt (1,500 lines)
- 🟡 Ending_Scenarios.txt (+1,500 lines expansion)

**Total Act 3 Content:** ~4,500 lines

---

#### Romance
- ❌ 13 NPC romance files (~7,800 lines total)
- ❌ romance_system.txt (400 lines)

**Total Romance Content:** ~8,200 lines

---

#### Systems
- ❌ time_passage.txt (200 lines)
- ❌ ability_equip.txt (300 lines)
- ❌ reputation_effects.txt (150 lines)
- ❌ inventory.txt (300 lines)

**Total Systems Content:** ~950 lines

---

#### Codex
- ✅ codex_factions.txt (created)
- ✅ codex_locations.txt (created)
- ✅ codex_characters.txt (created)

**Total Codex Content:** Completed

---

### Grand Total New Content Required

**Lines to Write:** ~23,800 lines of ChoiceScript  
**Current Codebase:** ~8,000 lines  
**Final Size:** ~31,800 lines

**Estimated Writing Time:**
- 50 lines/hour (average ChoiceScript writing speed)
- 476 hours total
- ~12 weeks at 40 hrs/week
- **Realistic Timeline:** 16-20 weeks (4-5 months)

---

## FILE CREATION CHECKLIST

### 📋 Origins (7 files)

- [x] origins/origin_noble.txt
- [x] origins/origin_commoner.txt
- [x] origins/origin_hunter.txt
- [ ] origins/origin_assassin.txt (refactor from prologue)
- [ ] Complete origins/origin_varkyr.txt
- [ ] Complete origins/origin_lupine.txt
- [ ] Complete origins/origin_forsaken.txt

### 📋 Act 1 (4 files)

- [ ] Complete act1_varkyr.txt
- [ ] Complete act1_lupine.txt
- [ ] Complete act1_human.txt
- [ ] Create act1_forsaken.txt (replace act1_forsaken_ng+.txt)

### 📋 Act 2 (7 files)

- [ ] Expand act2_common_hub.txt
- [ ] Create act2_varkyr_court.txt
- [ ] Create act2_lupine_territory.txt
- [ ] Create act2_forsaken_underground.txt
- [ ] Create act2_human_resistance.txt
- [ ] Expand hub_city.txt
- [ ] Complete mission_board.txt

### 📋 Act 3 (3 files)

- [ ] Create act3_war_path.txt
- [ ] Create act3_peace_path.txt
- [ ] Expand Ending_Scenarios.txt

### 📋 Romance (14 files)

- [ ] Create romance/isabella_romance.txt
- [ ] Create romance/rurik_romance.txt
- [ ] Create romance/caius_romance.txt
- [ ] Create romance/skylar_romance.txt
- [ ] Create romance/dante_romance.txt
- [ ] Create romance/mira_romance.txt
- [ ] Create romance/lucan_romance.txt
- [ ] Create romance/nadia_romance.txt
- [ ] Create romance/vincent_romance.txt
- [ ] Create romance/cassandra_romance.txt
- [ ] Create romance/thane_romance.txt
- [ ] Create romance/rhea_romance.txt
- [ ] Create romance/adrian_romance.txt
- [ ] Create romance_system.txt

### 📋 Systems (4 files)

- [ ] Create systems/time_passage.txt
- [ ] Create systems/ability_equip.txt
- [ ] Create systems/reputation_effects.txt
- [ ] Create systems/inventory.txt

### 📋 Codex (3 files)

- [x] Create codex/codex_factions.txt
- [x] Create codex/codex_locations.txt
- [x] Create codex/codex_characters.txt

### 📋 Documentation (2 files)

- [ ] Create BALANCE_GUIDE.md
- [ ] Update PROJECT_STATUS.md when complete

---

## SCENE FLOW ARCHITECTURE

### Full Game Flow (Complete)

```
startup.txt
    ↓
origin_select.txt
    ↓
[Choose one of 7 origins]
    ↓
├─ origin_assassin.txt → act1_forsaken/lupine/varkyr
├─ origin_noble.txt → act1_human/varkyr/lupine
├─ origin_commoner.txt → act1_forsaken/human
├─ origin_varkyr.txt → act1_varkyr
├─ origin_lupine.txt → act1_lupine
├─ origin_forsaken.txt → act1_forsaken
└─ origin_hunter.txt → act1_human/varkyr/lupine/forsaken
    ↓
[Act 1 - Faction Introduction]
    ↓
├─ act1_varkyr.txt
├─ act1_lupine.txt
├─ act1_human.txt
└─ act1_forsaken.txt
    ↓
[All routes merge]
    ↓
act2_common_hub.txt
    ↓
[Choose faction path]
    ↓
├─ act2_varkyr_court.txt
├─ act2_lupine_territory.txt
├─ act2_forsaken_underground.txt
└─ act2_human_resistance.txt
    ↓
[Choice: War or Peace]
    ↓
├─ act3_war_path.txt
└─ act3_peace_path.txt
    ↓
Ending_Scenarios.txt
    ↓
[15+ unique endings]
```

### Hub Access Points

```
hub_city.txt (accessible from Act 2+)
    ├─ mission_board.txt
    ├─ shop (inventory system)
    ├─ NPC interactions (romance)
    ├─ Fast travel
    └─ Time passage (rest/train)
```

### Systems Called from Scenes

```
Any combat/mission scene
    ↓
rank_progression.txt
    ├─ gain_xp
    └─ check_progression
        ↓
    [If rank-up earned]
        ↓
    varkyr_abilities.txt / lupine_abilities_complete.txt / forsaken_abilities.txt
        ↓
    [Player selects 2 new abilities]
        ↓
    [Return to calling scene]
```

---

## TESTING & QUALITY ASSURANCE

### Test Priority Matrix

| Test Type | Priority | Status | Owner |
|-----------|----------|--------|-------|
| Origin playthrough (7x) | Critical | ❌ | Dev team |
| Act 1 completion (4x) | Critical | ❌ | Dev team |
| Rank progression | Critical | ❌ | Dev team |
| Ability selection | Critical | ❌ | Dev team |
| Act 2 paths (4x) | High | ❌ | Dev team |
| Romance routes (13x) | High | ❌ | Beta testers |
| Endings (15+) | High | ❌ | Beta testers |
| Stats balance | Medium | ❌ | Beta testers |
| Codex completion | Medium | ❌ | Beta testers |
| Combat balance | Low | ❌ | Beta testers |

### Testing Phases

#### Phase 1: Unit Testing (Week 1)
- [ ] All `*goto` targets exist
- [ ] All variables initialized
- [ ] No syntax errors
- [ ] Python tests pass

#### Phase 2: Feature Testing (Week 2)
- [ ] Origin selection works
- [ ] Rank progression grants XP
- [ ] Abilities unlock at correct ranks
- [ ] Stats affect choices
- [ ] Codex accessible

#### Phase 3: Integration Testing (Week 3)
- [ ] Full origin → Act 1 → Act 2 playthrough
- [ ] Romance progression functional
- [ ] Faction relations affect outcomes
- [ ] Time passage works
- [ ] Inventory works

#### Phase 4: Balance Testing (Week 4)
- [ ] Players rank up 2-3x per act
- [ ] Stat checks feel fair
- [ ] Combat difficulty appropriate
- [ ] XP gains balanced

#### Phase 5: Beta Testing (Weeks 5-6)
- [ ] External playtesters
- [ ] Feedback collection
- [ ] Bug reports
- [ ] Balance tweaks

#### Phase 6: Final QA (Week 7)
- [ ] All bugs fixed
- [ ] All content proofread
- [ ] Final balance pass
- [ ] Release candidate

---

## RECOMMENDED DEVELOPMENT ORDER

### Priority 1 (Weeks 1-4): Foundation
1. Complete 3 missing origins (Noble, Commoner, Hunter)
2. Refactor prologue → origin_assassin.txt
3. Complete 4 origin endgames (Varkyr, Lupine, Forsaken, Assassin)
4. Integrate rank_progression into Act 1 scenes
5. Complete Act 1 endgames (all 4 routes)

**Deliverable:** Playable from any origin through Act 1

---

### Priority 2 (Weeks 5-8): Act 2 Core
1. Expand act2_common_hub.txt
2. Create time_passage.txt system
3. Create act2_varkyr_court.txt
4. Create act2_lupine_territory.txt
5. Expand hub_city.txt and mission_board.txt

**Deliverable:** Playable through Act 2 (2 of 4 paths)

---

### Priority 3 (Weeks 9-12): Act 2 Complete & Systems
1. Create act2_forsaken_underground.txt
2. Create act2_human_resistance.txt
3. Create ability_equip.txt
4. Create reputation_effects.txt
5. Create inventory.txt

**Deliverable:** Full Act 2 playable with systems

---

### Priority 4 (Weeks 13-16): Act 3 & Endings
1. Create act3_war_path.txt
2. Create act3_peace_path.txt
3. Expand Ending_Scenarios.txt (15+ endings)
4. Complete codex (3 files)

**Deliverable:** Full game playable to completion

---

### Priority 5 (Weeks 17-20): Romance & Polish
1. Create 4 priority romance files (Isabella, Rurik, Caius, Skylar)
2. Create romance_system.txt
3. Create remaining 9 romance files
4. Narrative polish and proofreading
5. Balance tuning

**Deliverable:** Complete game with romance

---

### Priority 6 (Weeks 21-22): Testing & Release
1. Full playtesting (all routes)
2. Bug fixes
3. Final balance pass
4. Documentation cleanup
5. Release preparation

**Deliverable:** Version 1.0.0 ready for release

---

## APPENDICES

### Appendix A: Naming Conventions

**Files:**
- Origins: `origin_[type].txt`
- Acts: `act[#]_[faction/descriptor].txt`
- Romance: `romance/[name]_romance.txt`
- Systems: `systems/[function].txt`
- Codex: `codex/codex_[category].txt`

**Labels:**
- Entry points: `*label [descriptor]_start` or `*label [descriptor]_entry`
- Sub-sections: `*label [descriptor]_[action]`
- Endings: `*label [descriptor]_end` or `*label [descriptor]_finale`

**Variables:**
- Stats: lowercase (`strength`, `agility`)
- Relations: `[faction]_relation` or `[NPC]_relation`
- Flags: descriptive (`met_Isabella`, `has_artifact`)
- Abilities: `[ability_name]` (e.g., `shadow_step`)

---

### Appendix B: XP Recommendations

| Task Difficulty | XP Reward | Example |
|-----------------|-----------|---------|
| Trivial | 10-25 | Dialogue choice, minor discovery |
| Easy | 25-50 | Complete conversation, find item |
| Standard | 50-100 | Complete minor quest, win minor fight |
| Moderate | 100-150 | Complete mission, win major fight |
| Hard | 150-250 | Complete major quest, defeat boss |
| Epic | 250-500 | Act completion, unite factions |

**Rank-up Thresholds (Recommended):**
- Commoner → Knight: 100 XP
- Knight → Baron/Baroness: 250 XP
- Baron/Baroness → Viscount/Viscountess: 500 XP
- Viscount/Viscountess → Count/Countess: 1,000 XP
- Count/Countess → Marquis/Marchioness: 2,000 XP
- Marquis/Marchioness → Duke/Duchess: 4,000 XP
- Duke/Duchess → Archduke/Archduchess: 8,000 XP
- Archduke/Archduchess → Imperial: 15,000 XP

---

### Appendix C: Stat Check Difficulty

| Check Type | Easy | Medium | Hard | Very Hard |
|------------|------|--------|------|-----------|
| Strength | 30 | 50 | 70 | 90 |
| Agility | 30 | 50 | 70 | 90 |
| Cunning | 30 | 50 | 70 | 90 |
| Will | 30 | 50 | 70 | 90 |
| Relation | 30 | 50 | 70 | 90 |

**Recommendation:** Most checks should be Medium (50), scaling to Hard (70) in Act 3

---

### Appendix D: Romance Progression Thresholds

| Stage | Relation Score | Description |
|-------|----------------|-------------|
| Met | 0-30 | Introduced, neutral/curious |
| Friendly | 30-50 | Positive interactions, trust building |
| Interested | 50-70 | Romantic tension, flirtation |
| Committed | 70-90 | Confession, relationship established |
| Devoted | 90-100 | Deep love, ending-level commitment |

**Romance Availability:** Requires 60+ relation and specific faction/alignment

---

### Appendix E: Writing Style Guide

**Tone:** Dark fantasy, morally grey, consequences-focused  
**Perspective:** Second person ("you")  
**Tense:** Present tense  
**Formatting:**
- Use `[b]bold[/b]` for important terms
- Use `[i]italics[/i]` for internal thoughts, emphasis
- Use `*page_break` every 300-500 lines
- Use `*line_break` between major paragraphs

**Avoid:**
- Modern slang
- Meta references
- Breaking 4th wall
- Excessive exposition dumps

**Embrace:**
- Player agency
- Meaningful choices
- Brutal consequences
- Dark atmosphere

---

## FINAL NOTES

This roadmap represents **everything needed** to complete Bloodline Requiem. The current foundation (Phase 1) is solid—systems work, architecture is sound, documentation is comprehensive.

**The path forward is clear:**
1. Complete origins (3-4 weeks)
2. Finish Act 1 (1-2 weeks)
3. Build Act 2 (6-8 weeks)
4. Create Act 3 & endings (4-6 weeks)
5. Add romance (3-4 weeks)
6. Polish & test (2-3 weeks)

**Estimated Total Time:** 19-27 weeks (4.5-6 months)

**At 40 hours/week:** Achievable in 5-6 months  
**At 20 hours/week:** Achievable in 10-12 months  
**At 10 hours/week:** Achievable in 20-24 months

The game is **40% complete** (systems and foundation). The remaining **60%** is content creation using those systems.

**You have everything you need to succeed.** The frameworks are built. The lore is rich. The architecture is scalable. Now it's time to write the story.

---

**Document Version:** 1.0  
**Last Updated:** December 6, 2025  
**Next Review:** After Phase 2 completion

---

*"Every legend begins with a choice. Every bloodline has an origin. Every shadow was once cast by light."*

—Bloodline Requiem
