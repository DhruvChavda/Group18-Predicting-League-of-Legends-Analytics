import React from "react";
import { Grid, makeStyles } from "@material-ui/core";

const useStyles = makeStyles({
    root: {
        background: "#f2e4fd",
    },
    cent: {
        textAlign: "center",
    },
    fsiz: {
        fontSize: "15px",
    },
});

export default function HowToPlay() {
    const classes = useStyles();
    return (
        <React.Fragment>
            <Grid container justify="space-around" spacing={2}>
                <Grid item lg={12}>
                    <div className={classes.fsiz}>
                        <p>
                            <b>
                                <span style={{ fontSize: "23px", color: "#2874A6" }}>League of Legends</span>
                            </b>{" "}
                            is a multiplayer online battle arena. It’s been one of the most popular games of all time
                            and currently one of the biggest esports.
                        </p>
                        <p>
                            In a standard game of League, ten players are split into two teams of five and battle it out
                            on a map called Summoner’s Rift.
                        </p>
                        <p>Each of these players controls a single character, known as a champion.</p>
                    </div>
                </Grid>
                <Grid item lg={6}>
                    <div className={classes.fsiz}>
                        <h1>What is a champion?</h1>
                        <p>All ten players in a League of Legends match controls a single champion.</p>
                        <p>There are currently over 140 champions with new ones being continuously added over time.</p>
                        <p>Every champion has special abilities and powers with unique playstyles.</p>
                        <p>Before a game begins at champ select, each team takes turns selecting champions.</p>
                        <p>
                            There’s a lot of strategies involved as you work with your team to create teams with
                            champions that work well together (more on this later).
                        </p>
                        <p>
                            Every game you play can be vastly different since every champion has their own feel and
                            gameplan.
                        </p>
                    </div>
                </Grid>
                <Grid item lg={6}>
                    <div className={classes.fsiz}>
                        <h1> How do you win?</h1>
                        <p>The ultimate goal of LoL is to destroy the other team’s base, but it’s not easy.</p>
                        <p>Your enemies will do everything they can to kill you and destroy your base.</p>
                        <p>Each base has a series of turrets and waves of minions that constantly spawn.</p>
                        <p>
                            If you started a game and tried to run straight to the enemy base, you’d certainly die, not
                            just because the enemy team would be trying to stop you at all costs, but also because you
                            may be too weak and die.
                        </p>
                        <p>
                            League is sort of like a role-playing game (RPG) that takes place in a very short amount of
                            time.
                        </p>
                        <p>
                            You begin at level 1 and gradually get stronger throughout the game by gaining experience
                            and earning gold to buy items.
                        </p>
                        <p>
                            The two teams continually grow in power and collide. Eventually, one team is able to get the
                            upper hand and make a final push for a victory.
                        </p>
                    </div>
                </Grid>

                <Grid item lg={10} className={classes.cent}>
                    <div className={classes.fsiz}>
                        <h1> What is Summoner’s Rift?</h1>
                        <p>
                            This is the standard map that the professionals play on and it’s where you’d be if you were
                            trying to climb the ranked ladder.
                        </p>
                        <p>
                            There are other maps in League, but for now, we’ll focus on Summoner’s Rift since it’s where
                            you’ll likely be spending most of your time.
                        </p>
                        <img
                            src="https://mobalytics.gg/wp-content/uploads/2018/12/Basic-map.jpg"
                            height="500px"
                            alt="basic map"
                        ></img>
                    </div>
                </Grid>
                <Grid item lg={6}>
                    <div className={classes.fsiz}>
                        <h1> Here are the basics of the Summoner’s Rift map:</h1>
                        <p>
                            There are two teams of five players: the blue team (base at bottom left corner) and the red
                            team (base at the top right corner).
                        </p>
                        <p>
                            To achieve victory, one team has to destroy the opposing team’s Nexus (basically the core of
                            their base).
                        </p>
                        <p>
                            During a match, minions will continually spawn from each base’s Nexus and proceed through
                            the three lanes (the paths are shown in the graphic above).The three lanes are known as top
                            lane, mid lane, and bot lane. In all three lanes, there are turrets which will attack enemy
                            champions and minions. Summoners must destroy all turrets in at least one lane and then
                            destroy the last two towers that protect a Nexus before being able to attack and destroy it.
                        </p>
                    </div>
                </Grid>
                <Grid item lg={6}>
                    <div className={classes.fsiz}>
                        <img
                            src="https://mobalytics.gg/wp-content/uploads/2019/06/Nexus-and-turrets.jpg"
                            height="320px"
                            alt="nexus"
                        ></img>
                    </div>
                </Grid>
                <Grid item lg={7}>
                    <div className={classes.fsiz}>
                        <img
                            src="https://mobalytics.gg/wp-content/uploads/2019/06/Super-minions.jpg"
                            alt="minion"
                            height="300px"
                        ></img>
                    </div>
                </Grid>
                <Grid item lg={5}>
                    <div className={classes.fsiz}>
                        <h1>Turrets and Inhibitors</h1>
                        <p>
                            Destroying turrets and other structures called inhibitors rewards players with gold and
                            allows the minion waves to push through the lane (since there aren’t any turrets to stop
                            them).
                        </p>
                        <p>
                            Inhibitors are structures that are behind the initial turrets inside a base. If an inhibitor
                            is destroyed, upgraded minions, called Super Minions, will spawn until an inhibitor respawns
                            after a few minutes. A team can often use the Super Minions to successfully siege a base
                            that was previously difficult to attack and create an opportunity to push to victory.
                        </p>
                    </div>
                </Grid>
                <Grid item lg={5}>
                    <div className={classes.fsiz}>
                        <h1>The Fountain and Shop</h1>
                        <p>
                            At the beginning of each game, you’ll begin at your fountain. You’ll revisit your fountain
                            because it’s where you’ll respawn when you die and it’s where your shop is located.
                        </p>
                        <p>
                            You can return to your fountain at any time during a game to heal or purchase items. All you
                            have to do is use the Recall ability which every summoner has access to – just be careful
                            and use it safely because you can be interrupted while casting it.
                        </p>
                    </div>
                </Grid>
                <Grid item lg={7}>
                    <div className={classes.fsiz}>
                        <img
                            src="https://mobalytics.gg/wp-content/uploads/2019/06/Fountain-and-shop.jpg"
                            alt="shop"
                            height="300"
                        ></img>
                    </div>
                </Grid>
                <Grid item lg={10} className={classes.cent}>
                    <div className={classes.fsiz}>
                        <h1> LoL Champion Basics</h1>
                        <p>
                            Now that we understand the basics of the map, let’s get back to talking about champions.
                            Champions are the heart and soul of League of Legends as they’re often what players resonate
                            with most.
                        </p>
                        <p>
                            While Summoner’s Rift stays constant, the different combinations of champions that are
                            chosen by the ten players in game can create vastly different rhythms and feels.
                        </p>
                        <p>
                            Right now there are currently over 140 champions, each of them representing a different
                            playstyle and experience.
                        </p>
                        <p>
                            Some are simple and easy to play while others may take a hundred games to master. Whether
                            you like dealing damage from afar, brawling at close quarters, or helping your team with
                            utility, there’s a champion for you.
                        </p>
                        <p>
                            In the next few sections, we’ll discuss different aspects of champions, such as their
                            abilities, stats, and scaling.
                        </p>
                        <img
                            src="https://mobalytics.gg/wp-content/uploads/2019/06/all-champions.jpg"
                            alt="champs"
                        ></img>
                    </div>
                </Grid>
                <Grid item lg={6}>
                    <div className={classes.fsiz}>
                        <h1> Champion Stats</h1>
                        <p>
                            A major aspect that sets champions apart is the distribution of their stats. Stats represent
                            a champion’s make up as far as how hard they are to kill, how much damage they do, and how
                            fast they move or attack.
                        </p>

                        <p>
                            From left to right: attack damage, ability power, armor, magic resist, attack speed,
                            cooldown reduction, critical strike chance, movement speed.
                        </p>
                    </div>
                </Grid>
                <Grid item lg={6}>
                    <div className={classes.fsiz}>
                        <img
                            src="https://mobalytics.gg/wp-content/uploads/2019/06/Champ-stats-Ashe.jpg"
                            alt="stats demo"
                            height="80px"
                        ></img>
                    </div>
                </Grid>

                <Grid item lg={10} className={(classes.cent, classes.fsiz)}>
                    <h1>The Three Phases and Scaling</h1>
                    <p>
                        These concepts are leaning more towards being intermediate than beginner, but we want to quickly
                        go over them since you’ll likely hear the terminology of the three phases: early game, mid game,
                        and late game.
                    </p>
                    <p>
                        The phases aren’t set in stone and act more as guidelines as every game is different in its own
                        way, but they tend to hold true to regarding how the majority of games turn out:
                    </p>
                </Grid>

                <Grid item lg={4} className={classes.fsiz}>
                    <h2>Early game (the first 15 minutes)</h2>
                    <p>• This is when all the turrets are up and everyone is in their lane except for the junglers.</p>
                    <p>• Until the jungler arrives, top and mid will mostly be 1v1 and bot lane will mostly be 2v2.</p>
                </Grid>
                <Grid item lg={4} className={classes.fsiz}>
                    <h2>Mid game (15 to 30 minutes)</h2>
                    <p>• At around 15 minutes, or when the first turrets begin to be destroyed, the mid game begins.</p>
                    <p>
                        • During the mid game, a match becomes messier than lane phase as some players will remain in
                        lane while others will begin to roam around the map to help destroy other turrets or contest
                        dragons or Rift Herald.
                    </p>
                </Grid>
                <Grid item lg={4} className={classes.fsiz}>
                    <h2>Late game (after 30 minutes)</h2>
                    <p>
                        • The mid game usually ends and around the 30 minute mark when all of the first turrets in the
                        lanes are destroyed (sometimes even more are gone by then). This is the late game.
                    </p>
                    <p>
                        • At this point, champions have acquired many of their major items and teams begin to group for
                        large teamfights around Baron and Elder Dragons.
                    </p>
                </Grid>
                <Grid item lg={10} className={`${classes.fsiz} ${classes.cent}`}>
                    <p>
                        So why are the three phases important? In League of Legends, every champion is designed to be
                        good during a certain time period. Some champions are designed to be strong in the early game
                        but fall off the longer the game goes while others are designed to be weak early but get
                        continuously stronger as the game goes on.
                    </p>
                    <p>
                        When a champion is at their strongest, it is known as a “power spike”. The process of getting
                        gradually stronger and achieving your power spike is known as “scaling”. We won’t get too into
                        detail here but know that scaling is usually influenced by a champion’s ability kit and their
                        stat ratios as they buy more items. Let’s cover a few examples.
                    </p>
                </Grid>
                <Grid item lg={11} className={`${classes.fsiz} ${classes.cent}`}>
                    <h1> How these phases actually depends upon Champion!?</h1>
                    <h2>Blitzcrank: Early game power spike</h2>
                    <img
                        src="https://mobalytics.gg/wp-content/uploads/2019/06/Blitzcrank-power-spike.jpg"
                        alt="blitz"
                    ></img>
                    <p>
                        Blitzcrank is one of the scariest early game supports because of his signature move, Rocket
                        Grab, which pulls an enemy toward him. One well-timed grab can pull a vulnerable target and turn
                        a 2v2 into a very quick 1v2 death.
                    </p>
                    <p>
                        His whole kit revolves around making picks and gaining an early advantage for his team. As the
                        game goes on, however, Blitzcrank’s grab loses power because it becomes harder for him to grab
                        his ideal target.
                    </p>
                    <p>
                        Instead of worrying about weaving his grab through a minion wave, he has to worry about getting
                        it through a frontline of tanks during teamfights. His ability is also outclassed by better
                        engage options that can target multiple champions instead of just one.
                    </p>
                    <h2>Ahri: Mid game power spike</h2>
                    <img src="https://mobalytics.gg/wp-content/uploads/2019/06/Ahri-power-spike.jpg" alt="ahri"></img>
                    <p>
                        The mid game is all about quick rotations with messy skirmishers and unpredictable team fights.
                        Ahri hits her power spike during this time because she is a mage that utilizes a high amount of
                        mobility and lower cooldown abilities that can be cast often.
                    </p>
                    <p>
                        Mid game fights are often fought from different angles and uneven numbers (3v2’s, 2v4’s, etc) so
                        being mobile and flexible has more value. She can use hit and run tactics and move around the
                        map quickly to help her laners that are still trying to take their turret or her jungler who is
                        contesting objectives.
                    </p>
                    <p>
                        She isn’t necessarily bad in the early game but will be outdamaged by champions that have less
                        mobility and more punch, and she tends to fall off in the late game since she doesn’t have
                        strong late game scaling compared to other champions.
                    </p>
                    <h2>Kog’Maw: Late game power spike</h2>
                    <img
                        src="https://mobalytics.gg/wp-content/uploads/2019/06/KogMaw-power-spike.jpg"
                        alt="kogMaw"
                    ></img>
                    <p>
                        When the late game arrives, you’ll start to see large scale teamfights with high stakes. One
                        false move can mean all five of your allies dying and a charge by the enemy team to destroy your
                        base.
                    </p>
                    <p>
                        Kog’Maw is a champion who’s easy to kill when alone but able to deal an insane amount of damage
                        when he’s protected (some team comps are even built around him). In the organized situations
                        during the late game where you have multiple frontliners and a backline of damage dealers,
                        Kog’Maw is at his best.
                    </p>
                    <p>
                        He hits his spike during the late game because he also has access to most or all of his items.
                        During the early game he’s focused on farming and won’t do that much damage and in the mid game,
                        he’s vulnerable during skirmishes since they often happen from multiple angles.
                    </p>
                </Grid>
            </Grid>
        </React.Fragment>
    );
}
