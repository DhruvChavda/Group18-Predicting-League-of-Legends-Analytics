import React from "react";
// import Link from "@material-ui/core/Link";
// import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import { Button, Grid,Link } from "@material-ui/core";
import { GetApp } from "@material-ui/icons";

export default function DownloadApp() {
    return (
        <React.Fragment>
            <Grid container justify="center">
                <Grid item lg={10}>
                    <Typography variant="h4" color="primary">
                        Download Our Real Time Analytics App for best results!
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        This app is designed to <b>Predict</b> the outcome of the match based on you playstyle. the app
                        seamlessly connects to the game's client api and shows useful information like{" "}
                        <b>Kills Deaths and Assists.</b>
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        It integrates this API information along with MACHINE LEARNING to suggests specific lanes for
                        which a champion should be played,along with the champion level and ability levels with around{" "}
                        <b>80%</b>
                        accuracy.
                    </Typography>
                </Grid>
                <Grid item lg={6}>
                    <Typography variant="h4" color="secondary">
                        How to use this App?
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        1. Download the App to your device
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        2. Open the App (Make Sure that you're inside a match in the game)
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        3. KaBOOM! follow the 'Ray of Light' (our App) 😁
                    </Typography>
                </Grid>
                <Grid item lg={6}>
                    <Typography variant="h4" color="secondary">
                        To Download the App, follow the given Steps:
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        1. Click on the button below. It'll redirect you to a google drive link!
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        2. It'll download an .exe file
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                        3. No need to install it. It's ready to ROCK!
                    </Typography>
                    <Link
                        rel="noopener noreferrer"
                        href="https://drive.google.com/file/d/1a7ZCNwulPKTiPWqKOIhO3PWdHNoK8x__/view?usp=sharing"
                        target="_blank"
                    >
                        <Button startIcon={<GetApp />} variant="contained" color="primary">
                            DOWNLOAD
                        </Button>
                    </Link>
                </Grid>
            </Grid>
        </React.Fragment>
    );
}
