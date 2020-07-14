# base power of all pokemon moves
# multi hit calculation
# avg. power = (2 * power * .375)+(3 * power * .375)+(4 * power * .125)+(5 * power * .125) ]
#            = 3 * power
# move Slam is not listed in if statements

def basePower(move):
    if move == 'Constrict':
        power = 10
    elif move == 'Wrap' or move == 'Poison Sting' or move == 'Bind':
        power = 15
    elif move == 'Infestation' or move == 'Leech Life' or move == 'Mud-Slap' or move == 'Nuzzle' or \
            move == 'Power Trip' or move == 'Rage' or move == 'Rapid Spin' or move == 'Stored Power':
        power = 20
    elif move == 'Astonish' or move == 'Feint' or move == 'Ice Ball' or move == 'Lick' or \
            move == 'Rollout' or move == 'Smog':
        power = 30
    elif move == 'Clamp' or move == 'Fire Spin' or move == 'Peck' or move == 'Sand Tomb'\
            or move == 'Snap Trap' or move == 'Whirlpool':
        power = 35
    elif move == 'Accelerock' or move == 'Acid' or move == 'Acid Spray' or move == 'Aqua Jet' or move == 'Branch Poke' \
            or move == 'Bubble' or move == 'Bullet Punch' or move == 'Disarming Voice' \
            or move == 'Echoed Voice' or move == 'Ember' or move == 'Fairy Wind' or move == 'Fake Out'\
            or move == 'False Swipe' or move == 'Fury Cutter' or move == 'Gust' or move == 'Hold Back'\
            or move == 'Ice Shard' or move == 'Leafage' or move == 'Mach Punch' or move == 'Mega Drain'\
            or move == 'Pay Day' or move == 'Pound' or move == 'Powder Snow' or move == 'Power-Up Punch' \
            or move == 'Pursuit' or move == 'Quick Attack' or move == 'Rock Smash' or move == 'Scratch' \
            or move == 'Shadow Sneak' or move == 'Tackle' or move == 'Thunder Shock' or move == 'Twister' \
            or move == 'Vacuum Wave' or move == 'Water Gun' or move == 'Dig' \
            or move == 'Razor Wind' or move == 'Dive' :
        power = 40
    elif move == 'Bounce':
        power = 42.5
    elif move == 'Vine Whip' or move == 'Arm Thrust' or move == 'Barrage' or move == 'Double Slap' \
            or move == 'Fury Attack' or move == 'Water Shuriken':
        power = 45
    elif move == 'Charge Beam' or move == 'Clear Smog' or move == 'Confusion' \
            or move == 'Cut' or move == 'Draining Kiss' or move == 'Fell Stinger' or move == 'Fly' \
            or move == 'Flame Charge' or move == 'Karate Chop' or move == 'Metal Claw' or move == 'Payback' \
            or move == 'Poison Fang' or move == 'Poison Tail' or move == 'Rapid Spin' or move == 'Rock Throw' \
            or move == 'Smack Down' or move == 'Snore' or move == 'Struggle Bug' or move == 'Terrain Pulse' \
            or move == 'Weather Ball' or move == 'Twineedle':
        power = 50
    elif move == 'Comet Punch' or move == 'Fury Swipes':
        power = 54
    elif move == 'Electroweb' or move == 'Icy Wind' or move == 'Mud Shot' or move == 'Razor Leaf' \
            or move == 'Snarl' or move == 'Acrobatics' or move == 'Vise Grip':
        power = 55
    elif move == 'Rolling Kick' or move == 'Circle Throw' or move == 'Dragon Tail' or move == 'Air Cutter' \
            or move == 'Rock Tomb' or move == 'Ancient Power' or move == 'Assurance' or move == 'Avalanche'\
            or move == 'Bite' or move == 'Breaking Swipe' or move == 'Brutal Swing' or move == 'Bug Bite' \
            or move == 'Bulldoze' or move == 'Covet' or move == 'Dragon Breath' or move == 'Flame Wheel' \
            or move == 'Flip Turn' or move == 'Force Palm' or move == 'Heart Stamp' or move == 'Hidden Power' \
            or move == 'Incinerate' or move == 'Needle Arm' or move == 'Ominous Wind' or move == 'Pluck' \
            or move == 'Revenge' or move == 'Round' or move == 'Silver Wind' or move == 'Sky Drop' \
            or move == 'Thief' or move == 'Water Pulse' or move == 'Wing Attack' \
            or move == 'Aerial Ace' or move == 'Feint Attack' or move == 'Magical Leaf' or move == 'Magnet Bomb' \
            or move == 'Shadow Punch' or move == 'Shock Wave' or move == 'Swift' or move == 'Triple Kick' \
            or move == 'Spike Cannon' or move == 'Double Kick' or move == 'Solar Beam' or move == 'Meteor Beam':
        power = 60
    elif move == 'Solar Blade':
        power = 62.5
    elif move == 'Bone Club' or move == 'Mirror Shot' or move == 'Mud Bomb' or move == 'Octazooka' \
            or move == 'Leaf Tornado' or move == 'Fire Fang' or move == 'Glaciate' or move == 'Ice Fang' \
            or move == 'Thunder Fang' or move == 'Aurora Beam' or move == 'Brine' or move == 'Bubble Beam' \
            or move == 'Chatter' or move == 'Hex' or move == 'Horn Attack' or move == 'Knock Off' \
            or move == 'Low Sweep' or move == 'Parabolic Charge' or move == 'Psybeam' or move == 'Sludge' \
            or move == 'Spark' or move == 'Steamroller'	or move == 'Stomp' or move == 'Venoshock':
        power = 65
    elif move == 'Skitter Smack' or move == 'Steel Wing' or move == 'Chip Away' or move == 'Cross Poison' \
            or move == 'Dizzy Punch' or move == 'Facade' or move == 'Flame Burst' or move == 'Freeze-Dry' \
            or move == 'Headbutt' or move == 'Luster Purge' or move == 'Mist Ball' or move == 'Night Slash' \
            or move == 'Psycho Cut' or move == 'Retaliate' or move == 'Rising Voltage' \
            or move == 'Scorching Sands' or move == 'Secret Power' or move == 'Shadow Claw' \
            or move == 'Slash' or move == 'Smelling Salts' or move == 'Sucker Punch' or move == 'Trop Kick' \
            or move == 'U-turn' or move == 'Volt Switch' or move == 'Wake-Up Slap' or move == 'Vital Throw' \
            or move == 'Smart Strike' or move == 'Double Hit' or move == 'Freeze Shock' or move == 'Ice Burn' \
            or move == 'Sky Attack':
        power = 70
    elif move == 'Rock Slide' or move == 'Air Slash' or move == 'Crush Claw' or move == 'Razor Shell' \
            or move == 'Brick Break' or move == 'Drain Punch' or move == 'Fire Punch' or move == 'Giga Drain' \
            or move == 'Horn Leech' or move == 'Ice Punch' or move == 'Lash Out' or move == 'Mystical Fire' \
            or move == 'Relic Song' or move == 'Signal Beam' or move == 'Spirit Break' \
            or move == 'Stomping Tantrum' or move == 'Thunder Punch' or move == 'Bone Rush' \
            or move == 'Bullet Seed' or move == 'Icicle Spear' or move == 'Pin Missile' \
            or move == 'Rock Blast' or move == 'Scale Shot' or move == 'Tail Slap' or move == 'Zippy Zap'\
            or move == 'Roar of Time' or move == 'Rock Wrecker' or move == 'Hyper Beam' or move == 'Meteor Assault' \
            or move == 'Blast Burn' or move == 'Frenzy Plant' or move == 'Giga Impact' \
            or move == 'Hydro Cannon':
        power = 75
    elif move == 'Submission' or move == 'Mega Punch' or move == 'Hyper Fang' or move == 'Zen Headbutt' \
            or move == 'Drill Run' or move == 'Anchor Shot' or move == 'Apple Acid' or move == 'Body Press' \
            or move == 'Crunch' or move == 'Dark Pulse' or move == 'Dazzling Gleam' \
            or move == 'Discharge' or move == 'Dragon Claw' or move == 'Drill Peck' \
            or move == 'Drum Beating' or move == 'Expanding Force' or move == 'Extrasensory' \
            or move == 'Extreme Speed' or move == 'Fiery Dance' or move == 'Fire Lash' or move == 'Fire Pledge' \
            or move == 'Flash Cannon' or move == 'Grass Pledge' or move == 'Grav Apple' or move == 'Iron Head' \
            or move == 'Jaw Lock' or move == 'Lava Plume' or move == 'Leech Life' or move == 'Lunge' \
            or move == 'Oblivion Wing' or move == 'Overdrive' or move == 'Poison Jab' or move == 'Power Gem' \
            or move == 'Psyshock' or move == 'Scald' or move == 'Seed Bomb' \
            or move == 'Shadow Ball' or move == 'Snipe Shot' or move == 'Spirit Shackle' \
            or move == 'Strength' or move == 'Throat Chop' or move == 'Tri Attack' or move == 'Water Pledge' \
            or move == 'Waterfall' or move == 'X-Scissor' or move == 'Zing Zap' or move == 'Aura Sphere' \
            or move == 'False Surrender' or move == 'Hyperspace Hole' or move == 'Dual Chop'\
            or move == 'Dual Wingbeat' or move == 'Eternabeam' or move == 'Prismatic Laser':
        power = 80
    elif move == 'Blaze Kick' or move == 'Icicle Crash' or move == 'Sky Uppercut' \
            or move == 'Night Daze' or move == 'Body Slam' or move == 'Bolt Beak' or move == 'Darkest Lariat' \
            or move == 'Dragon Pulse' or move == 'Fishious Rend' or move == 'Liquidation' \
            or move == 'Psychic Fangs' or move == 'Secret Sword' or move == 'Secret Sword' \
            or move == 'Shadow Bone':
        power = 85
    elif move == 'Muddy Water' or move == 'Rock Climb' or move == 'Take Down' or move == 'Aqua Tail' \
            or move == 'Meteor Mash' or move == 'Play Rough' or move == 'Floaty Fall' \
            or move == 'Strange Steam' or move == 'Attack Order' or move == 'Baddy Bad' \
            or move == 'Bouncy Bubble' or move == 'Bug Buzz' or move == 'Buzzy Buzz' or move == 'Dragon Hammer' \
            or move == 'Earth Power' or move == 'Energy Ball' or move == 'First Impression' \
            or move == 'Flamethrower' or move == 'Freezy Frost' or move == 'Glitzy Glow' \
            or move == 'Hyper Voice' or move == 'Ice Beam' or move == "Land's Wrath" \
            or move == 'Leaf Blade' or move == 'Petal Blizzard' or move == 'Phantom Force' \
            or move == 'Pollen Puff' or move == 'Psychic' or move == 'Revelation Dance' \
            or move == 'Sacred Sword' or move == 'Sappy Seed' or move == 'Sizzly Slide' or move == 'Sludge Bomb' \
            or move == 'Sparkling Aria' or move == 'Sparkly Swirl' or move == 'Spectral Thief' \
            or move == 'Splishy Splash' or move == 'Surf' or move == 'Thousand Arrows' \
            or move == 'Thousand Waves' or move == 'Thunderbolt' or move == 'Uproar' or move == 'Wild Charge'\
            or move == 'Frost Breath' or move == 'Storm Throw':
        power = 90
    elif move == 'Heat Wave' or move == 'High Horsepower'	or move == 'Foul Play' \
            or move == 'Moonblast' or move == 'Sludge Wave':
        power = 95
    elif move == 'Dynamic Punch' or move == 'Inferno' or move == 'Dragon Rush' or move == 'Egg Bomb' \
            or move == 'Iron Tail' or move == 'Magma Storm'	or move == 'Cross Chop' or move == 'Stone Edge' \
            or move == 'Crabhammer' or move == 'Hammer Arm' or move == 'Ice Hammer' or move == 'Aeroblast' \
            or move == 'Diamond Storm' or move == 'Flying Press' or move == 'Jump Kick' \
            or move == 'Sacred Fire' or move == 'Spacial Rend' or move == 'Beak Blast' or move == 'Behemoth Bash' \
            or move == 'Behemoth Blade' or move == 'Core Enforcer' or move == 'Dynamax Cannon' \
            or move == 'Earthquake' or move == 'Fusion Bolt' or move == 'Fusion Flare' or move == 'Judgment' \
            or move == 'Misty Explosion' or move == 'Moongeist Beam' or move == 'Photon Geyser' \
            or move == 'Plasma Fists' or move == 'Psystrike' or move == 'Searing Shot' \
            or move == 'Sunsteel Strike' or move == 'Bonemerang' or move == 'Dragon Darts'\
            or move == 'Gear Grind':
        power = 100
    elif move == 'Aura Wheel' or move == 'Blizzard' or move == 'Clanging Scales' or move == 'Fire Blast' \
            or move == 'Hurricane' or move == 'Hydro Pump' or move == 'Origin Pulse' or move == 'Poltergeist' \
            or move == 'Steam Eruption' or move == 'Thunder':
        power = 110
    elif move == 'Brave Bird' or move == 'Close Combat' or move == 'Double-Edge' or move == 'Dragon Ascent' \
            or move == 'Flare Blitz' or move == 'Focus Blast' or move == 'Future Sight' \
            or move == 'Gunk Shot' or move == 'Head Charge' or move == 'Mega Kick' or move == 'Megahorn' \
            or move == 'Multi-Attack' or move == 'Outrage' \
            or move == 'Petal Dance' or move == 'Power Whip' or move == 'Precipice Blades' \
            or move == 'Pyro Ball' or move == 'Seed Flare' or move == 'Shadow Force' \
            or move == 'Superpower' or move == 'Synchronoise' \
            or move == 'Techno Blast' or move == 'Thrash' or move == 'Volt Tackle' \
            or move == 'Wood Hammer' or move == 'Zap Cannon' or move == 'Triple Axel'\
            or move == 'Double Iron Bash':
        power = 120
    elif move == 'Blue Flare' or move == 'Bolt Strike' or move == 'Burn Up' or move == 'Draco Meteor' \
            or move == 'Fleur Cannon' or move == 'High Jump Kick' or move == 'Leaf Storm' \
            or move == 'Overheat' or move == 'Skull Bash' or move == 'Steel Roller':
        power = 130
    elif move == 'Boomburst' or move == 'Light of Ruin' or move == 'Psycho Boost' or move == 'Steel Beam':
        power = 140
    elif move == 'Eruption' or move == 'Focus Punch' or move == 'Head Smash' \
            or move == 'Mind Blown' or move == 'Shell Trap' or move == 'Water Spout':
        power = 150
    elif move == 'V-create':
        power = 180
    elif move == 'Ice Ball' or move == 'Rollout':
        power = 186
    elif move == 'Self-Destruct':
        power = 200
    elif move == 'Explosion':
        power = 250
    else:
        power = 0

    return power
