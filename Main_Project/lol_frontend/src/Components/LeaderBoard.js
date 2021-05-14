import React, { useState } from "react";
import axios from "axios";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import { Button, Paper, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/styles";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";

const useStyles = makeStyles({
    root: {
        margin: 10,
        padding: 5,
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

export default function BasicTable() {
    const classes = useStyles();

    const [param, setParam] = useState({
        league: "",
        queue: "",
        region: "",
    });

    const [dat, setDat] = useState(null);

    const handleClick = () => {
        console.log(param);
        axios
            .post("/api/leaderBoard", param)
            .then((res) => {
                console.log(res.data);
                setDat(res.data);
            })
            .catch((err) => console.log(err));
    };

    const handleChangeRegion = (event) => {
        setParam({ ...param, region: event.target.value });
    };

    const handleChangeQueue = (event) => {
        setParam({ ...param, queue: event.target.value });
    };

    const handleChangeLeague = (event) => {
        setParam({ ...param, league: event.target.value });
    };

    return (
        <React.Fragment>
            <Paper elevation={2} className={classes.root}>
                <FormControl variant="outlined" className={classes.formControl}>
                    <InputLabel id="demo-simple-select-outlined-label">League</InputLabel>
                    <Select
                        labelId="demo-simple-select-outlined-label"
                        id="league-select"
                        value={param.leagues_arr}
                        onChange={handleChangeLeague}
                        required
                        label="Leagues"
                    >
                        <MenuItem value={"challengerleagues"}>Challenger Leagues</MenuItem>
                        <MenuItem value={"grandmasterleagues"}>Grand Master Leagues</MenuItem>
                        <MenuItem value={"masterleagues"}>Master Leagues</MenuItem>
                    </Select>
                </FormControl>

                <FormControl variant="outlined" className={classes.formControl}>
                    <InputLabel id="demo-simple-select-outlined-label">Queue Type</InputLabel>
                    <Select
                        labelId="queue-select"
                        id="queue-select"
                        value={param.queue_arr}
                        onChange={handleChangeQueue}
                        label="Queue Type"
                    >
                        <MenuItem value={"RANKED_SOLO_5x5"}>Solo Rank</MenuItem>
                        <MenuItem value={"RANKED_FLEX_SR"}>Flex Rank</MenuItem>
                    </Select>
                </FormControl>

                <FormControl variant="outlined" className={classes.formControl}>
                    <InputLabel id="region select">Region</InputLabel>
                    <Select
                        labelId="demo-simple-select-outlined-label"
                        id="region-select"
                        value={param.region_arr}
                        onChange={handleChangeRegion}
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
                <Button variant="contained" color="primary" onClick={handleClick}>
                    Submit
                </Button>
            </Paper>
            {dat === null ? (
                <Typography variant="h4" color="textSecondary" align="center">
                    Leaderboard Will be Shown Here Soon! 
                </Typography>
            ) : (
                <Paper className={classes.table} elevation={2}>
                    <TableContainer>
                        <Table aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell align="center">Rank</TableCell>
                                    <TableCell align="center">Summoner Name</TableCell>
                                    <TableCell align="center">LP</TableCell>
                                    <TableCell align="center">Wins</TableCell>
                                    <TableCell align="center">Loss</TableCell>
                                    <TableCell align="center">Win Rate</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {dat.map((x, ind) => (
                                    <TableRow key={ind}>
                                        <TableCell align="center">{ind + 1}</TableCell>
                                        <TableCell align="center">{x[0]}</TableCell>
                                        <TableCell align="center">{x[1]}</TableCell>
                                        <TableCell align="center">{x[2]}</TableCell>
                                        <TableCell align="center">{x[3]}</TableCell>
                                        <TableCell align="center">{x[4].toFixed(2)} %</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                </Paper>
            )}
        </React.Fragment>
    );
}
