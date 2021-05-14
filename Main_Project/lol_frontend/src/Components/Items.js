import React, { useState, useEffect } from "react";
import axios from "axios";
import {
    ButtonGroup,
    Typography,
    Button,
    CardMedia,
    CardContent,
    CardActions,
    Card,
    Grid,
    makeStyles,
} from "@material-ui/core";

// import championData from "../Data/allChampionsData";

const useStyles = makeStyles({
    root: {
        background: "#f2e4fd",
    },
});



export default function Champions() {
    const [itemData, setItemData] = useState(null);
    // const classes = useStyles();
    useEffect(() => {
        axios
            .get("https://ddragon.leagueoflegends.com/cdn/11.7.1/data/en_US/item.json")
            .then((res) => {
                // console.log(Object.values(res.data.data));
                setItemData(Object.values(res.data.data));
            })
            .catch((err) => console.log(err));
    }, []);

    const classes = useStyles();
    return (
        <>
            <Grid container spacing={2}>
                {itemData &&
                    itemData.map((props) => {
                        return (
                            <Grid item lg={3} md={4} sm={11} key={props.id}>
                                <Card className={classes.root}>
                
                                    <CardMedia
                                        component="img"
                                        alt="Item Pic"
                                        height="100"
                                        image={`http://ddragon.leagueoflegends.com/cdn/11.9.1/img/item/${props.image.full}`}
                        
                                        title="Item"
                                    />
                                    <CardContent>
                                    <Typography gutterBottom variant="h5" component="h2">
                                        {props.name}
                                    </Typography>
                                    
                                    
                        
                        
                                    <Typography variant="body2" color="primary" component="p">
                                        {props.tags.join("/")}
                                    </Typography>

                                </CardContent>
                                <CardActions>
                                    <Button fullWidth size="medium" color="secondary" variant="contained">
                                        {props.plaintext}
                                    </Button>
                                </CardActions>
                                <CardActions>
                                    <ButtonGroup fullWidth size="small" color="primary" variant="contained">
                                        <Button>Buy {props.gold.base}</Button>
                                        <Button>Sell {props.gold.sell}</Button>
                                    </ButtonGroup>
                                </CardActions>
                
                            </Card>
                        </Grid>
                        );
                    })}
            </Grid>
        </>
    );
}

