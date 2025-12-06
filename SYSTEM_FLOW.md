# BLOODLINE REQUIEM - SYSTEM FLOW DIAGRAM

## Game Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       STARTUP.TXT                           │
│  - Initialize all variables                                 │
│  - Load scene_list                                          │
│  - Begin game → ORIGIN SELECT                              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              ORIGIN SELECTION (Future)                      │
│  ┌──────────┬──────────┬──────────┬──────────┐            │
│  │ Assassin │  Noble   │ Commoner │  Varkyr  │            │
│  │  Human   │  Human   │  Human   │ Initiate │            │
│  └──────────┴──────────┴──────────┴──────────┘            │
│  ┌──────────┬──────────┬──────────────────────┐            │
│  │ Lupine   │ Forsaken │   Hunter             │            │
│  │  Omega   │ Recruit  │   (Advanced)         │            │
│  └──────────┴──────────┴──────────────────────┘            │
│                     │                                       │
│          Each origin sets:                                  │
│          - alignment (varkyrs/lupine/forsaken/human)       │
│          - rank or lupine_rank                             │
│          - starting abilities                               │
│          - faction relations                                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    ACT 1: UNVEILING SHADOWS                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  FACTION-SPECIFIC ROUTES                             │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐    │  │
│  │  │  Varkyr    │  │  Lupine    │  │  Forsaken  │    │  │
│  │  │  Route     │  │  Route     │  │  Route     │    │  │
│  │  │            │  │            │  │            │    │  │
│  │  │ Crimson    │  │ Moon-Born  │  │  Caius's   │    │  │
│  │  │  Spire     │  │   Trial    │  │  Ritual    │    │  │
│  │  │ Initiation │  │            │  │            │    │  │
│  │  └────┬───────┘  └────┬───────┘  └────┬───────┘    │  │
│  │       │               │               │             │  │
│  │       └───────────────┼───────────────┘             │  │
│  │                       │                             │  │
│  │  COMMON MISSIONS & ENCOUNTERS                       │  │
│  │  - Investigate Mirror Lake                          │  │
│  │  - Faction diplomacy                                │  │
│  │  - First major choice (shape Act 2)                 │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 ACT 2: WAR OF BLOOD AND MOON                │
│  - Faction wars escalate                                    │
│  - Ecliptic Amulet shard quests                            │
│  - Romance progression                                      │
│  - Territory control (if high rank)                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 ACT 3: REQUIEM & REBUILD                    │
│  - Final confrontations                                     │
│  - Amulet reunification decision                           │
│  - Faction fates sealed                                     │
│  - Epilogues based on:                                      │
│    • MC's race & rank                                       │
│    • Romances                                               │
│    • Faction outcomes                                       │
│    • Amulet decision                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Ability System Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    RANK PROGRESSION                         │
│                                                             │
│  Player gains XP through:                                   │
│  - Completing missions                                      │
│  - Winning faction favor                                    │
│  - Consuming powerful blood (Varkyrs)                       │
│  - Passing pack trials (Lupines)                            │
│  - Stabilizing hybrid form (Forsaken)                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   RANK-UP TRIGGERED                         │
│                                                             │
│  *set rank "Knight"  (Varkyr example)                       │
│                                                             │
│  *gosub_scene varkyr_abilities varkyr_ability_select        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               ABILITY SELECTION SCREEN                      │
│                                                             │
│  The blood sings with newfound power.                       │
│  Choose TWO abilities from Knight rank:                     │
│                                                             │
│  ┌───────────────────┐  ┌───────────────────┐             │
│  │ Combat Mastery    │  │ Animal Command    │             │
│  └───────────────────┘  └───────────────────┘             │
│  ┌───────────────────┐  ┌───────────────────┐             │
│  │ Blood Bond        │  │ Shadow Step       │             │
│  └───────────────────┘  └───────────────────┘             │
│                                                             │
│  Player picks 2 → Booleans set to TRUE                     │
│  (enhanced_strength = true, shadow_step = true)            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│             ABILITIES AVAILABLE IN SCENES                   │
│                                                             │
│  *if (shadow_step)                                          │
│      #Use Shadow Step to flank enemy                        │
│          You dissolve into shadows!                         │
│          *goto shadow_flank                                 │
│                                                             │
│  Combat effectiveness scales with:                          │
│  - Rank (higher = more abilities)                           │
│  - Bloodlust/Rage/Control stats                            │
│  - Faction relations                                        │
│  - Moon phase (Lupines)                                     │
│  - Recent feeding (Varkyrs)                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Codex Navigation Flow

```
┌─────────────────────────────────────────────────────────────┐
│              STATS SCREEN (choicescript_stats.txt)          │
│                                                             │
│  Strength: ████████░░ 80%                                   │
│  Agility:  ██████░░░░ 60%                                   │
│                                                             │
│  ┌──────────────────────────────────┐                      │
│  │ View Character Relationships     │                      │
│  │ Codex / Lore              ◄──────┼─── Click here       │
│  │ Return                           │                      │
│  └──────────────────────────────────┘                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                CODEX MAIN (codex_main.txt)                  │
│                                                             │
│  What secrets do you seek?                                  │
│                                                             │
│  ┌─────────────────────────┐  ┌─────────────────────────┐ │
│  │ World History           │  │ Races of the Night      │ │
│  └────────┬────────────────┘  └────────┬────────────────┘ │
│           │                             │                  │
│  ┌────────┴────────────────┐  ┌────────┴────────────────┐ │
│  │ Factions & Powers       │  │ Locations of Veilfall   │ │
│  └─────────────────────────┘  └─────────────────────────┘ │
│                                                             │
│  ┌─────────────────────────┐  ┌─────────────────────────┐ │
│  │ Notable Individuals     │  │ The Ecliptic Amulet     │ │
│  └─────────────────────────┘  └─────────────────────────┘ │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┼───────────┬───────────────┐
         ▼           ▼           ▼               ▼
┌───────────┐  ┌──────────┐  ┌─────────┐  ┌──────────────┐
│ World     │  │ Races    │  │Factions │  │ Locations    │
│ History   │  │          │  │ (TODO)  │  │ (TODO)       │
│           │  │          │  └─────────┘  └──────────────┘
│ Timeline  │  │ Varkyrs  │
│ Pact Era  │  │ Lupines  │
│ War       │  │ Forsaken │
│ Post-War  │  │ Humans   │
└───────────┘  └──────────┘
```

---

## File Dependencies Map

```
startup.txt
    ├─► prologue.txt (current start)
    │
    ├─► systems/
    │   ├─► varkyr_abilities.txt (called via *gosub_scene)
    │   ├─► lupine_abilities_complete.txt (called via *gosub_scene)
    │   ├─► forsaken_abilities.txt (called via *gosub_scene)
    │   └─► power_tier_calc.txt (called in startup)
    │
    ├─► codex/
    │   ├─► codex_main.txt (called from stats screen)
    │   │   ├─► codex_world.txt
    │   │   ├─► codex_races.txt
    │   │   ├─► codex_factions.txt (TODO)
    │   │   ├─► codex_locations.txt (TODO)
    │   │   └─► codex_characters.txt (TODO)
    │   │
    │
    ├─► scenes/
    │   ├─► act1_varkyr.txt
    │   ├─► act1_lupine.txt
    │   ├─► act1_human.txt
    │   └─► act1_forsaken_ng+.txt
    │
    └─► choicescript_stats.txt → codex_main.txt
```

---

## Variable Inheritance & Checks

### Varkyr Example:

```
STARTUP.TXT initializes:
├─ alignment = ""
├─ rank = ""
├─ Bloodlust = 0
├─ control = 100
└─ All ability flags = false

ORIGIN/SCENE sets:
├─ alignment = "varkyrs"
├─ rank = "Commoner"
└─ Calls varkyr_abilities.txt

VARKYR_ABILITIES.TXT:
├─ Player chooses 2 from Commoner tier
├─ Sets flags: enhanced_strength = true, night_vision = true
└─ Updates unlocked_abilities string

RANK-UP (Commoner → Knight):
├─ rank = "Knight"
├─ Calls varkyr_abilities.txt again
├─ Player chooses 2 from Knight tier
├─ Sets flags: shadow_step = true, blood_bond = true
└─ Player now has 4 abilities total (inherits Commoner + adds Knight)

COMBAT SCENE checks:
*if (shadow_step)
    #Use Shadow Step
        [available because flag = true]
```

---

## Stat Screen Display Logic

```
choicescript_stats.txt reads:

*if (alignment = "varkyrs")
    *stat_chart
        opposed_pair control Control
            Control
            Bloodlust
        text rank Rank
        text humans_turned Humans Turned

*if (alignment = "lupine")
    *stat_chart
        opposed_pair control Control
            Control
            Rage
        text lupine_rank Rank
        text wolfs_turned Wolves Turned

*if (alignment = "forsaken")
    *stat_chart
        text forsaken_rank Rank
        text forsaken_type Type
        opposed_pair control Control
            Control
            Hybrid Instability
```

---

## Integration Points for Future Systems

### 1. Moon Phase System
```
*create moon_phase "Full"

*if (alignment = "lupine") and (moon_phase = "Full")
    All Lupine abilities gain +50% effectiveness
*elseif (moon_phase = "New")
    All Lupine abilities -30% effectiveness
```

### 2. Blood Satiation (Varkyrs)
```
*create blood_satiation 100

*if (blood_satiation < 30)
    *set Bloodlust +20
    You struggle to focus. The thirst claws at your mind.

*if (shadow_step) and (blood_satiation > 70)
    Shadow Step range doubled when well-fed.
```

### 3. Hybrid Stability (Forsaken)
```
*create hybrid_stability 50

*if (hybrid_stability < 30)
    Risk of losing control; War Form becomes unstable

*if (ecliptic_surge) and (hybrid_stability < 50)
    Ecliptic Surge may backfire, damaging you as well
```

### 4. Faction Reputation Gates
```
*if (varkyrs_relation > 70) and (rank = "Baron")
    #Request audience with the Matriarch
        Your reputation grants access to the Crimson Spire's inner sanctum.

*if (lupine_relation < 30)
    Lupine packs attack on sight. Whispering Pines is closed to you.
```

---

## Testing Scenarios

### Scenario 1: Varkyr Commoner → Knight
1. Start game → Origin: Varkyr
2. alignment = "varkyrs", rank = "Commoner"
3. Choose Enhanced Strength + Night Vision
4. Complete mission → Gain XP
5. Trigger rank-up: rank = "Knight"
6. Choose Shadow Step + Blood Bond
7. Test combat: Shadow Step option appears
8. ✅ SUCCESS if no errors and ability works

### Scenario 2: Lupine Omega → Zeta Scout
1. Start game → Origin: Lupine
2. alignment = "lupine", lupine_rank = "Omega"
3. Choose type: omega_variant = true
4. Choose Lunar Infusion + Primal Resurgence
5. Complete pack trial
6. Trigger rank-up: lupine_rank = "Zeta Scout"
7. Choose Pack's Bond + Scent Mastery
8. Test during full moon: powers amplified
9. ✅ SUCCESS if moon phase affects strength

### Scenario 3: Forsaken Initiate → Adept
1. Start game → Origin: Forsaken
2. alignment = "forsaken", forsaken_rank = "Initiate"
3. Choose forsaken_type = "Vamp-Wolf"
4. Choose Twilight Veil + Enhanced Strength (Varkyr tree)
5. Complete Caius's trial
6. Trigger rank-up: forsaken_rank = "Adept"
7. Choose Sanguine Howl + Lunar Infusion (Lupine tree)
8. Test: Use both blood AND lunar abilities
9. ✅ SUCCESS if hybrid versatility works

---

## Quick Reference: Where to Find Things

**Want to add a new Varkyr ability?**
→ `systems/varkyr_abilities.txt` → Find appropriate rank section → Add choice

**Want to add new lore entry?**
→ `codex/codex_*.txt` files → Add *choice option and *label

**Want to create new origin?**
→ `origins/origin_*.txt` → Set initial stats → Route to Act 1

**Want to add ability usage in combat?**
→ Your scene file → `*if (ability_name)` → `#Use [ability]` choice

**Want to track a new stat?**
→ `startup.txt` → `*create stat_name initial_value`
→ `choicescript_stats.txt` → Add to appropriate section

---

**End of System Flow Diagram**
