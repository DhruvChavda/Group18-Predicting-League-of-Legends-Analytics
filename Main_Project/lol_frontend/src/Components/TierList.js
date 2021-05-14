import React from "react";
// import Link from "@material-ui/core/Link";
// import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import {
    makeStyles,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
} from "@material-ui/core";
import dat from "../Data/tier_list";
import { Link as RouterLink } from "react-router-dom";
// import Title from "./Title";

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

export default function Profile() {
    const classes = useStyles();
    return (
        <React.Fragment>
            <Typography component="p" variant="h4">
                This is TierList!
            </Typography>
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
                                    <TableCell align="center">Champion Name</TableCell>
                                    <TableCell align="center">Pick Rate</TableCell>
                                    <TableCell align="center">Ban Rate</TableCell>
                                    <TableCell align="center">Total Matches</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {dat.map((x, ind) => (
                                    <TableRow component={RouterLink} to={`/champions/${x.name}`} key={ind}>
                                        <TableCell align="center">{ind + 1}</TableCell>
                                        <TableCell align="center">{x.name}</TableCell>
                                        <TableCell align="center">{x.pick}</TableCell>
                                        <TableCell align="center">{x.ban}</TableCell>
                                        <TableCell align="center">{x.total_Matches}</TableCell>
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