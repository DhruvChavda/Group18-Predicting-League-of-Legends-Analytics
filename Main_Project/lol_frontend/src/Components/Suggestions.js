import React, { useState } from "react";
// import Link from "@material-ui/core/Link";
// import { makeStyles } from "@material-ui/core/styles";
// import chartData from "../Data/chartData";
import {
    Button,
    FormControl,
    InputLabel,
    makeStyles,
    MenuItem,
    Select,
    TextField,
    Typography,
} from "@material-ui/core";
import BarSuggesstion from "./BarSuggesstion";
import axios from "axios"; //Uncomment this

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
        margin: "5px",
        minWidth: 200,
    },
    selectBox: {
        margin: "5px",
        minWidth: 150,
    },
    selectEmpty: {
        // marginTop: theme.spacing(2),
    },
});

export default function Suggestions() {
    const [reg, setReg] = useState("");
    const [sumName, setSumName] = useState("");
    const [fields, setFields] = useState({ summonername: "", region: "" });
    const [chartData, setChartData] = useState(null);

    const classes = useStyles();

    function handleClick(e) {
        console.log(sumName);
        console.log(reg);
        setFields({ summonername: sumName, region: reg });
        axios
            .post("/api/suggestion", { region: reg, summnorname: sumName })
            .then((res) => {
                console.log(res);
                setChartData(res.data);
            })
            .catch((err) => console.log(err));
    }

    return (
        <div>
            <Typography component="p" variant="h4" color="textPrimary">
                Enter your Summoner Name and Get Suggestions
            </Typography>
            <FormControl className={classes.formControl}>
                <TextField
                    variant="outlined"
                    required
                    id="summonerName"
                    label="Summoner Name"
                    name="summonerName"
                    onChange={(e) => {
                        setSumName(e.target.value);
                    }}
                    value={sumName}
                    autoFocus
                />
            </FormControl>
            <FormControl variant="outlined" className={classes.selectBox}>
                <InputLabel id="region select">Region</InputLabel>
                <Select
                    labelId="demo-simple-select-outlined-label"
                    id="region-select"
                    value={reg}
                    onChange={(e) => {
                        setReg(e.target.value);
                    }}
                    label="region"
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
            <Typography variant="h5">
                <Button variant="contained" color="primary" onClick={(e) => handleClick(e)}>
                    Get Suggesstions!
                </Button>
            </Typography>

            {fields.region !== "" && fields.summonername !== "" && chartData !== null && (
                <>
                    <Typography className={classes.root}>Suggesstions</Typography>
                    <BarSuggesstion data={chartData} />
                </>
            )}
        </div>
    );
}
