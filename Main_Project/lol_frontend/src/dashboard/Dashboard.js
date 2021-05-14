import React, { useEffect, useState } from "react";
import clsx from "clsx";
import {
    ButtonGroup,
    Link,
    IconButton,
    Container,
    Drawer,
    Typography,
    Divider,
    Box,
    AppBar,
    Toolbar,
    List,
    CssBaseline,
    Button,
    Grid,
    makeStyles,
} from "@material-ui/core";
import MenuIcon from "@material-ui/icons/Menu";
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft";
import { MainListItems, SecondaryListItems } from "./listItems";
import SignIn from "../Pages/SignIn";
import SignUp from "../Pages/SignUp";
import Champions from "../Components/Champions";
import Items from "../Components/Items";
import TierList from "../Components/TierList";
import Leaderboard from "../Components/LeaderBoard";
import HowToPlay from "../Components/HowToPlay";

import PersonalStats from "../Components/PersonalStats";
import Suggestions from "../Components/Suggestions";
import { ExitToApp, Person, PersonAdd } from "@material-ui/icons";
import { Route, Switch, Link as RouterLink } from "react-router-dom";
import Comparison from "../Components/Comparison";
import DownloadApp from "../Components/DownloadApp";
import DisplayChampion from "../Pages/DisplayChampion";
import Home from "../Components/Home";
import ProtectedRoutes from "../ProtectedRoutes";

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {"Copyright © "}
            <Link color="inherit" href="#">
                League of Legends analytics
            </Link>{" "}
            {new Date().getFullYear()}
            {"."}
        </Typography>
    );
}

const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
    },
    toolbar: {
        paddingRight: 24, // keep right padding when drawer closed
    },
    toolbarIcon: {
        display: "flex",
        alignItems: "center",
        justifyContent: "flex-end",
        padding: "0 8px",
        ...theme.mixins.toolbar,
    },
    appBar: {
        zIndex: theme.zIndex.drawer + 1,
        transition: theme.transitions.create(["width", "margin"], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
    },
    appBarShift: {
        marginLeft: drawerWidth,
        width: `calc(100% - ${drawerWidth}px)`,
        transition: theme.transitions.create(["width", "margin"], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen,
        }),
    },
    menuButton: {
        marginRight: 36,
    },
    menuButtonHidden: {
        display: "none",
    },
    title: {
        flexGrow: 1,
    },
    drawerPaper: {
        position: "relative",
        whiteSpace: "nowrap",
        width: drawerWidth,
        transition: theme.transitions.create("width", {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen,
        }),
    },
    drawerPaperClose: {
        overflowX: "hidden",
        transition: theme.transitions.create("width", {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        width: theme.spacing(7),
        [theme.breakpoints.up("sm")]: {
            width: theme.spacing(9),
        },
    },
    appBarSpacer: theme.mixins.toolbar,
    content: {
        flexGrow: 1,
        height: "100vh",
        overflow: "auto",
    },
    container: {
        paddingTop: theme.spacing(4),
        paddingBottom: theme.spacing(4),
    },
    paper: {
        padding: theme.spacing(2),
        display: "flex",
        overflow: "auto",
        flexDirection: "column",
    },
    fixedHeight: {
        height: 240,
    },
}));

export default function Dashboard() {
    const classes = useStyles();
    const [title, setTitle] = useState("Dashboard");
    const [open, setOpen] = useState(true);
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        document.title = title;
    }, [title]);

    function changeTitle(newTitle) {
        return setTitle(newTitle);
    }

    function authSet(flag) {
        return setIsAuthenticated(flag);
    }

    const handleDrawerOpen = () => {
        setOpen(true);
    };
    const handleDrawerClose = () => {
        setOpen(false);
    };

    return (
        <div className={classes.root}>
            <CssBaseline />
            <AppBar position="absolute" className={clsx(classes.appBar, open && classes.appBarShift)}>
                <Toolbar className={classes.toolbar}>
                    <IconButton
                        edge="start"
                        color="inherit"
                        aria-label="open drawer"
                        onClick={handleDrawerOpen}
                        className={clsx(classes.menuButton, open && classes.menuButtonHidden)}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
                        {title}
                    </Typography>
                    {!isAuthenticated && (
                        <ButtonGroup className={classes.root} size="large" color="default" variant="contained">
                            <Button
                                startIcon={<Person />}
                                component={RouterLink}
                                to="/sign-in"
                                onClick={() => {
                                    setTitle("sign-in");
                                }}
                            >
                                SignIn
                            </Button>
                            <Button
                                startIcon={<PersonAdd />}
                                component={RouterLink}
                                to="/sign-up"
                                onClick={() => {
                                    setTitle("sign-up");
                                }}
                            >
                                SignUp
                            </Button>
                        </ButtonGroup>
                    )}
                    {isAuthenticated && (
                        <ButtonGroup className={classes.root} size="large" color="default" variant="contained">
                            <Button
                                startIcon={<ExitToApp />}
                                component={RouterLink}
                                to="#"
                                onClick={() => {
                                    setTitle("Logging Out");
                                    setIsAuthenticated(false);
                                }}
                            >
                                LogOut
                            </Button>
                        </ButtonGroup>
                    )}
                </Toolbar>
            </AppBar>
            <Drawer
                variant="permanent"
                classes={{
                    paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
                }}
                open={open}
            >
                <div className={classes.toolbarIcon}>
                    <IconButton onClick={handleDrawerClose}>
                        <ChevronLeftIcon />
                    </IconButton>
                </div>
                <Divider />
                <List>{<MainListItems title={title} changeTitle={changeTitle} />}</List>
                <Divider />
                <List>{<SecondaryListItems title={title} changeTitle={changeTitle} />}</List>
            </Drawer>
            <main className={classes.content}>
                <div className={classes.appBarSpacer} />
                <Container maxWidth="lg" className={classes.container}>
                    <Grid container spacing={3}>
                        <Switch>
                            <Route exact path="/sign-in">
                                <SignIn setFlag={authSet} component={SignIn} />
                            </Route>
                            <Route exact path="/sign-up" component={SignUp} />
                            <Route exact path="/" component={Home} />
                            <Route exact path="/champions" component={Champions} />
                            <Route exact path="/champions/:championName">
                                <DisplayChampion title={title} changeTitle={changeTitle} />
                            </Route>
                            <Route exact path="/items" component={Items} />
                            <Route exact path="/tier-list" component={TierList} />
                            <Route exact path="/lead" component={Leaderboard} />
                            <Route exact path="/how-to-play" component={HowToPlay} />

                            <ProtectedRoutes
                                exact
                                path="/personal-stats"
                                component={PersonalStats}
                                isAuth={isAuthenticated}
                            /> 
                            {/* <Route exact path="/personal-stats" component={PersonalStats} /> */}
                            <ProtectedRoutes
                                exact
                                path="/suggestions"
                                component={Suggestions}
                                isAuth={isAuthenticated}
                            />
                            <ProtectedRoutes exact path="/comparison" component={Comparison} isAuth={isAuthenticated} /> 
                            {/* <Route exact path="/comparison" component={Comparison} isAuth={isAuthenticated} />  */}
                            <ProtectedRoutes exact path="/get-app" component={DownloadApp} isAuth={isAuthenticated} />
                            {/* <Route exact path="/get-app" component={DownloadApp} isAuth={isAuthenticated} /> */}
                        </Switch>
                    </Grid>
                    <Box pt={4}>
                        <Copyright />
                    </Box>
                </Container>
            </main>
        </div>
    );
}
