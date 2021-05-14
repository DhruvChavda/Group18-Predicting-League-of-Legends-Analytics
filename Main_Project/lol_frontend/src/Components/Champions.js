import React, { useState, useEffect } from "react";
import { Link as RouterLink } from "react-router-dom";
import axios from "axios";
import {
    ButtonGroup,
    Typography,
    Button,
    CardMedia,
    CardContent,
    CardActions,
    CardActionArea,
    Card,
    Grid,
} from "@material-ui/core";

// import championData from "../Data/allChampionsData";

// const useStyles = makeStyles({
//     root: {
//         margin: 5,
//         minWidth: "22%",
//     },
// });

export default function Champions() {
    const [championData, setChampionData] = useState(null);
    // const classes = useStyles();
    useEffect(() => {
        axios
            .get("http://ddragon.leagueoflegends.com/cdn/11.9.1/data/en_US/champion.json")
            .then((res) => {
                // console.log(Object.values(res.data.data));
                setChampionData(Object.values(res.data.data));
            })
            .catch((err) => console.log(err));
    }, []);
    return (
        <Grid container spacing={2}>
            {championData && championData.map(CreateChampions)}
        </Grid>
    );
}

function CreateChampions(props) {
    return (
        <Grid item lg={3} md={4} sm={11} key={props.id}>
            <Card>
                <CardActionArea component={RouterLink} to={`/champions/${props.id}`}>
                    <CardMedia
                        component="img"
                        alt="Champion Pic"
                        height="100"
                        image={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/champion/${props.image.full}`}
                        title="Contemplative Reptile"
                    />
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="h2">
                            {props.name}
                        </Typography>
                        <Typography variant="body2" color="textSecondary" component="p">
                            {props.title}
                        </Typography>
                        <Typography variant="body2" color="primary" component="p">
                            {props.tags.join("/")}
                        </Typography>
                    </CardContent>
                </CardActionArea>
                <CardActions>
                    <ButtonGroup fullWidth size="small" color="primary" variant="contained">
                        <Button>Attack {props.info.attack}</Button>
                        <Button>Defense {props.info.defense}</Button>
                    </ButtonGroup>
                </CardActions>
                <CardActions>
                    <ButtonGroup fullWidth size="small" color="secondary" variant="contained">
                        <Button>magic {props.info.magic}</Button>
                        <Button>difficulty {props.info.difficulty}</Button>
                    </ButtonGroup>
                </CardActions>
            </Card>
        </Grid>
    );
}
