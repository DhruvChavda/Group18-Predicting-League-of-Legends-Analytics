import React from "react";
import { Card, CardContent, Grid, makeStyles, Box, Typography } from "@material-ui/core";

const useStyles = makeStyles({
    root: {
        background: "#f2e4fd",
    },
});

function PlayStyle(props) {
    const size = 3;

    const dataL = props.data.lane;
    const dataL2 = dataL.slice(0, size);

    const dataR = props.data.role;
    const dataR2 = dataR.slice(0, size);

    const classes = useStyles();

    return (
        <>
            <div style={{ width: "100%" }}>
                <Box textAlign="center" p={3}>
                    <Typography variant="h5">Top 3 Lanes:</Typography>
                </Box>

                <Grid container spacing={4} direction="row" justify="center">
                    {dataL2.map((elem) => (
                        <Grid item xs={12} sm={6} md={3}>
                            <Card className={classes.root}>
                                <CardContent>
                                    <Box textAlign="center">
                                        <Typography gutterBottom variant="subtitle1" component="h3">
                                            {`${elem[0]}`}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            {`Chosen in ${elem[1]} of last 100 games`}
                                        </Typography>
                                    </Box>
                                </CardContent>
                            </Card>
                        </Grid>
                    ))}
                </Grid>

                <Box textAlign="center" p={3}>
                    <Typography variant="h5">Top 3 Roles:</Typography>
                </Box>

                <Grid container spacing={4} direction="row" justify="center">
                    {dataR2.map((elem) => (
                        <Grid item xs={12} sm={6} md={3}>
                            <Card className={classes.root}>
                                <CardContent>
                                    <Box textAlign="center">
                                        <Typography gutterBottom variant="subtitle1" component="h3">
                                            {`${elem[0]}`}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            {`In ${elem[1]} of last 100 games`}
                                        </Typography>
                                    </Box>
                                </CardContent>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </div>
        </>
    );
}

export default PlayStyle;
