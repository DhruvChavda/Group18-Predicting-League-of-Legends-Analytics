import React from "react";
import { Card, CardContent, Grid, Box, Typography } from "@material-ui/core";

function PersonalWL(props) {
    return (
        <>
            <div style={{ width: "100%" }}>
                <Box textAlign="center" p={3}>
                    <Typography variant="h5">Match Statistics:</Typography>
                </Box>

                <Grid container spacing={4} direction="row" justify="center">
                    <Grid item xs={12} sm={6} md={3}>
                        <Box border={1}>
                            <Card>
                                <CardContent>
                                    <Box textAlign="center">
                                        <Typography gutterBottom variant="subtitle2" component="h3">
                                            {`League Points: ${props.data.leaguePoints}`}
                                        </Typography>
                                    </Box>
                                </CardContent>
                            </Card>

                            <Card>
                                <CardContent>
                                    <Box textAlign="center">
                                        <Typography gutterBottom variant="subtitle2" component="h3">
                                            {`Wins: ${props.data.wins}`}
                                        </Typography>
                                    </Box>
                                </CardContent>
                            </Card>

                            <Card>
                                <CardContent>
                                    <Box textAlign="center">
                                        <Typography gutterBottom variant="subtitle2" component="h3">
                                            {`Losses: ${props.data.losses}`}
                                        </Typography>
                                    </Box>
                                </CardContent>
                            </Card>

                            <Card>
                                <CardContent>
                                    <Box textAlign="center">
                                        <Typography gutterBottom variant="subtitle2" component="h3">
                                            {`Tier: ${props.data.tier} ${props.data.rank}`}
                                        </Typography>
                                    </Box>
                                </CardContent>
                            </Card>

                            
                        </Box>
                    </Grid>
                </Grid>
            </div>
        </>
    );
}

export default PersonalWL;
