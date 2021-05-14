import {
    Avatar,
    Button,
    ButtonGroup,
    Card,
    CardActionArea,
    CardContent,
    Grid,
    makeStyles,
    Paper,
    Typography,
} from "@material-ui/core";
import { deepOrange } from "@material-ui/core/colors";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router";
import BarChampions from "../Components/BarChampions";

const useStyles = makeStyles({
    root: {
        // background: "#ffffff",
        margin: "0px",
    },
    basic: {
        fontSize: "18px",
    },
    alcenter: {
        justifyContent: "center",
        display: "flex",
        textAlign: "center",
        alignContent: "center",
    },
    lore: {
        padding: "5px",
        margin: "5px",
        color: "#000000",
    },
});

function DisplayChampion(props) {
    const { championName } = useParams();
    const [championData, setChampionData] = useState(null);
    const link = `http://ddragon.leagueoflegends.com/cdn/11.9.1/data/en_US/champion/${championName}.json`;

    useEffect(() => {
        props.changeTitle(`${championName}`);
        axios
            .get(link)  
            .then((res) => {
                const arrInit = Object.values(res.data);
                const x = arrInit[3];
                const arrX = Object.values(x);
                const finalData = arrX[0];
                console.log(finalData);
                setChampionData(finalData);
            })
            .catch((err) => {
                console.log(err);
            });
    }, [championName, link, props]);

    const classes = useStyles();

    return (
        <>
            {championData && (
                <div className={classes.root}>
                    <Grid container>
                        <Grid item lg={6}>
                            <Typography variant="h2" component="p" color="textPrimary">
                                <img
                                    src={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/champion/${championData.image.full}`}
                                    alt={`${championData.id}`}
                                />{" "}
                                &nbsp;
                                {championData.name}
                                <Typography variant="h4" color="textSecondary">
                                    {championData.title}
                                </Typography>
                            </Typography>
                            <Paper className={classes.lore}>
                                <Typography variant="caption" color="textSecondary" className={classes.basic}>
                                    "{championData.lore}"
                                </Typography>
                            </Paper>
                        </Grid>
                        <Grid item lg={6}>
                            <Typography variant="h3" color="primary">
                                Abilities
                            </Typography>
                            <Grid container spacing={1} justify="center">
                                <Grid item lg={6}>
                                    <Card variant="outlined" className={classes.alcenter}>
                                        <CardContent>
                                            <Typography variant="h5">{championData.spells[0].name}</Typography>
                                            <Typography variant="h5" component="h2" className={classes.alcenter}>
                                                <Avatar variant="rounded" sx={{ bgcolor: deepOrange[500] }}>
                                                    Q
                                                </Avatar>{" "}
                                                &nbsp; &nbsp;
                                                <Avatar
                                                    variant="rounded"
                                                    src={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/spell/${championData.spells[0].image.full}`}
                                                    alt=""
                                                />
                                            </Typography>
                                            <Typography color="textSecondary" gutterBottom>
                                                RangeBurn:
                                                <br /> {championData.spells[0].rangeBurn}
                                            </Typography>
                                            <CardActionArea>
                                                <ButtonGroup variant="contained" size="small" color="primary">
                                                    <Button>Maxrank {championData.spells[0].maxrank}</Button>
                                                    <Button>Cooldown Burn {championData.spells[0].cooldownBurn}</Button>
                                                </ButtonGroup>
                                            </CardActionArea>
                                        </CardContent>
                                    </Card>
                                </Grid>
                                <Grid item lg={6}>
                                    <Card variant="outlined" className={classes.alcenter}>
                                        <CardContent>
                                            <Typography variant="h5">{championData.spells[1].name}</Typography>
                                            <Typography variant="h5" component="h2" className={classes.alcenter}>
                                                <Avatar variant="rounded" sx={{ bgcolor: deepOrange[500] }}>
                                                    W
                                                </Avatar>{" "}
                                                &nbsp; &nbsp;
                                                <Avatar
                                                    variant="rounded"
                                                    src={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/spell/${championData.spells[1].image.full}`}
                                                    alt=""
                                                />
                                            </Typography>
                                            <Typography color="textSecondary" gutterBottom>
                                                RangeBurn:
                                                <br /> {championData.spells[1].rangeBurn}
                                            </Typography>
                                            <CardActionArea>
                                                <ButtonGroup variant="contained" size="small" color="primary">
                                                    <Button>Maxrank {championData.spells[1].maxrank}</Button>
                                                    <Button>Cooldown Burn {championData.spells[1].cooldownBurn}</Button>
                                                </ButtonGroup>
                                            </CardActionArea>
                                        </CardContent>
                                    </Card>
                                </Grid>
                                <Grid item lg={6}>
                                    <Card variant="outlined" className={classes.alcenter}>
                                        <CardContent>
                                            <Typography variant="h5">{championData.spells[2].name}</Typography>
                                            <Typography variant="h5" component="h2" className={classes.alcenter}>
                                                <Avatar variant="rounded" sx={{ bgcolor: deepOrange[500] }}>
                                                    E
                                                </Avatar>{" "}
                                                &nbsp; &nbsp;
                                                <Avatar
                                                    variant="rounded"
                                                    src={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/spell/${championData.spells[2].image.full}`}
                                                    alt=""
                                                />
                                            </Typography>
                                            <Typography color="textSecondary" gutterBottom>
                                                RangeBurn: <br />
                                                {championData.spells[2].rangeBurn}
                                            </Typography>
                                            <CardActionArea>
                                                <ButtonGroup variant="contained" size="small" color="primary">
                                                    <Button>Maxrank {championData.spells[2].maxrank}</Button>
                                                    <Button>Cooldown Burn {championData.spells[2].cooldownBurn}</Button>
                                                </ButtonGroup>
                                            </CardActionArea>
                                        </CardContent>
                                    </Card>
                                </Grid>
                                <Grid item lg={6}>
                                    <Card variant="outlined" className={classes.alcenter}>
                                        <CardContent>
                                            <Typography variant="h5">{championData.spells[3].name}</Typography>
                                            <Typography variant="h5" component="h2" className={classes.alcenter}>
                                                <Avatar variant="rounded" sx={{ bgcolor: deepOrange[500] }}>
                                                    R
                                                </Avatar>{" "}
                                                &nbsp; &nbsp;
                                                <Avatar
                                                    variant="rounded"
                                                    src={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/spell/${championData.spells[3].image.full}`}
                                                    alt=""
                                                />
                                            </Typography>
                                            <Typography color="textSecondary" gutterBottom>
                                                RangeBurn: <br />
                                                {championData.spells[3].rangeBurn}
                                            </Typography>
                                            <CardActionArea>
                                                <ButtonGroup variant="contained" size="small" color="primary">
                                                    <Button>Maxrank {championData.spells[3].maxrank}</Button>
                                                    <Button>Cooldown Burn {championData.spells[3].cooldownBurn}</Button>
                                                </ButtonGroup>
                                            </CardActionArea>
                                        </CardContent>
                                    </Card>
                                </Grid>
                            </Grid>
                        </Grid>
                        <Grid item lg={12}>
                            <Card variant="outlined" className={classes.alcenter}>
                                <CardContent>
                                    <Typography variant="h6" color="textSecondary">
                                        Passive Ability
                                    </Typography>
                                    <Typography variant="h5">{championData.passive.name}</Typography>
                                    <Typography variant="h5" component="h2" className={classes.alcenter}>
                                        <Avatar
                                            variant="rounded"
                                            src={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/${championData.passive.image.group}/${championData.passive.image.full}`}
                                            alt=""
                                        />
                                    </Typography>
                                    <Typography color="textSecondary" gutterBottom>
                                        {championData.passive.description}
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>
                    <Grid container justify="center">
                        {championData.allytips.length === 0 ? null : (
                            <Grid item lg={12}>
                                <Card variant="outlined" className={classes.alcenter}>
                                    <CardContent>
                                        <Typography variant="h4" color="primary">
                                            {`How does ${championName} contribute to a team?`}
                                        </Typography>
                                        <p>{championData.allytips.join("\r\n")}</p>
                                    </CardContent>
                                </Card>
                            </Grid>
                        )}
                        {championData.enemytips.length === 0 ? null : (
                            <Grid item lg={12}>
                                <Card variant="outlined" className={classes.alcenter}>
                                    <CardContent>
                                        <Typography variant="h4" color="secondary">
                                            {`How to fight against ${championName}?`}
                                        </Typography>
                                        <p>{championData.enemytips.join("\r\n")}</p>
                                    </CardContent>
                                </Card>
                            </Grid>
                        )}
                    </Grid>
                    <Grid container>
                        <Grid item lg={12}>
                            <BarChampions data={championData.stats}/>
                        </Grid>
                    </Grid>
                </div>
            )}
        </>
    );
}

export default DisplayChampion;
