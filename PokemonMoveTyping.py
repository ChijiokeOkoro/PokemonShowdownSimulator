# typing of all attacking moves
# if move has no base power then it is classified as 'None'
def typing(move):
    if move == 'Constrict' or move == 'Barrage' or move == 'Bind' or move == 'Double Slap' \
            or move == 'Fury Attack' or move == 'Wrap' or move == 'Comet Punch' or move == 'Fury Swipes' \
            or move == 'Rage' or move == 'Spike Cannon' or move == 'Tail Slap' or move == 'Feint' \
            or move == 'Double Hit' or move == 'Echoed Voice' or move == 'Fake Out' or move == 'False Swipe' \
            or move == 'Hold Back' or move == 'Pay Day' or move == 'Pound' or move == 'Quick Attack' \
            or move == 'Scratch' or move == 'Tackle' or move == 'Cut' or move == 'Rapid Spin' or move == 'Snore' \
            or move == 'Struggle' or move == 'Terrain Pulse' or move == 'Weather Ball' or move == 'Vise Grip' \
            or move == 'Covet' or move == 'Hidden Power' or move == 'Round' or move == 'Swift' or move == 'Horn Attack'\
            or move == 'Stomp' or move == 'Chip Away' or move == 'Dizzy Punch' or move == 'Facade' \
            or move == 'Headbutt' or move == 'Retaliate' or move == 'Secret Power' or move == 'Slash' \
            or move == 'Smelling Salts' or move == 'Crush Claw' or move == 'Relic Song' or move == 'Extreme Speed' \
            or move == 'Hyper Fang' or move == 'Mega Punch' or move == 'Razor Wind' or move == 'Slam' \
            or move == 'Strength' or move == 'Tri Attack' or move == 'Body Slam' or move == 'Hyper Voice' \
            or move == 'Revelation Dance' or move == 'Rock Climb' or move == 'Take Down' or move == 'Uproar' \
            or move == 'Egg Bomb' or move == 'Judgment' or move == 'Double-Edge' or move == 'Head Charge' \
            or move == 'Mega Kick' or move == 'Multi-Attack' or move == 'Techno Blast' or move == 'Thrash' \
            or move == 'Skull Bash' or move == 'Boomburst' or move == 'Last Resort' or move == 'Giga Impact' \
            or move == 'Hyper Beam' or move == 'Self-Destruct' or move == 'Explosion':
        montype = 'Normal'
    elif move == 'V-create' or move == 'Shell Trap' or move == 'Mind Blown' or move == 'Eruption' \
            or move == 'Blast Burn' or move == 'Overheat' or move == 'Burn Up' or move == 'Blue Flare' \
            or move == 'Pyro Ball' or move == 'Flare Blitz' or move == 'Fire Blast' or move == 'Searing Shot' \
            or move == 'Sacred Fire' or move == 'Magma Storm' or move == 'Inferno' or move == 'Fusion Flare' \
            or move == 'Heat Wave' or move == 'Sizzly Slide' or move == 'Flamethrower' or move == 'Blaze Kick' \
            or move == 'Lava Plume' or move == 'Fire Pledge' or move == 'Fire Lash' or move == 'Fiery Dance' \
            or move == 'Mystical Fire' or move == 'Fire Punch' or move == 'Flame Burst' or move == 'Fire Fang' \
            or move == 'Incinerate' or move == 'Flame Wheel' or move == 'Flame Charge' or move == 'Ember' \
            or move == 'Fire Spin':
        montype = 'Fire'
    elif move == 'Water Spout' or move == 'Hydro Cannon' or move == 'Steam Eruption' or move == 'Origin Pulse' \
            or move == 'Hydro Pump' or move == 'Crabhammer' or move == 'Surf' or move == 'Splishy Splash' \
            or move == 'Sparkling Aria' or move == 'Muddy Water' or move == 'Bouncy Bubble' \
            or move == 'Aqua Tail' or move == 'Liquidation' or move == 'Fishious Rend' or move == 'Waterfall' \
            or move == 'Water Pledge' or move == 'Snipe Shot' or move == 'Scald' or move == 'Dive' \
            or move == 'Razor Shell' or move == 'Octazooka' or move == 'Bubble Beam' or move == 'Brine' \
            or move == 'Water Pulse' or move == 'Flip Turn' or move == 'Water Gun' or move == 'Bubble' \
            or move == 'Aqua Jet' or move == 'Whirlpool' or move == 'Clamp' or move == 'Water Shuriken':
        montype = 'Water'
    elif move == 'Frenzy Plant' or move == 'Leaf Storm' or move == 'Solar Blade' or move == 'Wood Hammer' \
            or move == 'Solar Beam' or move == 'Seed Flare' or move == 'Power Whip' or move == 'Petal Dance' \
            or move == 'Sappy Seed' or move == 'Petal Blizzard' or move == 'Leaf Blade' \
            or move == 'Energy Ball' or move == 'Seed Bomb' or move == 'Grav Apple' or move == 'Grass Pledge' \
            or move == 'Drum Beating' or move == 'Apple Acid' or move == 'Horn Leech' or move == 'Giga Drain' \
            or move == 'Trop Kick' or move == 'Leaf Tornado' or move == 'Needle Arm' or move == 'Magical Leaf' \
            or move == 'Razor Leaf' or move == 'Vine Whip' or move == 'Mega Drain' or move == 'Leafage' \
            or move == 'Branch Poke' or move == 'Snap Trap' or move == 'Bullet Seed' or move == 'Absorb':
        montype = 'Grass'
    elif move == 'Ice Burn' or move == 'Freeze Shock' or move == 'Blizzard' or move == 'Ice Hammer' \
            or move == 'Ice Beam' or move == 'Frosty Frost' or move == 'Icicle Crash' or move == 'Ice Punch' \
            or move == 'Freeze-Dry' or move == 'Ice Fang' or move == 'Glaiate' or move == 'Aurora Beam' \
            or move == 'Frost Breath' or move == 'Avalanche' or move == 'Icy Wind' or move == 'Powder Snow' \
            or move == 'Ice Shard' or move == 'Ice Ball' or move == 'Icicle Spear' or move == 'Triple Axel' \
            or move == 'Sheer Cold':
        montype = 'Ice'
    elif move == 'Meteor Assault' or move == 'Focus Punch' or move == 'High Jump Kick' or move == 'Superpower' \
            or move == 'Focus Blast' or move == 'Close Combat' or move == 'Jump Kick' or move == 'Hammer Arm' \
            or move == 'Flying Press' or move == 'Dynamic Punch' or move == 'Cross Chop' \
            or move == 'Sacred Sword' or move == 'Sky Uppercut' or move == 'Secret Sword' \
            or move == 'Submission' or move == 'Body Press' or move == 'Aura Sphere' or move == 'Drain Punch' \
            or move == 'Brick Break' or move == 'Wake-Up Slap' or move == 'Vital Throw' \
            or move == 'Low Sweep' or move == 'Storm Throw' or move == 'Rolling Kick' or move == 'Revenge' \
            or move == 'Force Palm' or move == 'Circle Throw' or move == 'Karate Chop' \
            or move == 'Vacuum Wave' or move == 'Rock Smash' or move == 'Power-Up Punch' \
            or move == 'Mach Punch' or move == 'Double Kick' or move == 'Arm Thrust' or move == 'Triple Kick':
        montype = 'Fighting'
    elif move == 'Gunk Shot' or move == 'Belch' or move == 'Sludge Wave' or move == 'Sludge Bomb' \
            or move == 'Poison Jab' or move == 'Cross Poison' or move == 'Venoshock' or move == 'Sludge' \
            or move == 'Poison Tail' or move == 'Poison Fang' or move == 'Clear Smog' \
            or move == 'Acid Spray' or move == 'Acid' or move == 'Smog' or move == 'Poison Sting':
        montype = 'Poison'
    elif move == 'Precipice Blades' or move == 'Earthquake' or move == 'High Horsepower' \
            or move == 'Thousand Waves' or move == 'Thousand Arrows' or move == "Land's Wrath" \
            or move == 'Earth Power' or move == 'Drill Run' or move == 'Dig' or move == 'Stomping Tantrum' \
            or move == 'Scorching Sands' or move == 'Mud Bomb' or move == 'Bone Club' or move == 'Bulldoze' \
            or move == 'Mud Shot' or move == 'Bonemerang' or move == 'Sand Tomb' or move == 'Bone Rush' \
            or move == 'Mud-Slap' or move == 'Magnitude':
        montype = 'Ground'
    elif move == 'Sky Attack' or move == 'Dragon Ascent' or move == 'Brave Bird' or move == 'Hurricane' \
            or move == 'Beak Blast' or move == 'Aeroblast' or move == 'Fly' or move == 'Floaty Fall' \
            or move == 'Bounce' or move == 'Oblivion Wing' or move == 'Drill Peck' or move == 'Air Slash' \
            or move == 'Chatter' or move == 'Wing Attack' or move == 'Sky Drop' or move == 'Pluck' \
            or move == 'Air Cutter' or move == 'Aerial Ace' or move == 'Acrobatics' or move == 'Gust' \
            or move == 'Dual Wingbeat' or move == 'Peck':
        montype = 'Flying'
    elif move == 'Light That Burns the Sky' or move == 'Prismatic Laser' or move == 'Psycho Boost' \
            or move == 'Synchronoise' or move == 'Future Sight' or move == 'Psystrike' \
            or move == 'Photon Geyser' or move == 'Dream Eater' or move == 'Psychic' or move == 'Glitzy Glow' \
            or move == 'Psychic Fangs' or move == 'Zen Headbutt' or move == 'Psyshock' \
            or move == 'Hyperspace Hole' or move == 'Extrasensory' or move == 'Expanding Force' \
            or move == 'Psycho Cut' or move == 'Mist Ball' or move == 'Luster Purge' or move == 'Psybeam' \
            or move == 'Heart Stamp' or move == 'Confusion' or move == 'Stored Power' \
            or move == 'Psywave':
        montype = 'Psychic'
    elif move == 'Megahorn' or move == 'Pollen Puff' or move == 'First Impression' or move == 'Bug Buzz' \
            or move == 'Attack Order' or move == 'X-Scissor' or move == 'Lunge' or move == 'Leech Life' \
            or move == 'Signal Beam' or move == 'U-turn' or move == 'Skitter Smack' or move == 'U-turn' \
            or move == 'Steamroller' or move == 'Silver Wind' or move == 'Bug Bite' or move == 'Struggle Bug' \
            or move == 'Fell Stinger' or move == 'Fury Cutter' or move == 'Twineedle' or move == 'Pin Missile' \
            or move == 'Infestation':
        montype = 'Bug'
    elif move == 'Rock Wrecker' or move == 'Head Smash' or move == 'Meteor Beam' or move == 'Stone Edge' \
            or move == 'Diamond Storm' or move == 'Power Gem' or move == 'Rock Slide' or move == 'Rock Tomb' \
            or move == 'Ancient Power' or move == 'Smack Down' or move == 'Rock Throw' or move == 'Accelrock' \
            or move == 'Rollout' or move == 'Rock Blast':
        montype = 'Rock'
    elif move == 'Shadow Force' or move == 'Poltergeist' or move == 'Moongeist Beam' or move == 'Spectral Thief'\
            or move == 'Phantom Force' or move == 'Shadow Bone' or move == 'Spirit Shackle' or move == 'Shadow Ball'\
            or move == 'Shadow Ball' or move == 'Shadow Claw' or move == 'Hex' or move == 'Shadow Punch'\
            or move == 'Ominous Wind' or move == 'Shadow Sneak' or move == 'Lick' or move == 'Astonish':
        montype = 'Ghost'
    elif move == 'Eternabeam' or move == 'Roar of Time' or move == 'Draco Meteor' or move == 'Outrage' \
            or move == 'Clanging Scales' or move == 'Spacial Rend' or move == 'Dynamax Cannon' or move == 'Dragon Rush'\
            or move == 'Core Enforcer' or move == 'Dragon Hammer' or move == 'Dragon Pulse' or move == 'Dragon Claw' \
            or move == 'Dragon Tail' or move == 'Dragon Breath' or move == 'Breaking Swipe' or move == 'Dragon Darts' \
            or move == 'Twister' or move == 'Dual Chop' or move == 'Scale Shot' or move == 'Dragon Rage':
        montype = 'Dragon'
    elif move == 'Hyperspace Hole' or move == 'Foul Play' or move == 'Baddy Bay' or move == 'Night Daze' \
            or move == 'Wicked Blow' or move == 'Darkest Lariat' or move == 'Throat Chop' or move == 'Jaw Lock' \
            or move == 'False Surrender' or move == 'Dark Pulse' or move == 'Crunch' or move == 'Lash Out' \
            or move == 'Sucker Punch' or move == 'Night Slash' or move == 'Knock Off' or move == 'Thief'\
            or move == 'Feint Attack' or move == 'Brutal Swing' or move == 'Bite' or move == 'Assurance' \
            or move == 'Snarl' or move == 'Payback' or move == 'Pursuit' or move == 'Power Trip':
        montype = 'Dark'
    elif move == 'Steel Beam' or move == 'Doom Desire' or move == 'Steel Roller' or move == 'Sunsteel Strike' \
            or move == 'Iron Tail' or move == 'Behemoth Blade' or move == 'Behemoth Bash' or move == 'Meteor Mash' \
            or move == 'Iron Head' or move == 'Flash Cannon' or move == 'Anchor Shot' or move == 'Steel Wing' \
            or move == 'Smart Strike' or move == 'Mirror Shot' or move == 'Magnet Bomb' or move == 'Double Iron Bash' \
            or move == 'Metal Claw' or move == 'Gear Grind' or move == 'Bullet Punch' or move == 'Heavy Slam'\
            or move == 'Gyro Ball':
        montype = 'Steel'
    elif move == 'Light of Ruin' or move == 'Fleur Cannon' or move == 'Misty Explosion' or move == 'Moonblast' \
            or move == 'Strange Steam' or move == 'Sparkly Swirl' or move == 'Play Rough' or move == 'Dazzling Gleam' \
            or move == 'Spirit Break' or move == 'Draining Kiss' or move == 'Fairy Wind' or move == 'Disarming Voice' \
            or move == "Nature's Madness" or move == 'Guardian of Alola':
        montype = 'Fairy'
    elif move == 'Bolt Strike' or move == 'Zap Cannon' or move == 'Volt Tackle' or move == 'Thunder' \
            or move == 'Aura Wheel' or move == 'Plasma Fists' or move == 'Fusion Bolt' or move == 'Wild Charge' \
            or move == 'Thunderbolt' or move == 'Buzzy Buzz' or move == 'Bolt Beak' \
            or move == 'Zing Zap' or move == 'Overdrive' or move == 'Discharge' or move == 'Thunder Punch' \
            or move == 'Volt Switch' or move == 'Rising Voltage' or move == 'Thunder Fang' or move == 'Spark' \
            or move == 'Parabolic Charge' or move == 'Shock Wave' or move == 'Electroweb' or move == 'Zippy Zap' \
            or move == 'Charge Beam' or move == 'Thunder Shock' or move == 'Nuzzle':
        montype = 'Electric'
    else:
        montype = 'None'

    return montype
