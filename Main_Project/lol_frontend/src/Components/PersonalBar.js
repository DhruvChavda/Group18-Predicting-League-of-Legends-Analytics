import React, { useEffect, useState } from "react";
import { Link as RouterLink } from "react-router-dom";
import {
    CardActionArea,
    Card,
    CardContent,
    CardMedia,
    Grid,
    Box,
    Typography,
} from "@material-ui/core";

function PersonalDetails(props) { 
    const size = 3; 
    const recoData = props.data.recommand;
    // const displayReco = recoData.slice(0, size).map((x) => x[1] * 100);
    // const recoLabel = recoData.slice(0, size).map((x) => x[0]);

    const usedData = props.data.used;
    const dataC2 = usedData.slice(0, size);
    const displayUsed = usedData.slice(0, size).map((x) => x[1] * 100);
    const usedLabel = recoData.slice(0, size).map((x) => x[0]);
    
    return (
        <>  

            


            
            <div style={{ width: "100%" }}>
                    <Box textAlign="center" p = {3}>
                            
                            <Typography variant='h5'>
                                Top 3 Champions:

                            </Typography>
                    </Box> 
                

                <Grid
                container
                spacing={4}
                direction="row"
                justify="center"
                
                >
                    {dataC2.map(elem => (
                        
                        
                        // {`${elem[0]}` ==='None'?null:
                        
                        <Grid item xs={12} sm={6} md={3} >
                            <CardActionArea component={RouterLink} to={`/champions/${elem[0].replace(/\s+/g,'')}`}>
                            <Card>
                            <CardMedia
                                component="img"
                                alt="Champion Pic"
                                height="100"
                                
                                image={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/champion/${elem[0].replace(/\s+/g,'')}.png`}
                                title="Champion"
                            />
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="h5" component="h2">
                                    {`${elem[0]}`}
                                </Typography>
                                <Typography variant="body2" color="textSecondary" component="p">
                                    {`Used in ${elem[1].toFixed(2)*100}% of recent games`}
                                </Typography>
                                </Box>
                            </CardContent>
                            
                            </Card>
                            </CardActionArea>
                        </Grid>
                        // }
                    ))}
                </Grid>
                

            </div>
        </>
    );
}

export default PersonalDetails;