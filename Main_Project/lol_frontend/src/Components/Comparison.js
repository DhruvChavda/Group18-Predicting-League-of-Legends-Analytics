import React, { useState } from "react";
// import Link from "@material-ui/core/Link";
// import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import { Link as RouterLink } from "react-router-dom";
import {
    Button,
    ButtonGroup,
    FormControl,
    Grid,
    InputLabel,
    makeStyles,
    MenuItem,
    Select,
    Box,
    Card,
    CardMedia,
    CardContent,
    CardActionArea,
    TextField,
} from "@material-ui/core";
import axios from "axios";
import { borders } from '@material-ui/system'
import PersonalWL from "./PersonalWL"

const useStyles = makeStyles({
    root: {
        margin: 10,
        padding: 5,
        background: "#db8762",
    },
    root2: {
        background: "#83c4ef"
    },
    table: {
        minWidth: "100%",
    },
    formControl: {
        textAlign: "center",
        margin: 5,
        minWidth: 170,
    },
    selectEmpty: {
        // marginTop: theme.spacing(2),
    },
    
});

export default function Comparison() {
    const [reg1, setReg1] = useState();
    const [reg2, setReg2] = useState();
    const [play1, setPlay1] = useState();
    const [play2, setPlay2] = useState();
    const [play1det, setPlay1det] = useState(null);
    const [play2det, setPlay2det] = useState(null);
    const [flag1, setFlag1] = useState(false);
    const [flag2, setFlag2] = useState(false);

    function handleSubmit() {

        
        axios
            .post("http://127.0.0.1:8000/api/playerCompare", { region: [reg1, reg2], player: [play1, play2] })
            .then((res) => {
                console.log(res);
                
                const x = Object.values(res.data);

                
                const final1 = x[0]
                const final2 = x[1]
                const finalvals1 = Object.values(final1)
                const finalvals2 = Object.values(final2)
                // setLeagueData(finalvals[9][0]);
                if(finalvals1[9].length===0)
                {
                    setFlag1(true);
                    // console.log('yes')
                }
                else
                {
                    setFlag1(false);
                }
                if(finalvals2[9].length===0)
                {
                    setFlag2(true);
                    // console.log('yes')
                }
                else
                {
                    setFlag2(false);
                }

                console.log(finalvals1);
                setPlay1det(finalvals1);
                console.log(finalvals2);
                setPlay2det(finalvals2);
            })
            .catch((err) => console.log(err));
        // POST request here

        
    }
    const classes = useStyles();
    return (
        <React.Fragment>
            <Grid container justify="center">
                <Grid item lg={6}>
                    <FormControl className={classes.formControl}>
                        <TextField
                            variant="outlined"
                            required
                            id="summonerName"
                            label="Summoner Name"
                            name="summonerName"
                            value={play1 || ""}
                            onChange={(e) => setPlay1(e.target.value)}
                            autoFocus
                        />
                  </FormControl>
                    <FormControl variant="outlined" className={classes.formControl}>
                        <InputLabel id="region select">Region</InputLabel>
                        <Select
                            labelId="demo-simple-select-outlined-label"
                            id="region-select"
                            value={reg1}
                            onChange={(e) => setReg1(e.target.value)}
                            label="Challenger"
                        >
                            <MenuItem value={"br1"}>br 1</MenuItem>
                            <MenuItem value={"eun1"}>eun 1</MenuItem>
                            <MenuItem value={"euw1"}>euw 1</MenuItem>
                            <MenuItem value={"jp1"}>jp 1</MenuItem>
                            <MenuItem value={"kr"}>kr</MenuItem>
                            <MenuItem value={"la1"}>la 1</MenuItem>
                            <MenuItem value={"la2"}>la 2</MenuItem>
                            <MenuItem value={"na1"}>na 1</MenuItem>
                            <MenuItem value={"oc1"}>oc 1</MenuItem>
                            <MenuItem value={"ru"}>ru</MenuItem>
                            <MenuItem value={"tr1"}>tr 1</MenuItem>
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item lg={6}>
                    <FormControl className={classes.formControl}>
                        <TextField
                            variant="outlined"
                            required
                            id="summonerName"
                            label="Summoner Name"
                            name="summonerName"
                            value={play2 || ""}
                            onChange={(e) => setPlay2(e.target.value)}
                        />
                    </FormControl>
                    <FormControl variant="outlined" className={classes.formControl}>
                        <InputLabel id="region select">Region</InputLabel>
                        <Select
                            labelId="demo-simple-select-outlined-label"
                            id="region-select"
                            value={reg2}
                            onChange={(e) => setReg2(e.target.value)}
                            label="Challenger"
                        >
                            <MenuItem value={"br1"}>br 1</MenuItem>
                            <MenuItem value={"eun1"}>eun 1</MenuItem>
                            <MenuItem value={"euw1"}>euw 1</MenuItem>
                            <MenuItem value={"jp1"}>jp 1</MenuItem>
                            <MenuItem value={"kr"}>kr</MenuItem>
                            <MenuItem value={"la1"}>la 1</MenuItem>
                            <MenuItem value={"la2"}>la 2</MenuItem>
                            <MenuItem value={"na1"}>na 1</MenuItem>
                            <MenuItem value={"oc1"}>oc 1</MenuItem>
                            <MenuItem value={"ru"}>ru</MenuItem>
                            <MenuItem value={"tr1"}>tr 1</MenuItem>
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item lg={12}>
                    <Typography variant="h3">
                        <ButtonGroup variant="contained" color="primary">
                            <Button fullWidth onClick={() => handleSubmit()}>
                                Compare!
                            </Button>
                        </ButtonGroup>
                    </Typography>
                </Grid>
            </Grid>
            {play1det && play2det && (
                <>
                    <Grid container justify="space-evenly">
                        <Grid item lg={6}>
                            <Box textAlign='center' p={3}>
                            <Button variant="outlined" color="secondary" disableElevation>
                                <Typography variant='h4'>
                                    {`${play1}`}

                                </Typography>
                            
                            </Button>
                            </Box>


                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Top Champion

                                </Typography>
                            

                            </Box>

                            <CardActionArea component={RouterLink} to={`/champions/${play1det[2].replace(/\s+/g,'')}`}>
                            <Card
                                className={classes.root}
                            >
                            <CardMedia
                                component="img"
                                alt="Champion Pic"
                                height="100"
                                
                                image={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/champion/${play1det[2].replace(/\s+/g,'')}.png`}
                                title="Champion"
                            />
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="h5" component="h2">
                                    {`${play1det[2]}`}
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>
                            </CardActionArea>
                            
                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Preferred Lane

                                </Typography>
                            

                            </Box>

                            <Card
                                className={classes.root2}
                            >
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle1" component="h3">
                                    {`${play1det[5]}`}
                                </Typography>
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Preferred Role

                                </Typography>
                            

                            </Box>

                            <Card
                                className={classes.root2}
                            >
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle1" component="h3">
                                    {`${play1det[7]}`}
                                </Typography>
                                </Box>
                            </CardContent>
                            
                            </Card>


                            {!flag1 && play1det[9][0] !== null &&
                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Match Statistics

                                </Typography>
                            

                            </Box>
                            }
                            {!flag1 && play1det[9][0] !== null &&
                            <Box border={1}>
                            <Card>
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`League Points: ${play1det[9][0].leaguePoints}`} 
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Card>
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`Wins: ${play1det[9][0].wins}`}
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Card>
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`Losses: ${play1det[9][0].losses}`}
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Card>
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`Tier: ${play1det[9][0].tier} ${play1det[9][0].rank}`} 
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            

                            </Box>
                            }


                        </Grid>
                        <Grid item lg={6}>
                            <Box textAlign='center' p={3}>
                            <Button variant="outlined" color="secondary" disableElevation>
                                <Typography variant='h4'>
                                    {`${play2}`}

                                </Typography>
                            
                            </Button>
                            </Box>


                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Top Champion

                                </Typography>
                            

                            </Box>

                            <CardActionArea component={RouterLink} to={`/champions/${play2det[2].replace(/\s+/g,'')}`}>
                            <Card
                                className={classes.root}
                            >
                            <CardMedia
                                component="img"
                                alt="Champion Pic"
                                height="100"
                                
                                image={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/champion/${play2det[2].replace(/\s+/g,'')}.png`}
                                title="Champion"
                            />
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="h5" component="h2">
                                    {`${play2det[2]}`}
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>
                            </CardActionArea>
                            

                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Preferred Lane

                                </Typography>
                            

                            </Box>

                            <Card
                                className={classes.root2}
                            >
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle1" component="h3">
                                    {`${play2det[5]}`}
                                </Typography>
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Preferred Role

                                </Typography>
                            

                            </Box>

                            <Card
                                className={classes.root2}
                            >
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle1" component="h3">
                                    {`${play2det[7]}`}
                                </Typography>
                                </Box>
                            </CardContent>
                            
                            </Card>

                            {!flag2 && play2det[9][0] !== null &&
                            <Box textAlign='center' p={3}>
                            
                                <Typography variant='h5'>
                                    Match Statistics

                                </Typography>
                            

                            </Box>
                            }
                                                        
                            {!flag2 && play2det[9][0] !== null &&
                            <Box border={1}>

                            <Card>
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`League Points: ${play2det[9][0].leaguePoints}`} 
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Card>
                            

                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`Wins: ${play2det[9][0].wins}`}
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Card>
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`Losses: ${play2det[9][0].losses}`}
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            <Card>
                            
                            <CardContent>
                                <Box textAlign = "center">
                                <Typography gutterBottom variant="subtitle2" component="h3">
                                    {`Tier: ${play2det[9][0].tier} ${play2det[9][0].rank}`} 
                                </Typography>
                                
                                </Box>
                            </CardContent>
                            
                            </Card>

                            
                            </Box>
                            } 

                        </Grid>
                    </Grid>
                </>
            )}
        </React.Fragment>
    );
}