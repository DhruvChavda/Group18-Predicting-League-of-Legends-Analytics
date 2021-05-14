import { Grid, makeStyles, Paper, Typography, Box } from "@material-ui/core";
import React from "react";
import logop from "../Assets/provisional.png";
import logob from "../Assets/bronze.png";
import logos from "../Assets/silver.png";
import logog from "../Assets/gold.png";
import logod from "../Assets/diamond.png";

const useStyles = makeStyles({
    title: {
        color: "#2874A6",
        textAlign: "center",
    },
    subt: {
        color: "#6C3483",
        textAlign: "center",
    },
    ter: {
        color: "#555555",
        textAlign: "center",
    },
    cont: {
        marginTop: "35px",
    },
    pad: {
        padding: "10px",
    },
});

function Home() {
    const classes = useStyles();
    return (
        <>
            <Grid container justify="center">
                <Grid item lg={1}></Grid>
                <Grid item lg={2} className={classes.root}>
                    <img src={logop} alt="logo" height="100px"></img>
                </Grid>
                <Grid item lg={2} className={classes.root}>
                    <img src={logog} alt="logo" height="100px"></img>
                </Grid>
                <Grid item lg={2} className={classes.root}>
                    <img src={logod} alt="logo" height="100px"></img>
                </Grid>
                <Grid item lg={2} className={classes.root}>
                    <img src={logos} alt="logo" height="100px"></img>
                </Grid>
                <Grid item lg={2} className={classes.root}>
                    <img src={logob} alt="logo" height="100px"></img>
                </Grid>
                <Grid item lg={12}>
                    <Box textAlign='Center' p = {3}>
                    <Typography variant="h2" className={classes.title}>
                        Welcome To League of Legends Analytics!
                    </Typography>
                    </Box>
                </Grid>
                <Grid item lg={8}>
                    <Box textAlign='Center' p = {3}>
                    <Typography variant="h4" className={classes.subt}>
                        Your One Stop Solution to learn and excel at the world's most popular MOBA!
                    </Typography>
                    </Box>
                </Grid>
            </Grid>
            <Grid container justify="space-evenly" className={classes.cont} spacing={2}>
                <Grid item lg={6}>
                    <Paper className={classes.pad}>
                        <Box textAlign='Center' p = {3}>
                        <Typography variant="h5" className={classes.ter}>
                            Why to have such an app?
                        </Typography>
                        </Box>
                        <Box textAlign='Center' p = {3}>

                        
                        <Typography variant="h6" color="textSecondary">
                            League of Legends is one of the most difficult games to master, especially with all the Champions, Items and strategies it has, our app simply helps you keep track of your playstyle alongwith some custom tailored suggestions!
                        </Typography>
                        </Box>
                    </Paper>
                </Grid>
                <Grid item lg={6}>
                    <Paper Paper className={classes.pad}>
                        <Box textAlign='Center' p = {3}>
                        <Typography variant="h5" className={classes.ter}>
                            What do we have for you?
                        </Typography>
                        </Box>
                        <Box textAlign='Center' p = {3}>
                        <Typography variant="h6" color="textSecondary">
                            Information about champions, stats about players, awesome suggestions and comparisons!
                        </Typography>
                        </Box>
                    </Paper>
                </Grid>
            </Grid>
            <Grid container justify="space-evenly" className={classes.cont} spacing={2}>

                <Typography variant="h4" color="primary">
                    Explore the app <b>Now!</b>
                </Typography>
            </Grid>
        </>
    );
}

export default Home;
