import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Link as RouterLink } from "react-router-dom";
import axios from "axios";
import challenger from "../Assets/challenger.png";

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: "100%", // Fix IE 11 issue.
        marginTop: theme.spacing(3),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

export default function SignUp() {
    const classes = useStyles();
    const [userDetails, setUserDetails] = useState({ fname: "", lname: "", email: "", password: "" });
    const [conPass, setConPass] = useState("");

    function handleClick(e) {
        if (userDetails.password === conPass) {
            console.log(userDetails);
            axios
                .post("/api/auth/register", userDetails)
                .then((res) => {
                    console.log(res);
                    if (res.data.flag === false) {
                        alert("This email is already Registered 🚫. Please try another email");
                    } else {
                        alert("Registration Successful ✔");
                    }
                })
                .catch((err) => console.log(err));
        } else {
            alert("Passwords do not match. Please try again");
        }
        e.preventDefault();
    }

    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <div className={classes.paper}>
                <img style={{ height: "150px" }} src={challenger} alt="signup" />
                <Typography component="h1" variant="h5">
                    Sign up
                </Typography>
                <form className={classes.form} noValidate>
                    <Grid container spacing={2}>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                autoComplete="fname"
                                name="firstName"
                                variant="outlined"
                                required
                                fullWidth
                                id="firstName"
                                label="First Name"
                                value={userDetails.fname}
                                onChange={(e) => {
                                    setUserDetails({ ...userDetails, fname: e.target.value });
                                }}
                                autoFocus
                            />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                variant="outlined"
                                required
                                fullWidth
                                id="lastName"
                                label="Last Name"
                                name="lastName"
                                autoComplete="lname"
                                value={userDetails.lname}
                                onChange={(e) => {
                                    setUserDetails({ ...userDetails, lname: e.target.value });
                                }}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                fullWidth
                                id="email"
                                label="Email Address"
                                name="email"
                                autoComplete="email"
                                value={userDetails.email}
                                onChange={(e) => {
                                    setUserDetails({ ...userDetails, email: e.target.value });
                                }}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                fullWidth
                                name="password"
                                label="Password"
                                type="password"
                                id="password"
                                autoComplete="current-password"
                                value={userDetails.password}
                                onChange={(e) => {
                                    setUserDetails({ ...userDetails, password: e.target.value });
                                }}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                variant="outlined"
                                required
                                fullWidth
                                name="password"
                                label="Confirm Password"
                                type="password"
                                id="conpassword"
                                autoComplete="current-password"
                                value={conPass}
                                onChange={(e) => {
                                    setConPass(e.target.value);
                                }}
                            />
                        </Grid>
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        onClick={(e) => handleClick(e)}
                    >
                        Sign Up
                    </Button>
                    <Grid container>
                        <Grid item>
                            <Link component={RouterLink} to="/sign-in" variant="body2">
                                Already have an account? Sign in
                            </Link>
                        </Grid>
                    </Grid>
                </form>
            </div>
            <Box mt={5}></Box>
        </Container>
    );
}
