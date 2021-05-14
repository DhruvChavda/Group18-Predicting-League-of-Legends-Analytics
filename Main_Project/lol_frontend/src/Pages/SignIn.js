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
import { Link as RouterLink, Redirect } from "react-router-dom";
// import GoogleLogin from "react-google-login";
import master from "../Assets/master.png";
import axios from "axios";

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
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

export default function SignIn(props) {
    const classes = useStyles();
    const [userDetails, setUserDetails] = useState({ email: "", password: "" });

    // const responseGoogle = (response) => {
    //     console.log(response);
    // };

    function handleClick(e) {
        console.log(userDetails);
        axios
            .post("/api/auth/login", userDetails)
            .then((res) => {
                console.log(res);
                if (res.data.flag === false) {
                    alert("Email or Password Incorrect!");
                } else {
                    alert("Logged in successfully!");
                    props.setFlag(true);
                    <Redirect to="/" />;
                    setUserDetails({ email: "", password: "" });
                }
            })
            .catch((err) => console.log(err));
        e.preventDefault();
    }

    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <div className={classes.paper}>
                <img style={{ height: "150px" }} src={master} alt="signin" />
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <form className={classes.form} noValidate>
                    <TextField
                        variant="outlined"
                        margin="normal"
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
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        value={userDetails.password}
                        onChange={(e) => {
                            setUserDetails({ ...userDetails, password: e.target.value });
                        }}
                        autoComplete="current-password"
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        onClick={(e) => handleClick(e)}
                    >
                        Sign In
                    </Button>
                    {/* <Typography align="center" variant="h6" color="primary">
                        OR
                    </Typography>
                    <Typography align="center" gutterBottom m={5}>
                        <GoogleLogin
                            clientId="" //  CLIENT ID GOES HERE AS A STRING
                            buttonText="Sign-In using Google"
                            onSuccess={responseGoogle}
                            onFailure={responseGoogle}
                            cookiePolicy={"single_host_origin"}
                            align="center"
                        />
                    </Typography> */}
                    <Grid container>
                        <Grid item xs>
                            <Link href="#" variant="body2">
                                Forgot password?
                            </Link>
                        </Grid>
                        <Grid item>
                            <Link component={RouterLink} to="/sign-up" variant="body2">
                                {"Don't have an account? Sign Up"}
                            </Link>
                        </Grid>
                    </Grid>
                </form>
            </div>
            <Box mt={8}></Box>
        </Container>
    );
}
